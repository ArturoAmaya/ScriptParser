from scriptparser import scene, caption, avatar_video, background, slide, slide_source, style, style_type, transition_type, transition_in, avatar_style
import re

def parse_composition(command:str, default: dict = None):
    composition = dict()
    composition["avatar"] = dict()
    if ',' in command: 
        params = command[1:-1].split(',') # [1:-1] get rid of the outside []
    else:
        params = [command[1:-1]]
    for param in params:
        if ':' in param:
            v = param.split(":")[1].strip() # get value
            k = param.split(":")[0].strip() # get key
            match k:
                case 'type':
                    # setting the style type
                    composition["type"] = style_type(v)
                #case 'position':
                    # positions will be ;-separated for now
                    #p = v[1:-1].split(";") for when ptuples have ()
                #    p = v[1:-1].split(";")
                #    composition["avatar"]["position"] = (float(p[0]), float(p[1]))
                #case 'scale':
                #    composition["avatar"]["scale"] = float(v)
                #case 'style':
                #    composition["avatar"]["style"] = avatar_style(v)
                case 'outout_dim':
                    d = v[1:-1].split(";")
                    composition["output_dim"] = (float(d[0]), float(d[1]))
                #case 'background':
                #    composition["avatar"]["background"] = v
                #    composition["true_background"] = v
            
    # pass in defaults
    if not "type" in composition:
        composition["type"] = default["type"] if default!=None else style_type.PIP
        composition["avatar_position"] = composition["avatar_position"] if "avatar_position" in composition else default["avatar_position"] if default!=None else (0,0)
        composition["avatar_scale"] = composition["avatar_scale"] if "avatar_scale" in composition else default["avatar_scale"] if default!=None else 1.0
        composition["output_dim"] = composition["output_dim"] if "output_dim" in composition else default["output_dim"] if default!=None else (1280,720)
        composition["slides_scale"] = composition["slides_scale"] if "slides_scale" in composition else default["slides_scale"] if default!=None else None
        composition["slides_position"] = composition["slides_position"] if "slides_position" in composition else default["slides_position"] if default!=None else None
        composition["true_background"] = composition["true_background"] if "true_background" in composition else default["true_background"] if default!=None else "#FFFFFF"
        composition["avatar_width"] = composition["avatar_width"] if "avatar_width" in composition else default["avatar_width"] if default!=None else None
        composition["avatar_side"] = composition["avatar_side"] if "avatar_side" in composition else default["avatar_side"] if default!=None else None
        composition["slide_side"] = composition["slide_side"] if "slide_side" in composition else default["slide_side"] if default!=None else None

        # then do the avatar defaults for hey gen PIP
        composition["avatar"]["position"] = composition["avatar"]["position"] if "position" in composition["avatar"] else default["avatar"]["position"] if default!=None else (0.75, 0.75)
        composition["avatar"]["style"] = composition["avatar"]["style"] if "style" in composition["avatar"] else default["avatar"]["style"] if default!=None else "normal"
        composition["avatar"]["background"] = composition["avatar"]["background"] if "background" in composition["avatar"] else default["avatar"]["background"] if default!=None else "#FFFFFF"
        composition["avatar"]["scale"] = composition["avatar"]["scale"] if "scale" in composition["avatar"] else default["avatar"]["scale"] if default != None else 0.5
    else:
        match composition["type"]:
            case style_type.PIP:
                composition["avatar_position"] = composition["avatar_position"] if "avatar_position" in composition else default["avatar_position"] if default!=None else (0,0)
                composition["avatar_scale"] = composition["avatar_scale"] if "avatar_scale" in composition else default["avatar_scale"] if default!=None else 1.0
                composition["output_dim"] = composition["output_dim"] if "output_dim" in composition else default["output_dim"] if default!=None else (1280,720)
                composition["slides_scale"] = composition["slides_scale"] if "slides_scale" in composition else default["slides_scale"] if default!=None else None
                composition["slides_position"] = composition["slides_position"] if "slides_position" in composition else default["slides_position"] if default!=None else None
                composition["true_background"] = composition["true_background"] if "true_background" in composition else default["true_background"] if default!=None else "#FFFFFF"
                composition["avatar_width"] = composition["avatar_width"] if "avatar_width" in composition else default["avatar_width"] if default!=None else None
                composition["avatar_side"] = composition["avatar_side"] if "avatar_side" in composition else default["avatar_side"] if default!=None else None
                composition["slide_side"] = composition["slide_side"] if "slide_side" in composition else default["slide_side"] if default!=None else None

                # then do the avatar defaults for hey gen PIP
                composition["avatar"]["position"] = composition["avatar"]["position"] if "position" in composition["avatar"] else default["avatar"]["position"] if default!=None else (0.75, 0.75)
                composition["avatar"]["style"] = composition["avatar"]["style"] if "style" in composition["avatar"] else default["avatar"]["style"] if default!=None else "normal"
                composition["avatar"]["background"] = composition["avatar"]["background"] if "background" in composition["avatar"] else default["avatar"]["background"] if default!=None else "#FFFFFF"
                composition["avatar"]["scale"] = composition["avatar"]["scale"] if "scale" in composition["avatar"] else default["avatar"]["scale"] if default != None else 0.5

            case style_type.AVATAR:
                composition["avatar_position"] = composition["avatar_position"] if "avatar_position" in composition else default["avatar_position"] if default!=None else (0,0)
                composition["avatar_scale"] = composition["avatar_scale"] if "avatar_scale" in composition else default["avatar_scale"] if default!=None else 1.0
                composition["output_dim"] = composition["output_dim"] if "output_dim" in composition else default["output_dim"] if default!=None else (1280,720)
                composition["slides_scale"] = composition["slides_scale"] if "slides_scale" in composition else default["slides_scale"] if default!=None else None
                composition["slides_position"] = composition["slides_position"] if "slides_position" in composition else default["slides_position"] if default!=None else None
                composition["true_background"] = composition["true_background"] if "true_background" in composition else default["true_background"] if default!=None else "#FFFFFF"
                composition["avatar_width"] = composition["avatar_width"] if "avatar_width" in composition else default["avatar_width"] if default!=None else None
                composition["avatar_side"] = composition["avatar_side"] if "avatar_side" in composition else default["avatar_side"] if default!=None else None
                composition["slide_side"] = composition["slide_side"] if "slide_side" in composition else default["slide_side"] if default!=None else None

                # then do the avatar defaults for hey gen PIP
                composition["avatar"]["position"] = composition["avatar"]["position"] if "position" in composition["avatar"] else default["avatar"]["position"] if default!=None else (0.5, 0.5)
                composition["avatar"]["style"] = composition["avatar"]["style"] if "style" in composition["avatar"] else default["avatar"]["style"] if default!=None else "normal"
                composition["avatar"]["background"] = composition["avatar"]["background"] if "background" in composition["avatar"] else default["avatar"]["background"] if default!=None else "#FFFFFF"
                composition["avatar"]["scale"] = composition["avatar"]["scale"] if "scale" in composition["avatar"] else default["avatar"]["scale"] if default != None else 1.0
            case default:
                raise Exception("not pip wyd")
    
    return composition

