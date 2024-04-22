from scriptparser import scene,style_type
import ffmpeg

def compose_scenes(script: tuple[dict,list[scene]]):
    script_head, script_body = script
    for scene in script_body:
        scene.avatar_video.video = ffmpeg.input(scene.avatar_video.filename)
        scene.avatar_video.metadata = ffmpeg.probe(scene.avatar_video.filename)
        if scene.style.style == style_type.PIP:
            scene.clip = scene.avatar_video.video # for now there's not much to do with a pip since we've generated it in heygen
        else:
            print("error unsupported scene style: " + scene.style.style)
    return (script_head, script_body)