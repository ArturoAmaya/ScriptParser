import ffmpeg

innie = ffmpeg.input('vid.mp4')
probes = ffmpeg.probe('vid.mp4')
video_stream = next((stream for stream in probes['streams'] if stream['codec_type'] == 'video'), None)
print(probes)
outie = ffmpeg.input('vid.mp4')

width = int(video_stream['width'])
height = int(video_stream['height'])
innie = innie.filter('scale', width = f"{width/4}", height=f"{height/4}").output('output.mp4').run()