from scriptparser import scene

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

def parse_script(script:list[str]):
    true_script = []
    for line in script:
        snippets = line.split(r"\\")
        for snippet in snippets:
            if snippet != '':
                true_script.append(snippet)
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
                script.append(str(line.strip()))
        header = parse_header(header)
        script = parse_script(script)
        return (header, script)
    except:
        return False