from scriptparser import scene, slide_source, style, style_type, transition, transition_in

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
                case "Avatar ID":
                    true_header["Avatar ID"] = line_split[1].strip()
                case "Voice ID":
                    true_header["Voice ID"] = line_split[1].strip()
                case "Slides":
                    slides = True
                    true_header["Slides"] = []
        else:
            true_header["Slides"].append(line.strip())
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
        s.text = line.replace('\\\\', '')
        s.slide.slide_source_type = slide_source.URL
        s.slide.slide_url = header['Slides'][count]

        # default here is pip so no background to be set
        # assign style per default for v0.01 using ffmpeg notation
        s.style.style = style_type.PIP
        s.style.avatar_scale = 0.5
        s.style.slides_scale = 1.0
        s.style.avatar_position = (0.75,0.75)
        s.style.slides_position = (0.0,0.0)
        #style(style_type.PIP, 0.5, 1.0, (0.75,0.75), (0.0,0.0))

        # transition infor
        if (count != 0):
            s.transition_in.t_type = transition.FADE
            s.transition_in.duration = 1.0
        
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
                if (str(line.strip())!=''):
                    script.append(str(line.strip()))
        header = parse_header(header)
        script = parse_script(script, header)
        return (header, script)
    except:
        return False