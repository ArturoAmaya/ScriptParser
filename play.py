import ffmpeg

innie = ffmpeg.input('clip1.mp4')
probes = ffmpeg.probe('clip1.mp4')
print(innie)