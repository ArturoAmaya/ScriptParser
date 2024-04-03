import requests
# cut up a script and put it into the format of a V2 HeyGen video

def upload_script(script: tuple[dict, list]):
    # unpack the script
    (script_header, script_body) = script
    # compose the JSON first
    ## header
    post_header = dict()
    post_header["Content-Type"] = "application/json"
    post_header["x-api-key"] = script_header["HeyGen API key"]

    ## json body
    post_json = dict()
    post_json["video inputs"] = []
    for line in script_body:
        clip = dict()
        clip["character"] = dict()
        clip["character"]["type"] = "avatar"
        clip["character"]["avatar_id"] = script_header["Avatar ID"]
        clip["character"]["avatar_style"] = "normal"
        clip["character"]["scale"] = 0.5
        clip["character"]["offset"] = {"x": 0.25, "y": 0.25}

        clip["voice"] = dict()
        clip["voice"]["type"] = "text"
        clip["input_text"] = line
        clip["voice_id"] = script_header["Voice ID"]

        clip["background"] = dict()
        clip["background"]["type"] = "image"
        clip["background"]["url"] = script_header["Slides"][script_body.index(line)] if script_body.index(line) < len(script_header["Slides"]) else script_header["Slides"][-1]

        post_json["video inputs"].append(clip)
    post_json["test"] = True
    post_json["caption"] = True
    post_json["dimension"] = {"width": 1280, "height": 720}

    response = requests.post("https://api.heygen.com/v2/video/generate", json = post_json, headers=post_header)
    return response