from parse import parse_from_file
from upload import upload_script, parse_upload_response, get_slides, get_avatar_clips
from compose import compose_scenes
import sys
from transition import transitions
import ffmpeg
import argparse


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
msg = "This tool is designd to take a correctly marked up text file (preferably .md but .txt works exactly the same) and produce a composed clip with HeyGen"
# Initialize parser
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-i", "--Input", help = "name/location of the file")
args = parser.parse_args()

if args.Input:
    filepath = args.Input
    script = parse_from_file(filepath)
    if script:
        responses = upload_script(script)

        # parse the response content into the scenes - literally just the avatar video ids
        script = parse_upload_response(responses, script)

        # get the slides 
        script = get_slides(script)

        # then go get the links from the videos and download the clips. hopefully they've rendered by now
        #time.sleep(1500)
        script = get_avatar_clips(script)
        print(script)

        # compose the scenes
        script = compose_scenes(script)
        # transitions
        (script, v, a, v_d, a_d) = transitions(script)
        # output video
        ffmpeg.output(v,a, script[0]["Lecture Name"]+".mp4", pix_fmt='yuv420p').run()
    
        # presumably response has the URL of the pending video. for each of the clips get the url. for each one, download it.
        # can't do this section without higher API limit yet
        #print(responses)
    else:
        print(script)