import requests
from scriptparser import scene, style_type, avatar_style
import json
from urllib.request import urlretrieve
import time, sys, re
# cut up a script and put it into the format of a V2 HeyGen video

def upload_script(script: tuple[dict, list[scene]]):
    # unpack the script
    (script_header, script_body) = script
    responses = []
    for scene in script_body:
        # compose the JSON first
        ## header
        if scene.style.style == style_type.PIP:
            post_header = dict()
            post_header["Content-Type"] = "application/json"
            post_header["x-api-key"] = script_header["HeyGen API key"]

            ## json body
            post_json = dict()
            post_json["video_inputs"] = []
            clip = dict()
            clip["character"] = dict()
            clip["character"]["type"] = "avatar"
            clip["character"]["avatar_id"] = scene.avatar_video.avatar_id #script_header["Default Avatar ID"]
            clip["character"]["avatar_style"] = scene.avatar_video.style.value
            clip["character"]["scale"] = scene.avatar_video.scale
            clip["character"]["offset"] = {"x": scene.avatar_video.position[0]-0.5, "y": scene.avatar_video.position[1]-0.5} 
            # hey gen uses offset of of the middle of the canvas for the 
            # middle of the avatar so middle middle is 0.0,0.0, bottom left is -0.25,0.25 etc . 
            # I want to use top-left is 0.0 because I believe that is how ffmpeg does it
            # my (0,0) (top-left) is heygen's -0.5,-0.5. We can tentatively use me-0.5
            if scene.avatar_video.style == avatar_style.CIRCLE:
                clip["character"]["circle_background_color"] = scene.avatar_video.circle_background

            clip["voice"] = dict()
            if scene.audio_file == None:
                clip["voice"]["type"] = "text"
                clip["voice"]["input_text"] = scene.text
                clip["voice"]["voice_id"] = scene.avatar_video.voice_id #script_header["Default Voice ID"]
            else:
                clip["voice"]["type"] = "audio"
                clip["voice"]["audio_asset_id"] = scene.audio_asset_id

            clip["background"] = dict()
            clip["background"]["type"] = "image"
            if "pdf" in script_header:
                clip["background"]["image_asset_id"] = scene.slide.asset_id
            else:
                clip["background"]["url"] = scene.slide.slide_url #script_header["Slides"][script_body.index(line)] if script_body.index(line) < len(script_header["Slides"]) else script_header["Slides"][-1]

            post_json["video_inputs"].append(clip)
            post_json["test"] = True
            post_json["caption"] = True
            post_json["dimension"] = {"width": scene.style.output_dim[0], "height": scene.style.output_dim[1]}

            print(post_json)
            response = requests.post("https://api.heygen.com/v2/video/generate", json = post_json, headers=post_header)
            responses.append(response)
        elif scene.style.style == style_type.AVATAR or scene.style.style == style_type.VOICEOVER:
            post_header = dict()
            post_header["Content-Type"] = "application/json"
            post_header["x-api-key"] = script_header["HeyGen API key"]

            ## json body
            post_json = dict()
            post_json["video_inputs"] = []
            clip = dict()
            clip["character"] = dict()
            clip["character"]["type"] = "avatar"
            clip["character"]["avatar_id"] = scene.avatar_video.avatar_id  #script_header["Default Avatar ID"]
            clip["character"]["avatar_style"] = scene.avatar_video.style.value
            clip["character"]["scale"] = scene.avatar_video.scale
            clip["character"]["offset"] = {"x": scene.avatar_video.position[0]-0.5, "y": scene.avatar_video.position[1]-0.5} 
            # hey gen uses offset of of the middle of the canvas for the 
            # middle of the avatar so middle middle is 0.0,0.0, bottom left is -0.25,0.25 etc . 
            # I want to use top-left is 0.0 because I believe that is how ffmpeg does it
            # my (0,0) (top-left) is heygen's -0.5,-0.5. We can tentatively use me-0.5
            if scene.avatar_video.style == avatar_style.CIRCLE:
                clip["character"]["circle_background_color"] = scene.avatar_video.circle_background

            clip["voice"] = dict()
            if scene.audio_file == None:
                clip["voice"]["type"] = "text"
                clip["voice"]["input_text"] = scene.text
                clip["voice"]["voice_id"] = scene.avatar_video.voice_id #script_header["Default Voice ID"]
            else:
                clip["voice"]["type"] = "audio"
                clip["voice"]["audio_asset_id"] = scene.audio_asset_id

            clip["background"] = dict()
            clip["background"]["type"] = "color"
            clip["background"]["value"] = scene.avatar_video.background

            post_json["video_inputs"].append(clip)
            post_json["test"] = True
            post_json["caption"] = True
            post_json["dimension"] = {"width": scene.style.output_dim[0], "height": scene.style.output_dim[1]}

            print(post_json)
            response = requests.post("https://api.heygen.com/v2/video/generate", json = post_json, headers=post_header)
            responses.append(response)

        elif scene.style.style == style_type.SBS or scene.style.style == style_type.FPIP:
            post_header = dict()
            post_header["Content-Type"] = "application/json"
            post_header["x-api-key"] = script_header["HeyGen API key"]

            ## json body
            post_json = dict()
            post_json["video_inputs"] = []
            clip = dict()
            clip["character"] = dict()
            clip["character"]["type"] = "avatar"
            clip["character"]["avatar_id"] = scene.avatar_video.avatar_id #script_header["Default Avatar ID"]
            clip["character"]["avatar_style"] = scene.avatar_video.style.value
            clip["character"]["scale"] = scene.avatar_video.scale
            clip["character"]["offset"] = {"x": scene.avatar_video.position[0]-0.5, "y": scene.avatar_video.position[1]-0.5} 
            # hey gen uses offset of of the middle of the canvas for the 
            # middle of the avatar so middle middle is 0.0,0.0, bottom left is -0.25,0.25 etc . 
            # I want to use top-left is 0.0 because I believe that is how ffmpeg does it
            # my (0,0) (top-left) is heygen's -0.5,-0.5. We can tentatively use me-0.5
            if scene.avatar_video.style == avatar_style.CIRCLE:
                clip["character"]["circle_background_color"] = scene.avatar_video.circle_background

            clip["voice"] = dict()
            if scene.audio_file == None:
                clip["voice"]["type"] = "text"
                clip["voice"]["input_text"] = scene.text
                clip["voice"]["voice_id"] = scene.avatar_video.voice_id #script_header["Default Voice ID"]
            else:
                clip["voice"]["type"] = "audio"
                clip["voice"]["audio_asset_id"] = scene.audio_asset_id

            clip["background"] = dict()
            clip["background"]["type"] = "color"
            clip["background"]["value"] = scene.avatar_video.background

            post_json["video_inputs"].append(clip)
            post_json["test"] = True
            post_json["caption"] = True
            post_json["dimension"] = {"width": scene.style.output_dim[0], "height": scene.style.output_dim[1]}

            print(post_json)
            response = requests.post("https://api.heygen.com/v2/video/generate", json = post_json, headers=post_header)
            responses.append(response)
        
        else: 
            raise Exception("unsupported composition type for now")
    return responses

