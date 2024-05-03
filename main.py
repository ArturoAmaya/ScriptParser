from parse import parse_from_file, restore_intermediate
from upload import upload_script, parse_upload_response, get_slides, get_avatar_clips
from compose import compose_scenes
import sys
from transition import transitions
import ffmpeg
import argparse
import json

def save_intermediate(script: tuple[dict,list[object]], filename:str):
    with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dict(header=script[0],body=[i.to_dict() for i in script[1]]), f, ensure_ascii=False, indent=4)

### OUTLINE:

# parse the text into scenes 
# scene object has porperties like
# - number: what number in the sequence this is
# - style: the type of composition: pip, avatar-only, side by side [for now], slide only
#   - avatar_scale: how big the avatar is
#   - slides_scale: how big the slide image is
#   - avatar_position: where in the image the avatar is
#   - slides_position: where in the image the slide image is
# - slide:
#   - slide_source_type: where the slide is coming from. for now just URL type
#   - slide_url: where to get the slide image from
#   - slide_img: the actual image
# - background:
#   - background_source_type: where the background is coming from URL and static background for now.
#   - background_url: where to get the background from
#   - background_command: how to generate the background if it's a command
# - transition_in:
#   - transition_type: for now only accept fade
#   - tranisiton_duration: how long to make the transition
# - avatar_video:
#   - avatar_video_id: id for the video per heygen
#   - avatar_video_url: the url for the video
#   - avatar_ideo: the video itself
#   - avatar_video_probe: the video data like stream length and such
# - text: the text that is said in this clip
# - clip: the composed clip pre-transition
# - caption:
#   - caption_url: duh
#   - caption_filename: caption filename
#   - parsed_caption: the caption info (start stamp, end stamp, text)

# scripting markup: 
# - \n means new clip
# - \\ mid-clip change

# the order of operations will be: 
# - parse script
# - post to heygen and get the slides assets
# - get the heygen videos from the ids
# - compose the clips
# - splice everything together

# two types of transitions
# - between_clips: that is,the video_id of this clip and the previous is different. 
# - mid_clip: the video_id of this clip and the previous is the same. we have to use caption information to sync them up. 

# I think with this we can do everything except for changing the slides halfway through the avatar clip in a side by side. 
# the problem is that that requires a transition before the composition has finished, and splitting it into two clips means that the avatar resets
# it's ok if we make the transition methods available to the composition algorithm. we can specify that this is a special scene and follow a special order.


# V
#filepath = sys.argv[1]
msg = "This tool is designed to take a correctly marked up text file (preferably .md but .txt works exactly the same) and produce a composed clip with HeyGen"
# Initialize parser
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-is", "--Input-script", type=str, help="name/location of the input file")
#subparsers = parser.add_subparsers(help="sub-command help")
# make a save intermediate subparser
#save_parser = subparsers.add_parser('--save-intermediate', default=False, action="store_true", help="Save intermediate versions of the script")

parser.add_argument("--save-intermediate", default=False, action="store_true", help="Save intermediate versions of the script")
parser.add_argument("-if", "--intermediate-filename", type=str, default="data.json", help="Name of the intermediate data file to be written")


parser.add_argument("--load-intermediate", default=False, action="store_true", help="Load intermediate y/n")
parser.add_argument("-s", "--intermediate-stage", default=0, type=int, help="stage of the intermediate file")
parser.add_argument("-in", "--Input-intermediate", default="data.json", help="name/location of the intermediate file to be read")

parser.add_argument("-d", "--Destination", default="./", type=str, help="base destination folder for downloads")

parser.add_argument("-f", "--force", default=False, action="store_true", help="Force overwrite a file with matching name")
args = parser.parse_args()

