# dummy version of a long video wrapper. basically given a folder it'll run through them and do all of them then concat them all
from subprocess import call
import argparse
import os
import shutil
import json
import ffmpeg
from transition import transition
from scriptparser import transition_type

skiplist = ["demo1.md", "demo2.md", "demo3.md", "demo4.md", "demo5.md"]#"notebook_script1.md","notebook_script2.md","notebook_script3.md","notebook_script4.md","notebook_script5.md"]
#"demo1.md", "demo2.md","demo3.md", "demo4.md"]#["demo1.md", "demo2.md"]

msg = "very dumb wrapper for making long form videos"

parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-if", "--input-folder", type=str, help="name of the input folder")
args = parser.parse_args()

#try:
#    shutil.rmtree("./longrun")
#except:
#    print("ok not there")
#call(["mkdir", "longrun"])

#for root, dirs, files in os.walk(args.input_folder):
for filename in sorted(os.listdir(args.input_folder)):
#    for filename in sorted(files):
    print(filename)#call(["ls", "-l", "./assets"])
    if filename not in skiplist and filename[-3:]==".md":
        # for each filename make a folder inside longrun
        call(["mkdir", f"./longrun/{filename}"])

        # call main in that folder
        call(["python3", "main.py", "-is", f"{args.input_folder}/{filename}", "--save-intermediate", "-d", f"./longrun/{filename}/"])

clips = []
probes = []

for i in range(3): # 40 was way too much
    for filename in sorted(os.listdir(args.input_folder)):
        meta = None
    
        try:
            # grab the json and get the output filename
            with open(f"./longrun/{filename}/data.json") as f:
                meta = json.load(f)
            vid = meta["header"]["Lecture Name"] # the name of the video file output
            clips.append(ffmpeg.input(f"./longrun/{filename}/{vid}.mp4"))
            probes.append(ffmpeg.probe(f"./longrun/{filename}/{vid}.mp4"))
        except:
            print(f"no folder with name {filename}")
temp_v = clips[0].video
temp_a = clips[0].audio
temp_v_d = float(next((stream for stream in probes[0]['streams'] if stream['codec_type'] == 'video'), None)['duration'])
temp_a_d = float(next((stream for stream in probes[0]['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

count = 0
for clip in clips[1:]:

    scene_v_d = float(next((stream for stream in probes[clips.index(clip)]['streams'] if stream['codec_type'] == 'video'), None)['duration'])
    scene_a_d = float(next((stream for stream in probes[clips.index(clip)]['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

    (temp_v, temp_a, temp_v_d, temp_a_d) = transition(temp_v, clip, temp_a, clip.audio, transition_type("concat"), 1.0, temp_v_d, scene_v_d, temp_a_d, scene_a_d)
    count = count + 1
    if count%4 == 0:

        # gpu high bitrate
        # ffmpeg.output(temp_v,temp_a, f"./hw_accel_test/high_quality_hw/temp{count//4}.mp4", **{'pix_fmt':'yuv420p','profile:v':'high','b:v': '6000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        # temp = ffmpeg.input(f"./hw_accel_test/high_quality_hw/temp{count//4}.mp4") 
        # ffmpeg.output(temp_v, temp_a, "./hw_accel_test/high_quality_hw/final.mp4", **{'pixel_format':'yuv420p','profile:v':'high','b:v': '6000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox', 'pix_fmt':'yuv420p'}).run(overwrite_output=True)

        # high bitrate gpu plus sw end
        # ffmpeg.output(temp_v,temp_a, f"./hw_accel_test/hw_then_sw/temp{count//4}.mp4", **{'pix_fmt':'yuv420p','profile:v':'high','b:v': '6000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        # temp = ffmpeg.input(f"./hw_accel_test/hw_then_sw/temp{count//4}.mp4") 
        # ffmpeg.output(temp_v, temp_a, "./hw_accel_test/high_quality_hw/final.mp4", **{'pixel_format':'yuv420p','profile:v':'high','b:v': '6000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox', 'pix_fmt':'yuv420p'}).run(overwrite_output=True)

        # actual longrun
        ffmpeg.output(temp_v,temp_a, f"./temp{count//4}.mp4", **{'pix_fmt':'yuv420p','profile:v':'high','b:v': '6000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        temp = ffmpeg.input(f"./temp{count//4}.mp4") 
        
        # sw_only:
        # ffmpeg.output(temp_v,temp_a, f"./hw_accel_test/sw_only/temp{count//4}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        # temp = ffmpeg.input(f"./hw_accel_test/sw_only/temp{count//4}.mp4") 
        # ffmpeg.output(temp_v, temp_a, "./hw_accel_test/sw_only/final.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True)

        # sw_only multithreaded 30:
        #ffmpeg.output(temp_v,temp_a, f"./hw_accel_test/sw_multithread_4/temp{count//4}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k', 'threads':'30'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        #temp = ffmpeg.input(f"./hw_accel_test/sw_multithread_4/temp{count//4}.mp4") 
        # ffmpeg.output(temp_v, temp_a, "./hw_accel_test/sw_only/final.mp4" , vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k', 'threads':'4'}).run(overwrite_output=True)

        # sw_only multithreaded 16:
        # ffmpeg.output(temp_v,temp_a, f"./hw_accel_test/sw_multithread_16/temp{count//4}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k', 'threads':'16'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        # temp = ffmpeg.input(f"./hw_accel_test/sw_multithread_16/temp{count//4}.mp4") 
        # ffmpeg.output(temp_v, temp_a, "./hw_accel_test/sw_only/final.mp4" , vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k', 'threads':'4'}).run(overwrite_output=True)

        # hw _low bitrate
        #ffmpeg.output(temp_v,temp_a, f"./hw_accel_test/low_quality_hw/temp{count//4}.mp4", **{'pix_fmt':'yuv420p','profile:v':'high','b:v': '2000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox'}).run(overwrite_output=True) # vcodec h264 apparently interferes with GPU accel, which is done with h264_videotoolbox b:v replaces crf for quality preset very slow not needed. seems to work with mpeg color range we can figure out how to set it to 
        #temp = ffmpeg.input(f"./hw_accel_test/low_quality_hw/temp{count//4}.mp4")
        # ffmpeg.output(temp_v, temp_a, "./hw_accel_test/low_quality_hw/final.mp4", **{'pixel_format':'yuv420p','profile:v':'high','b:v': '2000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox', 'pix_fmt':'yuv420p'}).run(overwrite_output=True)

        temp_v = temp.video
        temp_a = temp.audio
        # does re-writing make a different a and v stream length? in calculations temp1 has a_d 155.534895 and v_d 158.12 but the file has 155.573 and 156.08 respectively.
        # what if we don't read the new ones?
        # what if we only read the video number but keep the calculated audio
        temp_probe = ffmpeg.probe(f"./temp{count//4}.mp4")
        temp_v_d = float(next((stream for stream in temp_probe['streams'] if stream['codec_type'] == 'video'), None)['duration'])
        temp_a_d = float(next((stream for stream in temp_probe['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

#return (script, temp_v, temp_a, temp_v_d, temp_a_d)
ffmpeg.output(temp_v, temp_a, "./final.mp4", **{'pixel_format':'yuv420p','profile:v':'high','b:v': '6000k', 'b:a': '192k', 'c:v': 'h264_videotoolbox', 'pix_fmt':'yuv420p'}).run(overwrite_output=True)

# REENCODE IN SW
temp = ffmpeg.input(f"./final.mp4") 
temp_v = temp.video
temp_a = temp.audio
ffmpeg.output(temp_v, temp_a, "./final_sw.mp4" , vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True)
