from scriptparser import scene, style_type, transition_type
import ffmpeg

def transition(v0: ffmpeg.nodes.FilterableStream, v1: ffmpeg.nodes.FilterableStream, a0: ffmpeg.nodes.FilterableStream, a1: ffmpeg.nodes.FilterableStream, transition_type: transition_type, duration: float, v0_d: float, v1_d: float, a0_d: float, a1_d:float)->tuple[ffmpeg.nodes.FilterableStream, ffmpeg.nodes.FilterableStream, float, float]:
    
    if transition_type == transition_type.FADE:
        temp_clip_v = ffmpeg.filter([v0, v1], 'xfade', transition='fade', duration=duration, offset=(v0_d-duration-(v0_d-a0_d)))
    else: 
        print("unsupported transition type")

    temp_clip_a = ffmpeg.filter([a0,a1], 'acrossfade', duration=duration)

    # calculate the durations of the new clip
    temp_clip_v_d = v0_d + v1_d - duration
    temp_clip_a_d = a0_d + a1_d - duration
    return (temp_clip_v, temp_clip_a, temp_clip_v_d, temp_clip_a_d)

def transitions(script: tuple[dict,list[scene]]):

    pass