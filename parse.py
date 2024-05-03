from scriptparser import scene, caption, avatar_video, background, slide, slide_source, style, style_type, transition_type, transition_in
import re

def parse_composition(str):
    # for now all the compositions are default so return default
    pass
def parse_transition(command:str, default: dict=None):
    transition = dict()
    if ',' in command:
        params = command[1:-1].split(',')
    else:
        params = [command[1:-1]]
    for param in params:
        if ':' in param:
            p = param.split(":")[1].strip()
            if param.split(":")[0].strip() == "duration":
                transition["duration"] = float(p)
            elif param.split(":")[0].strip() == "type":
                transition["t_type"] = transition_type(p)
            else:
                print("something went wrong parsing the default transition")
                transition["duration"] = default["duration"] if default != None else 1.0
                transition["t_type"] = default["t_type"] if default != None else transition_type.FADE
                break
        else:
            p = param.strip()
            if p == '':
                transition["duration"] = default["duration"] if default != None else 1.0
                transition["t_type"] = default["t_type"] if default != None else transition_type.FADE
            else:
                # with no keys just try to match
                try:
                    d = float(p)
                    transition["duration"] = d
                except:
                    transition["t_type"] = transition_type(p)
        
    if "duration" not in transition:
        transition["duration"] = default["duration"] if default != None else 1.0
    if "t_type" not in transition:
        transition["t_type"] = default["duration"] if default != None else transition_type.FADE
    return transition

def parse_header(header:list[str]):
    true_header = dict()
    slides = False
    for line in header:
        line_split = line.split(':')
        if not slides:
            match line_split[0].strip():
                case "Name":
                    true_header["Name"] = line_split[1].strip()
                case "Lecture Name":
                    true_header["Lecture Name"] = line_split[1].strip()
                case "HeyGen API key":
                    true_header["HeyGen API key"] = line_split[1].strip()
                case "Creatomate API key":
                    true_header["Creatomate API key"] = line_split[1].strip()
                case "Default Avatar ID":
                    true_header["Default Avatar ID"] = line_split[1].strip()
                case "Default Voice ID":
                    true_header["Default Voice ID"] = line_split[1].strip()
                case "Slides":
                    slides = True
                    true_header["Slides"] = []
                case "Default Composition":
                    true_header["Default Composition"] = parse_composition(line_split[1].strip())
                case "Default Transition":
                    transition_command = re.compile('({.*?})')
                    true_header["Default Transition"] = parse_transition(transition_command.search(line).group())
        else:
            true_header["Slides"].append(line.strip())

    # TODO populate default composition and transition if needed
    return true_header

def parse_script(script:list[scene], header:dict):
    true_script = []
    count = 0
    for line in script:
        # make a new scene
        s = scene()

        # assign the number
        s.number = count
        

        # assign the text, the background type, the slides url, the style
        s.text = re.sub('({.*?})', '', line) # line.replace('\\\\', '') # TODO return to this when we add in mid-clip cuts
        s.slide.slide_source_type = slide_source.URL
        s.slide.slide_url = header['Slides'][count] if count < len(header["Slides"]) else header["Slides"][-1]

        # default here is pip so no background to be set
        # assign style per default for v0.01 using ffmpeg notation
        # TODO update to read default composition
        s.style.style = style_type.PIP
        s.style.avatar_scale = 0.5
        s.style.slides_scale = 1.0
        s.style.avatar_position = (0.75,0.75)
        s.style.slides_position = (0.0,0.0)
        #style(style_type.PIP, 0.5, 1.0, (0.75,0.75), (0.0,0.0))

        # transition infor
        if (count != 0):
            # grab the {} command
            s.transition_in = transition_in.from_dict(parse_transition(re.compile('({.*?})').search(line).group(), header["Default Transition"]))
        
        # at this point, the only things in scene with no value are
        # avatar_video - id, metadata, url and video depend on uploading the clips
        # this is PIP only so no background needed
        # caption - same reason as avatar_video
        # clip - video hasn't been made yet
        # slide img - havent gotten the slides yet
        # the first slide should have no transition in information

        # increment the count
        count = count + 1

        # add the scene to the scene list
        true_script.append(s)
    return true_script

def parse_from_file(filepath: str):
    try:
        # read the files
        file = open(filepath, 'r')
        header = []
        script = []
        lines = file.readlines()
        head = True
        for line in lines:
            if head and line.strip() != "--":
                header.append(line.strip())
            elif line.strip() == "--":
                head = False
            else:
                # note that new line is any new line, and repeated newlines are treated the same as only one new line
                if (str(line.strip())!=''):
                    extra_lines = re.split(r'({.*?})', line.strip())
                    
                    if extra_lines[0] == '':
                        extra_lines.pop(0)
                    # if the array starts with a command, go two by two, combining strings and adding them to true script
                    if extra_lines[0][0] == '{' and extra_lines[0][-1] == '}':
                        while len(extra_lines) > 1:
                            script.append(str(extra_lines[0].strip()) + str(extra_lines[1].strip()))
                            extra_lines.pop(0)
                            extra_lines.pop(0)
                    else:
                        # otherwise add the first in with an empty command and then continue as before
                        script.append('{}' + str(extra_lines[0].strip()))
                        extra_lines.pop(0)
                        while len(extra_lines) > 1:
                            script.append(str(extra_lines[0].strip()) + str(extra_lines[1].strip()))
                            extra_lines.pop(0)
                            extra_lines.pop(0)
        header = parse_header(header)
        script = parse_script(script, header)
        return (header, script)
    except:
        return False
    

def restore_intermediate(script: dict)->tuple[dict, list[scene]]:
    scenes = []
    for item in script["body"]:
        s = scene()

        s.number = item["number"]
        s.style = style.from_dict(item["style"])
        s.slide = slide.from_dict(item["slide"])
        s.background = background.from_dict(item["background"]) # NO BACKGROUND INFO YET
        s.transition_in = transition_in.from_dict(item["transition_in"])
        s.avatar_video = avatar_video.from_dict(item["avatar_video"])
        s.text = item["text"]
        s.clip = None
        s.caption = caption.from_dict(item["caption"])

        scenes.append(s)
    return (script["header"], scenes)