from scriptparser import scene, style_type, transition_type
import ffmpeg

def transition(v0: ffmpeg.nodes.FilterableStream, v1: ffmpeg.nodes.FilterableStream, a0: ffmpeg.nodes.FilterableStream, a1: ffmpeg.nodes.FilterableStream, transition_type: transition_type, duration: float, v0_d: float, v1_d: float, a0_d: float, a1_d:float)->tuple[ffmpeg.nodes.FilterableStream, ffmpeg.nodes.FilterableStream, float, float]:
    
    # if it's not custom, not concat and not error
    if (transition_type != transition_type.CUSTOM) and (transition_type !=transition_type.CONCAT) and (transition_type != transition_type.ERROR):
        temp_clip_v = ffmpeg.filter([v0, v1], 'xfade', transition=transition_type.value, duration=duration, offset=(v0_d-duration-(v0_d-a0_d)))
    elif transition_type == transition_type.CUSTOM:
        print("custom transition requested but not yet supported, I'll give you a fade instead")
        temp_clip_v = ffmpeg.filter([v0, v1], 'xfade', transition=transition_type.FADE.value, duration=duration, offset=(v0_d-duration-(v0_d-a0_d)))
    elif transition_type == transition_type.CONCAT or transition_type == transition_type.ERROR:
        # TODO concatenation filter
        print("concatenation requested")

        if transition_type == transition_type.ERROR:
            print("because of an error, mind you")
    else:
        print("error bro")

    temp_clip_a = ffmpeg.filter([a0,a1], 'acrossfade', duration=duration)

    # calculate the durations of the new clip
    temp_clip_v_d = v0_d + v1_d - duration
    temp_clip_a_d = a0_d + a1_d - duration
    return (temp_clip_v, temp_clip_a, temp_clip_v_d, temp_clip_a_d)

def transitions(script: tuple[dict,list[scene]]):

    # the first clip has no transition in
    header, scenes = script

    temp = scenes[0]

    temp_v = temp.clip
    temp_a = temp.clip.audio
    temp_v_d = float(next((stream for stream in temp.avatar_video.metadata['streams'] if stream['codec_type'] == 'video'), None)['duration'])
    temp_a_d = float(next((stream for stream in temp.avatar_video.metadata['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

    for scene in scenes[1:]:

        scene_v_d = float(next((stream for stream in scene.avatar_video.metadata['streams'] if stream['codec_type'] == 'video'), None)['duration'])
        scene_a_d = float(next((stream for stream in scene.avatar_video.metadata['streams'] if stream['codec_type'] == 'audio'), None)['duration'])

        (temp_v, temp_a, temp_v_d, temp_a_d) = transition(temp_v, scene.clip, temp_a, scene.clip.audio, scene.transition_in.t_type, scene.transition_in.duration, temp_v_d, scene_v_d, temp_a_d, scene_a_d)

    return (script, temp_v, temp_a, temp_v_d, temp_a_d)