def parse_upload_response(responses:list[requests.models.Response], script: tuple[dict,list[scene]])->list[scene]:
    count = 0
    script_header, script_body = script
    for response in responses:
        if response.status_code == 200:
            body = json.loads(response.text)
            script_body[count].avatar_video.video_id = body["data"]["video_id"]
        else:
            body = json.loads(response.text)
            body['error']
            print("Error with video number " + str(count))
            print(body['error']['message'])
            if response.status_code == 429:
                raise Exception("You've used up the available requests on this API key in the last 24 hours. Please wait or try a different key.")
            else:
                raise Exception(f"Uknown error ocurred: {body['error']['message']}")
        count = count + 1
    return script

# HELPER FNS
def download_file_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download&confirm=1"

    session = requests.Session()

    print("get session response")
    try: 
        response = session.get(URL, params={"id": file_id}, stream=True, timeout=100)
        token = get_confirm_token(response)

        print("if token")
        if token:
            params = {"id": file_id, "confirm": token}
            response = session.get(URL, params=params, stream=True)

        print("gonna save response content")
        save_response_content(response, destination)
    except requests.exceptions.ReadTimeout:
        download_file_from_google_drive(file_id, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                print("writing chunk")


def get_slides(script:list[scene], dir:str="./")->list[scene]:
    count  = 0
    script_header, script_body = script

    if "pdf" not in script_header:
        for scene in script_body:
            if scene.slide.slide_url != None and scene.slide.slide_url != '':
                url_pieces = re.split('\/', scene.slide.slide_url)
                if url_pieces[2] == 'drive.google.com':
                    file_id = url_pieces[5]
                    print("about to download from google drive")
                    download_file_from_google_drive(file_id, dir+f"slide{count}.jpg")
                    print("just downloaded from google drive")
                    scene.slide.slide_filename = dir+f"slide{count}.jpg"
                    count = count + 1
    #for scene in script_body:
    #    if scene.slide.slide_url != None and scene.slide.slide_url != '':
    #        path, headers = urlretrieve(scene.slide.slide_url, dir+f"slide{count}.jpg") # todo return and decide how to import the file format. don't think this thing cares tho
    #        scene.slide.slide_filename = path
    #        count = count + 1
    return script

def get_avatar_clip(scene:scene, apikey:str, count:int, wait:int, dir:str="./"):
    time.sleep(wait)
    post_header = dict()
    post_header['Content-Type'] = "application/json"
    post_header["x-api-key"] = apikey #script_header["HeyGen API key"]
    response = requests.get("https://api.heygen.com/v1/video_status.get?video_id="+scene.avatar_video.video_id, headers=post_header)
    if response.status_code == 200:
        body = json.loads(response.text)
        if body["data"]["status"] == "completed":

            # get the url to the video and download it
            scene.avatar_video.url = body["data"]["video_url"]
            path, headers = urlretrieve(scene.avatar_video.url, dir+f"avatar{count}.mp4")
            scene.avatar_video.filename = path

            # get the url to the caption and download it
            scene.caption.caption_url = body["data"]["caption_url"] if body["data"]["caption_url"] != None else None
            if scene.caption.caption_url != None:
                path, headers = urlretrieve(scene.caption.caption_url, dir+f"caption{count}.ass")
                scene.caption.caption_filename = path
            return scene
        else:
            print("trying again with video " + str(scene.number) + " waiting " + str(wait*2))
            return get_avatar_clip(scene, apikey, count, wait*2, dir)
    pass


def get_avatar_clips(script:tuple[dict,list[scene]], dir:str="./")->list[scene]:
    count = 0
    script_header, script_body = script
    apikey = script_header["HeyGen API key"]
    for scene in script_body:
        script_body[count] = get_avatar_clip(scene, apikey, count, 50, dir)
        count = count + 1
    return script