def parse_avatar(command:str, default: dict=None):
    avatar = dict()
    if ',' in command:
        params = command[1:-1].split(',')
    else:
        params = [command[1:-1]]
    for param in params:
        if ':' in param:
            v = param.split(":")[1].strip() 
            k = param.split(":")[0].strip()
            match k:
                case 'id':
                    avatar["avatar_id"] = v
                case 'avatar_id':
                    avatar['avatar_id'] = v
                case 'voice_id':
                    avatar["voice_id"] = v
                case 'position':
                    p = v.split(";")
                    avatar["position"] = (float(p[0]),float(p[1]))
                case 'scale':
                    avatar['scale'] = float(v)
                case 'style':
                    avatar["style"] = avatar_style(v)
                case 'cbc': # circlebackground color
                    avatar["circle_background"] = v
                case 'circle_background':
                    avatar["circle_bakground"] = v
                case 'bc': # background color
                    avatar["background"] = v
                case "background":
                    avatar["background"] = v
    
    avatar["avatar_id"] = avatar["avatar_id"] if "avatar_id" in avatar else default["avatar_id"] if default!=None and "avatar_id" in default else "Luke_public_3_20240306"
    avatar["voice_id"] = avatar["voice_id"] if "voice_id" in avatar else default["voice_id"] if default!=None and "voice_id" in default else "5dddee02307b4f49a17c123c120a60ca"
    avatar["position"] = avatar["position"] if "position" in avatar else default["position"] if default!=None and "position" in default else (0.5,0.5)
    avatar["scale"] = avatar["scale"] if "scale" in avatar else default["scale"] if default!=None and "scale" in default else 1.0
    avatar["style"] = avatar["style"] if "style" in avatar else default["style"] if default!=None and "style" in default else style_type("normal")
    avatar["circle_background"] = avatar["circle_background"] if "circle_background" in avatar else default["circle_background"] if default!=None and "circle_background" in default else "#FFFFFF"
    avatar["background"] = avatar["background"] if "background" in avatar else default["background"] if default!=None and "background" in default else "#FFFFFF"

    return avatar
    
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
        transition["t_type"] = default["t_type"] if default != None else transition_type.FADE
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
                #case "Creatomate API key":
                #    true_header["Creatomate API key"] = line_split[1].strip()
                #case "Default Avatar ID":
                #    true_header["Default Avatar ID"] = line_split[1].strip()
                #case "Default Voice ID":
                #    true_header["Default Voice ID"] = line_split[1].strip()
                case "Slides":
                    slides = True
                    true_header["Slides"] = []
                case "Default Composition":
                    composition_command = re.compile('(\[.*?\])')
                    true_header["Default Composition"] = parse_composition(composition_command.search(line).group())
                case "Default Transition":
                    transition_command = re.compile('({.*?})')
                    true_header["Default Transition"] = parse_transition(transition_command.search(line).group())
                case "Default Avatar":
                    avatar_command = re.compile('(\(.*?\))')
                    true_header["Default Avatar"] = parse_avatar(avatar_command.search(line).group())
        else:
            true_header["Slides"].append(line.strip())

    # TODO populate default composition and transition if needed
    return true_header