if args.Input_script and not args.load_intermediate:

    # at stage 0 right now
    filepath = args.Input_script
    script = parse_from_file(filepath)
    if args.save_intermediate:
        save_intermediate(script, args.Destination+args.intermediate_filename)

    # stage 1 - after file parse
    if script:
        responses = upload_script(script)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)
        # parse the response content into the scenes - literally just the avatar video ids
        script = parse_upload_response(responses, script)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 2 - after parsing upload response
        # get the slides 
        script = get_slides(script, args.Destination)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 3 - after getting slides
        # then go get the links from the videos and download the clips. hopefully they've rendered by now
        #time.sleep(1500)
        script = get_avatar_clips(script, args.Destination)
        print(script)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 4 - after getting all the assets. At this point there's no point splititng up stages since we can serialize an ffmpeg transition node or a video
        # compose the scenes
        script = compose_scenes(script)
        # transitions
        (script, v, a, v_d, a_d) = transitions(script)
        # output video
        ffmpeg.output(v,a, args.Destination+script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p', vcodec="h264", crf=18, preset="veryslow").run(overwrite_output=args.force)
    
        # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
        # can't do this section without higher API limit yet
        #print(responses)
    else:
        print(script)
else:
    # choose the intermediate stage to start from:
    if (args.intermediate_stage == 0):
        print("start from the beginning you weirdo")
        filepath = args.Input_script
        script = parse_from_file(filepath)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 1 - after file parse
        if script:
            responses = upload_script(script)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)
            # parse the response content into the scenes - literally just the avatar video ids
            script = parse_upload_response(responses, script)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)

            # stage 2 - after parsing upload response
            # get the slides 
            script = get_slides(script, args.Destination)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)

            # stage 3 - after getting slides
            # then go get the links from the videos and download the clips. hopefully they've rendered by now
            #time.sleep(1500)
            script = get_avatar_clips(script, args.Destination)
            print(script)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)

            # stage 4 - after getting all the assets. At this point there's no point splititng up stages since we can serialize an ffmpeg transition node or a video
            # compose the scenes
            script = compose_scenes(script)
            # transitions
            (script, v, a, v_d, a_d) = transitions(script)
            # output video
            ffmpeg.output(v,a, script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p', vcodec="h264", crf=18, preset="veryslow").run(overwrite_output=args.force)
        
            # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
            # can't do this section without higher API limit yet
            #print(responses)
        else:
            print(script)
    elif (args.intermediate_stage == 1):
        print("start from 1")
        f = open(args.Input_intermediate)
        script = restore_intermediate(json.load(f))
        f.close()
        # stage 1 - after file parse
        if script:
            responses = upload_script(script)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)
            # parse the response content into the scenes - literally just the avatar video ids
            script = parse_upload_response(responses, script)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)

            # stage 2 - after parsing upload response
            # get the slides 
            script = get_slides(script, args.Destination)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)

            # stage 3 - after getting slides
            # then go get the links from the videos and download the clips. hopefully they've rendered by now
            #time.sleep(1500)
            script = get_avatar_clips(script, args.Destination)
            print(script)
            if args.save_intermediate:
                save_intermediate(script, args.Destination+args.intermediate_filename)

            # stage 4 - after getting all the assets. At this point there's no point splititng up stages since we can serialize an ffmpeg transition node or a video
            # compose the scenes
            script = compose_scenes(script)
            # transitions
            (script, v, a, v_d, a_d) = transitions(script)
            # output video
            ffmpeg.output(v,a, script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p', vcodec="h264", crf=18, preset="veryslow").run(overwrite_output=args.force)
        
            # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
            # can't do this section without higher API limit yet
            #print(responses)
        else:
            print(script)
    elif (args.intermediate_stage == 2):
        print("start from 2")
        f = open(args.Input_intermediate)
        script = restore_intermediate(json.load(f))
        f.close()
        script = get_slides(script, args.Destination)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 3 - after getting slides
        # then go get the links from the videos and download the clips. hopefully they've rendered by now
        #time.sleep(1500)
        script = get_avatar_clips(script, args.Destination)
        print(script)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 4 - after getting all the assets. At this point there's no point splititng up stages since we can serialize an ffmpeg transition node or a video
        # compose the scenes
        script = compose_scenes(script)
        # transitions
        (script, v, a, v_d, a_d) = transitions(script)
        # output video
        ffmpeg.output(v,a, script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p', vcodec="h264", crf=18, preset="veryslow").run(overwrite_output=args.force)
        
        # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
        # can't do this section without higher API limit yet
        #print(responses)
        
    elif (args.intermediate_stage == 3):
        print("start from 3")
        f = open(args.Input_intermediate)
        script = restore_intermediate(json.load(f))
        f.close()
        # stage 3 - after getting slides
        # then go get the links from the videos and download the clips. hopefully they've rendered by now
        #time.sleep(1500)
        script = get_avatar_clips(script, args.Destination)
        print(script)
        if args.save_intermediate:
            save_intermediate(script, args.Destination+args.intermediate_filename)

        # stage 4 - after getting all the assets. At this point there's no point splititng up stages since we can serialize an ffmpeg transition node or a video
        # compose the scenes
        script = compose_scenes(script)
        # transitions
        (script, v, a, v_d, a_d) = transitions(script)
        # output video
        ffmpeg.output(v,a, script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p', vcodec="h264", crf=18, preset="veryslow").run(overwrite_output=args.force)
        
        # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
        # can't do this section without higher API limit yet
        #print(responses)
    elif (args.intermediate_stage == 4):
        print("start from 4")
        f = open(args.Input_intermediate)
        script = restore_intermediate(json.load(f))
        f.close()
        # stage 4 - after getting all the assets. At this point there's no point splititng up stages since we can serialize an ffmpeg transition node or a video
        # compose the scenes
        script = compose_scenes(script)
        # transitions
        (script, v, a, v_d, a_d) = transitions(script)
        # output video
        ffmpeg.output(v,a, script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p', vcodec="h264", crf=18, preset="veryslow").run(overwrite_output=args.force)
        
        # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
        # can't do this section without higher API limit yet
        #print(responses)
    else:
        print("invalid argument bruv")
         