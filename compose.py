from scriptparser import scene,style_type
import ffmpeg
import ass,re

def find_midclip_cut(midlinetext: str, count:int, caption_events:ass.EventsSection):
    found = False
    while count > 0 and not found:
        first_words = re.compile('^(( *([\w\\-\'\"\,\.\?\!\;]+)){'+str(count)+'})') #find the first five words, including -, ", ,, ., ?, !, ;
        first_words = first_words.search(midlinetext).group().strip()
        for event in caption_events:
            found = True if event.text.replace('\\n', '').replace(' \'', '\'').find(first_words) != -1 else False
            if found:
                return event.end.total_seconds()
        count = count - 1
    return -1


def compose_scenes(script: tuple[dict,list[scene]]):
    script_head, script_body = script
    for scene in script_body:
        scene.avatar_video.video = ffmpeg.input(scene.avatar_video.filename)
        scene.avatar_video.metadata = ffmpeg.probe(scene.avatar_video.filename)

        # if this is the backhalf of a midline cut
        if scene.midline_cut:
            # try to find where the nearest phrase to the one indicated ends
            with open(scene.caption.caption_filename) as f:
                scene.parsed_caption = ass.parse(f)
            
            # try to match 5 words from the start of the multiline text
            cut_point = find_midclip_cut(scene.midline_text, 5, scene.parsed_caption.events)
            
            if script_body.index(scene)+1 < len(script_body) and script_body[script_body.index(scene)+1].midline_cut:
                # write to file and get it back TODO without write to file if possible
                v = scene.avatar_video.video.trim(start=cut_point, end=find_midclip_cut(script_body[script_body.index(scene)+1].midline_text, 5, scene.parsed_caption.events)).filter('setpts', 'PTS-STARTPTS')
                a = scene.avatar_video.video.audio.filter('atrim', start=cut_point, end=find_midclip_cut(script_body[script_body.index(scene)+1].midline_text, 5, scene.parsed_caption.events)).filter('asetpts', 'PTS-STARTPTS') # need to setpts so that the new clip has adjusted duration otherwise its same length but silent/frozen until the part that made it through the trim arrives
                ffmpeg.output(v,a,f"./trim{scene.number}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True)
                scene.avatar_video.video = ffmpeg.input(f"./trim{scene.number}.mp4")
                scene.avatar_video.metadata = ffmpeg.probe(f"./trim{scene.number}.mp4")
            else:
                # write to file and get it back TODO without write to file if possible
                v = scene.avatar_video.video.trim(start=cut_point, end=float(scene.avatar_video.metadata['streams'][0]['duration'])).filter('setpts', 'PTS-STARTPTS')
                a = scene.avatar_video.video.audio.filter('atrim', start=cut_point).filter('asetpts', 'PTS-STARTPTS') # need to setpts so that the new clip has adjusted duration otherwise its same length but silent/frozen until the part that made it through the trim arrives
                ffmpeg.output(v,a,f"./trim{scene.number}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True)
                scene.avatar_video.video = ffmpeg.input(f"./trim{scene.number}.mp4")
                scene.avatar_video.metadata = ffmpeg.probe(f"./trim{scene.number}.mp4")

        elif script_body.index(scene)+1 < len(script_body) and script_body[script_body.index(scene)+1].midline_cut: # if this is the front half of a midline cut
            # try to find where the nearest phrase to the one indicated ends
            with open(scene.caption.caption_filename) as f:
                scene.parsed_caption = ass.parse(f)
            
            # try to match 5 words from the start of the multiline text
            cut_point = find_midclip_cut(script_body[script_body.index(scene)+1].midline_text, 5, scene.parsed_caption.events)
            
            # write to file and get it back TODO without write to file if possible
            v = scene.avatar_video.video.trim(start=0, end=cut_point).filter('setpts', 'PTS-STARTPTS')
            a = scene.avatar_video.video.audio.filter('atrim', start=0, end=cut_point).filter('asetpts', 'PTS-STARTPTS')
            ffmpeg.output(v,a,f"./trim{scene.number}.mp4", vcodec="h264", pix_fmt='yuv420p', crf=18, preset="veryslow", **{'b:a': '192k'}).run(overwrite_output=True)
            scene.avatar_video.video = ffmpeg.input(f"./trim{scene.number}.mp4")
            scene.avatar_video.metadata = ffmpeg.probe(f"./trim{scene.number}.mp4")
        
        if scene.style.style == style_type.PIP:
            scene.clip = scene.avatar_video.video # for now there's not much to do with a pip since we've generated it in heygen
        elif scene.style.style == style_type.AVATAR:
            scene.clip = scene.avatar_video.video
        elif scene.style.style == style_type.VOICEOVER:
            # TODO REVISIT THIS THIS IS BRITTLE
             
            # get the slide
            slide = ffmpeg.input(scene.slide.slide_filename, **{'loop':'1'})
            
            # cut the audio out
            ffmpeg.output(scene.avatar_video.video.audio, f"{scene.avatar_video.filename}.mp3").run()
            audio = ffmpeg.input(f"{scene.avatar_video.filename}.mp3")

            # then put em together
            ffmpeg.concat(slide, audio,v=1,a=1).output(f"{scene.avatar_video.filename}_voiceover.mp4", shortest=None).run()
            scene.clip = ffmpeg.input(f"{scene.avatar_video.filename}_voiceover.mp4")
        else:
            raise Exception("error unsupported scene style: " + scene.style.style)

    return (script_head, script_body)