import requests
from scriptparser import scene
import json
from urllib.request import urlretrieve
import time
# cut up a script and put it into the format of a V2 HeyGen video

def upload_script(script: tuple[dict, list[scene]]):
    # unpack the script
    (script_header, script_body) = script
    responses = []
    for scene in script_body:
        # compose the JSON first
        ## header
        post_header = dict()
        post_header["Content-Type"] = "application/json"
        post_header["x-api-key"] = script_header["HeyGen API key"]

        ## json body
        post_json = dict()
        post_json["video_inputs"] = []
        clip = dict()
        clip["character"] = dict()
        clip["character"]["type"] = "avatar"
        clip["character"]["avatar_id"] = script_header["Avatar ID"]
        clip["character"]["avatar_style"] = "normal"
        clip["character"]["scale"] = scene.style.avatar_scale
        clip["character"]["offset"] = {"x": 1-scene.style.avatar_position[0], "y": 1-scene.style.avatar_position[1]} # TODO revisit I believe hey gen's implementation is different to ffmpeg's. believe they do bottom right indexing or smth idk

        clip["voice"] = dict()
        clip["voice"]["type"] = "text"
        clip["voice"]["input_text"] = scene.text
        clip["voice"]["voice_id"] = script_header["Voice ID"]

        clip["background"] = dict()
        clip["background"]["type"] = "image"
        clip["background"]["url"] = scene.slide.slide_url #script_header["Slides"][script_body.index(line)] if script_body.index(line) < len(script_header["Slides"]) else script_header["Slides"][-1]

        post_json["video_inputs"].append(clip)
        post_json["test"] = True
        post_json["caption"] = True
        post_json["dimension"] = {"width": 1280, "height": 720}

        print(post_json)
        response = requests.post("https://api.heygen.com/v2/video/generate", json = post_json, headers=post_header)
        responses.append(response)
    return responses

def parse_upload_response(responses:list[requests.models.Response], script: tuple[dict,list[scene]])->list[scene]:
    count = 0
    script_header, script_body = script
    for response in responses:
        if response.status_code == 200:
            body = json.loads(response.text)
            script_body[count].avatar_video.id = body["data"]["video_id"]
        else:
            print("Yo, error with video number ", count)
        count = count + 1
    return script

def get_slides(script:list[scene])->list[scene]:
    count  = 0
    script_header, script_body = script
    for scene in script_body:
        if scene.slide.slide_url != None or scene.slide.slide_url != '':
            path, headers = urlretrieve(scene.slide.slide_url, f"slide{count}.jpg") # todo return and decide how to import the file format. don't think this thing cares tho
            scene.slide.slide_filename = path
            count = count + 1
    return script

def get_avatar_clip(scene:scene, apikey:str, count:int, wait:int):
    time.sleep(wait)
    post_header = dict()
    post_header['Content-Type'] = "application/json"
    post_header["x-api-key"] = apikey #script_header["HeyGen API key"]
    response = requests.get("https://api.heygen.com/v1/video_status.get?video_id="+scene.avatar_video.id, headers=post_header)
    if response.status_code == 200:
        body = json.loads(response.text)
        if body["data"]["status"] == "completed":

            # get the url to the video and download it
            scene.avatar_video.url = body["data"]["video_url"]
            path, headers = urlretrieve(scene.avatar_video.url, f"avatar{count}.mp4")
            scene.avatar_video.filename = path

            # get the url to the caption and download it
            scene.caption.caption_url = body["data"]["caption_url"]
            path, headers = urlretrieve(scene.caption.caption_url, f"caption{count}.ass")
            scene.caption.caption_filename = path
            return scene
        else:
            print("trying again with video " + str(scene.number) + " waiting " + str(wait*2))
            return get_avatar_clip(scene, apikey, count, wait*2)
    pass


def get_avatar_clips(script:tuple[dict,list[scene]])->list[scene]:
    count = 0
    script_header, script_body = script
    apikey = script_header["HeyGen API key"]
    for scene in script_body:
        script_body[count] = get_avatar_clip(scene, apikey, count, 50)
        count = count + 1
    return script