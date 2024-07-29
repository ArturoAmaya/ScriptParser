import ffmpeg

slide = ffmpeg.input('./long_scripts/slides/out0.jpg', **{'loop':'1', })
clip = ffmpeg.input('./longrun/demo1.md/avatar1.mp4')#ffmpeg.input('SidebysideClip.mp4')

scaled_clip = clip.filter('scale', *['0.4*iw', '0.4*ih'])


# this overlay thing does the placement based on the top left corner of the overlay video

# bottom right
#overlaid = ffmpeg.filter([slide, scaled_clip], 'overlay', shortest=1, x='main_w-overlay_w', y='main_h-overlay_h')

# top right
#overlaid = ffmpeg.filter([slide, scaled_clip], 'overlay', shortest=1, x='main_w-overlay_w', y='0')

# top left
#overlaid = ffmpeg.filter([slide, scaled_clip], 'overlay', shortest=1, x='0', y='0')

# bottom left
overlaid = ffmpeg.filter([slide, scaled_clip], 'overlay', shortest=1, x='0', y='main_h-overlay_h')


ffmpeg.output(overlaid, clip.audio, "AH.mp4").run()
