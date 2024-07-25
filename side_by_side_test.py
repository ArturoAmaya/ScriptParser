import ffmpeg

margin = 10
c = 4*margin


output_dim = (1280,720)

# import background, clip and slide
bckgrnd = ffmpeg.input(f'color=pink:size={output_dim[0]}x{output_dim[1]}', f='lavfi').video  # background with color string, captials work too
clip = ffmpeg.input('./longrun/demo2.md/avatar4.mp4')#ffmpeg.input('SidebysideClip.mp4')
slide = ffmpeg.input('./long_scripts/slides/out0.jpg', **{'loop':'1', })

cropped_avatar_dim = (int((output_dim[0]-c)/3), int(int((output_dim[0]-c)/3)*output_dim[1]/output_dim[0]))
scaled_slides_dim = (2*cropped_avatar_dim[0], 2*cropped_avatar_dim[1])

cropped_avatar = clip.filter('crop', *['iw/2', 'ih', '325', '0']).filter('scale', *[str(cropped_avatar_dim[0]), str(2*cropped_avatar_dim[1])]) # in width, height, x, y format
scaled_slides = slide.filter('scale', *[str(scaled_slides_dim[0]), str(scaled_slides_dim[1])])#*['1280', '720'])#*['0.9*iw', '0.9*ih'])


bkgnd_slides = ffmpeg.filter([bckgrnd, scaled_slides], 'overlay', shortest=1, x=str(margin), y='(main_h-overlay_h)/2') #*['10','(main_h-overlay_h)/2'])
out = ffmpeg.filter([bkgnd_slides, cropped_avatar], 'overlay', shortest= 1, x=str(3*margin+scaled_slides_dim[0]), y='(main_h-overlay_h)/2')

#ffmpeg.concat(out, clip.audio, v=1, a=1).output("AH.mp4").run()
ffmpeg.output(out, clip.audio, "AH.mp4").run()

# ffmpeg -f lavfi -i color=c=blue:s=1920x1080:r=24 
# -i LectureSlides1.mov 
# -i Sidebysideclip.mp4 
# -filter_complex 
# "[2:v]crop=w=iw/2:h=0.9*ih:x=325:y=0[cropped_avatar];
# [1:v]scale=w=0.9*iw:h=0.9*ih[scaled_slides];
# [0:v][scaled_slides]overlay=10:(main_h-overlay_h)/2:shortest=1[bkgnd_slides];
# [bkgnd_slides][cropped_avatar]overlay=main_w-overlay_w-20:(main_h-overlay_h)/2:shortest=1[out]" 
# -map "[out]" -map 2:a side_by_side_test.mp4

# this works perfectly ffmpeg -f lavfi -i color=c=blue:s=1920x1080:r=24 -loop 1 -i ./long_scripts/slides/out0.jpg -i Sidebysideclip.mp4 -filter_complex "[2:v]crop=w=iw/2:h=0.9*ih:x=325:y=0[cropped_avatar];[1:v]scale=w=0.9*iw:h=0.9*ih[scaled_slides];[0:v][scaled_slides]overlay=10:(main_h-overlay_h)/2:shortest=1[bkgnd_slides];[bkgnd_slides][cropped_avatar]overlay=main_w-overlay_w-20:(main_h-overlay_h)/2:shortest=1[out]" -map "[out]" -map 2:a side_by_side_test.mp4