def parse_script(script:list[tuple[scene,bool]], header:dict):
    true_script = []
    count = 0
    slide_count = 0
    for (line,midline) in script:
        # make a new scene
        s = scene()
        s.midline_cut = midline
        # assign the number
        s.number = count

        # get the composition command and parse it
        comp_command = re.compile('(\[.*?\])').search(line) # returns first instance with a span that is [start,end)
        if comp_command == None:
            comp = parse_composition(re.compile('(\[.*?\])').search("[]"+line).group(), header["Default Composition"])
        else:
            comp = parse_composition(re.compile('(\[.*?\])').search(line).group(), header["Default Composition"])
        
        # get the avatar command and parse it
        avatar_command = re.compile('(\(.*?\))').search(line)
        if avatar_command == None:
            avatar_dict = parse_avatar(re.compile('(\(.*?\))').search("()"+line).group(), header["Default Avatar"])
        else:
            avatar_dict = parse_avatar(re.compile('(\(.*?\))').search(line).group(), header["Default Avatar"])

        s.avatar_video = avatar_video.from_dict(avatar_dict)
        s.style = style.from_dict(comp)
        #s.style.style = style_type.PIP
        #s.style.avatar_scale = 0.5
        #s.style.slides_scale = 1.0
        #s.style.avatar_position = (0.75,0.75)
        #s.style.slides_position = (0.0,0.0)
        #style(style_type.PIP, 0.5, 1.0, (0.75,0.75), (0.0,0.0))

        # transition info
        if (count != 0):
            # grab the {} command
            s.transition_in = transition_in.from_dict(parse_transition(re.compile('({.*?})').search(line).group() if re.compile('({.*?})').search(line) !=None else "", header["Default Transition"]))
        
        # assign the text, the background type, the slides url, the style
        

        # if the next clip is a midline cut give this one the combined text
        if script.index((line,midline))+1<len(script) and script[script.index((line,midline))+1][1] == True:
            lookahead = script.index((line,midline))+1
            s.text = re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', line)))
            while lookahead < len(script) and script[lookahead][1]:
                s.text = s.text + re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', script[lookahead][0])))
                lookahead = lookahead + 1
            #s.text = re.sub('({.*?})', '', re.sub('(\[.*?\])','', line)) + re.sub('({.*?})', '', re.sub('(\[.*?\])','', script[script.index((line,midline))+1][0]))
            if s.midline_cut == True: # TODO simplify this condition block
                lookback = script.index((line,midline))
                #s.text = re.sub('({.*?})', '', re.sub('(\[.*?\])','', line))
                while script[lookback][1]:
                    lookback = lookback -1
                    s.text = re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', script[lookback][0]))) + s.text
                #s.text = re.sub('({.*?})', '', re.sub('(\[.*?\])','', script[script.index((line,midline))-1][0])) + re.sub('({.*?})', '', re.sub('(\[.*?\])','', line))
                s.midline_text = re.sub('(\(.*?\))','', re.sub('({.*?})', '', re.sub('(\[.*?\])','', line)))
        elif s.midline_cut == True:
            # if this one is midline get the previous combined text
            lookback = script.index((line,midline))
            s.text = re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', line)))
            while script[lookback][1]:
                lookback = lookback -1
                s.text = re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', script[lookback][0]))) + s.text
            #s.text = re.sub('({.*?})', '', re.sub('(\[.*?\])','', script[script.index((line,midline))-1][0])) + re.sub('({.*?})', '', re.sub('(\[.*?\])','', line))
            s.midline_text = re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', line)))
        else:
            s.text = re.sub('(\(.*?\))','',re.sub('({.*?})', '', re.sub('(\[.*?\])','', line))) # line.replace('\\\\', '') # TODO return to this when we add in mid-clip cuts
        
        if s.style.style == style_type.PIP:
            s.slide.slide_source_type = slide_source.URL
            s.slide.slide_url = header['Slides'][slide_count] if slide_count < len(header["Slides"]) else header["Slides"][-1]
            slide_count = slide_count + 1
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
                # this currently finds {} commands and splits the line based on that, then pairs each {} with it's text line
                # there are some exceptions/issues
                # currently []{} commands get screwed, only {}[] commands work
                # [] commands mid-line are ignored.
                # i think this is the one: '((?: *[\[{].*?[\]}]){1,2}(?:[^\[{\n])*)'
                # https://regex101.com/r/geWa9s/1
                # proposed new flow would be:
                # chop up the line based on the appearance of  *[\[{].*?[\]}], i.e. either {} or []
                # remove all the ''s that that makes


                # adding () commands we do ((?: *[\[{\(].*?[\]}\)]){1,3}(?:[^\[{\(\n])*) per https://regex101.com/r/RY7CPb/1
                if(str(line.strip())!=''):
                    command_pairs = [s for s in re.split(r'((?: *[\[{\(].*?[\]}\)]){1,3}(?:[^\[{\(\n])*)', line) if s!='' and s!='\n'] # this produces all the command-script pairs
                    # get the command pairs then decide what to do with them
                    for pair in command_pairs:

                        # if there's a good []{}()/{}[]() group in any order put that in the script
                        if re.compile('( *[\[{\()].*?[\])]){3}').search(pair)!=None:
                            script.append((pair, False))

                        # a midline cut is a () or a [] (or both) that are not paired with a {} and is not at the beginning of the line
                        elif (re.compile('( *\[.*?\])').search(pair)!=None or re.compile('( *\(.*?\))').search(pair)!=None) \
                            and re.compile('( *{.*?})').search(pair)==None and \
                            pair != command_pairs[0]:
                        # if there's only a [] and it's midline pair it with a concat. True indicates this is a midline cut and we need to do something about it
                            script.append(("{concat}"+pair, True))
                        elif re.compile('( *{.*?})').search(pair):
                        # if there's only a {} just put it in the script
                            script.append((pair,False))
                        else: 
                            # this is now for defaults and for []-only commands that are at the beginning of a line
                            #print("what is" + pair+"? I will treat it as a default default")
                            script.append((pair,False))
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
        s.midline_cut = item["midline_cut"]
        s.midline_text = item["midline_text"]

        scenes.append(s)
    return (script["header"], scenes)