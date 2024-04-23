import ffmpeg
import transition
from scriptparser import transition_type

vid1 = ffmpeg.input('avatar0.mp4')
probe1 = ffmpeg.probe('avatar0.mp4')

vid2 = ffmpeg.input('avatar1.mp4')
probe2 = ffmpeg.probe('avatar1.mp4')
#video_stream = next((stream for stream in probes['streams'] if stream['codec_type'] == 'video'), None)
#print(probes)
#outie = ffmpeg.input('vid.mp4')

#width = int(video_stream['width'])
#height = int(video_stream['height'])
#innie = innie.filter('scale', width = f"{width/4}", height=f"{height/4}").output('output.mp4').run()

# let's try a fade transition
vid1_vid_stream = next((stream for stream in probe1['streams'] if stream['codec_type'] == 'video'), None)
vid1_audio_stream = next((stream for stream in probe1['streams'] if stream['codec_type'] == 'audio'), None)

vid2_vid_stream = next((stream for stream in probe2['streams'] if stream['codec_type'] == 'video'), None)
vid2_audio_stream = next((stream for stream in probe2['streams'] if stream['codec_type'] == 'audio'), None)


clip =ffmpeg.filter([vid1,vid2], 'xfade', transition='fade', duration=1, offset=(float(vid1_vid_stream['duration'])-1-(float(vid1_vid_stream['duration'])-float(vid1_audio_stream['duration']))))
audio = ffmpeg.filter([vid1.audio, vid2.audio], 'acrossfade', duration=1)
ffmpeg.output(clip,audio,'output.mp4', pix_fmt='yuv420p').run()


#vid1 = vid1.filter('xfade', duration=1, offset=(float(vid1_vid_stream['duration'])-1-(float(vid1_vid_stream['duration'])-float(vid1_audio_stream['duration']))))

(v, a, v_d, a_d) = transition.transition(vid1,vid2,vid1.audio,
                                         vid2.audio,transition_type.FADE,1.0,
                                         float(vid1_vid_stream['duration']), float(vid2_vid_stream['duration']), float(vid1_audio_stream['duration']), float(vid2_audio_stream['duration']))
ffmpeg.output(v,a,'output2.mp4',pix_fmt='yuv420p').run()

vid3 = ffmpeg.input('avatar2.mp4')
probe3 = ffmpeg.probe('avatar2.mp4')
vid3_vid_stream = next((stream for stream in probe3['streams'] if stream['codec_type'] == 'video'), None)
vid3_audio_stream = next((stream for stream in probe3['streams'] if stream['codec_type'] == 'audio'), None)

(v,a,v_d,a_d) = transition.transition(v,vid3,a,vid3.audio,transition_type.FADE, 1.0, v_d, float(vid3_vid_stream['duration']), a_d, float(vid3_audio_stream['duration']))
ffmpeg.output(v,a,'output3.mp4', pix_fmt='yuv420p').run()
