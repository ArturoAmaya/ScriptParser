from scriptparser import scene, style_type, transition_type
import ffmpeg
import os

def transition(v0: ffmpeg.nodes.FilterableStream, v1: ffmpeg.nodes.FilterableStream, a0: ffmpeg.nodes.FilterableStream, a1: ffmpeg.nodes.FilterableStream, transition_type: transition_type, duration: float, v0_d: float, v1_d: float, a0_d: float, a1_d:float)->tuple[ffmpeg.nodes.FilterableStream, ffmpeg.nodes.FilterableStream, float, float]:
    
    # if it's not custom, not concat and not error
    if (transition_type != transition_type.CUSTOM) and (transition_type !=transition_type.CONCAT) and duration != 0.0:
        temp_clip_v = ffmpeg.filter([v0, v1], 'xfade', transition=transition_type.value, duration=duration, offset=(v0_d-duration-(v0_d-a0_d)))
        temp_clip_a = ffmpeg.filter([a0,a1], 'acrossfade', duration=duration)

        # calculate the durations of the new clip
        temp_clip_v_d = v0_d + v1_d - duration # TODO check this
        temp_clip_a_d = a0_d + a1_d - duration
    elif transition_type == transition_type.CUSTOM:
        print("custom transition requested but not yet supported, I'll give you a fade WITH NO AUDIO instead")
        temp_clip_v = ffmpeg.filter([v0, v1], 'xfade', transition=transition_type.FADE.value, duration=duration, offset=(v0_d-duration-(v0_d-a0_d)))
    elif transition_type == transition_type.CONCAT or duration==0:
        print("concatenation requested or you gave me a 0")

        # NOTE: per https://github.com/kkroening/ffmpeg-python/issues/137 there is a slow concat and a fast concat. fast concat takes a file list and is executed at the moment of input, which is a problem for me. We will consider adding this later, but for now do slow concat
        
        # I've figured out that concat seems to work a little weird, so
        
        # trim the first video stream to match the audio length
        temp_clip_v = ffmpeg.filter(v0, 'trim', start=0.0, end=a0_d)
        # concat the video streams
        temp_clip_v = ffmpeg.concat(temp_clip_v, v1,a=0,v=1)
        temp_clip_v = ffmpeg.filter(temp_clip_v, 'settb', 1/12800)
        
        temp_clip_a = ffmpeg.concat(a0,a1, v=0, a=1)

        temp_clip_v_d = v0_d + v1_d # TODO check this originally v0_d
        temp_clip_a_d = a0_d + a1_d
    else:
        print("error bro")
#[0:v][1:v]concat=a=0:n=1:v=2[s0];[s0][2]xfade=duration=1.0:offset=64.97395800000001:transition=hrwind[s1];[s1][3]xfade=duration=1.0:offset=99.168937:transition=dissolve[s2];[s2][4]xfade=duration=1.0:offset=127.93991600000001:transition=fade[s3];[0:a][1:a]concat=a=2:n=1:v=0[s4];[s4:a][2:a]acrossfade=duration=1.0[s5];[s5][3:a]acrossfade=duration=1.0[s6];[s6][4:a]acrossfade=duration=1.0[s7]
    
    return (temp_clip_v, temp_clip_a, temp_clip_v_d, temp_clip_a_d)

def transitions(script: tuple[dict,list[scene]]):

    # the first clip has no transition in
    header, scenes = script

    temp = scenes[0]

    temp_v = temp.clip.video
    temp_a = temp.clip.audio
    temp_v_d = float(next((stream for stream in temp.avatar_video.metadata['streams'] if stream['codec_type'] == 'video'), None)['duration'])
    temp_a_d = float(next((stream for stream in temp.avatar_video.metadata['streams'] if stream['codec_type'] == 'audio'), None)['duration'])
    count = 0
    for scene in scenes[1:]:

        scene_v_d = float(next((stream for stream in scene.avatar_video.metadata['streams'] if stream['codec_type'] == 'video'), None)['duration'])
        scene_a_d = float(next((stream for stream in scene.avatar_video.metadata['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

        (temp_v, temp_a, temp_v_d, temp_a_d) = transition(temp_v, scene.clip, temp_a, scene.clip.audio, scene.transition_in.t_type, scene.transition_in.duration, temp_v_d, scene_v_d, temp_a_d, scene_a_d)
        
        # apparently if I try to hold everything in memory I lose some buffers doing anything above 5 clips together, so I'm writing to file in the meantime
        # apparently you also lose a ton of audio quality if you leave default settings so I'm making it lossless and really slow to see what happens
        count = count + 1
        if count%4 == 0:
            ffmpeg.output(temp_v,temp_a, f"temp{count//4}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True)
            temp = ffmpeg.input(f"temp{count//4}.mp4")
            temp_v = temp.video
            temp_a = temp.audio
            # does re-writing make a different a and v stream length? in calculations temp1 has a_d 155.534895 and v_d 158.12 but the file has 155.573 and 156.08 respectively.
            # what if we don't read the new ones?
            # what if we only read the video number but keep the calculated audio
            temp_probe = ffmpeg.probe(f"temp{count//4}.mp4")
            temp_v_d = float(next((stream for stream in temp_probe['streams'] if stream['codec_type'] == 'video'), None)['duration'])
            temp_a_d = float(next((stream for stream in temp_probe['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

    return (script, temp_v, temp_a, temp_v_d, temp_a_d)