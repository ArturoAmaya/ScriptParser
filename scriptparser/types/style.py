from dataclasses import dataclass, asdict
from enum import Enum

class style_type(str,Enum):
    PIP = "pip"
    FPIP = "fpip" #ffmpeg pip
    AVATAR = "avatar-only"
    SBS = "side-by-side"
    VOICEOVER = "voiceover"
    #SLIDE = "slide-only"

class av_style(str, Enum):
    NORMAL = "normal"
    CLOSEUP = "closeUp"
    CIRCLE = "circle"

class side(str,Enum):
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"

@dataclass
class style:
    style: style_type # default type of scenes
    avatar_position: tuple[float,float] # where the top left point of the avatar CLIP should be wrt to the canvas. 0-1 as a percentage of size of output dim
    avatar_scale: float # size of the avatar clip in terms of its original size
    output_dim: tuple[float,float]
    slides_scale: float # how big the slides should be wrt to their original size
    slides_position: tuple[float,float] # same as above
    true_background: str # if there is a scene background what is it
    avatar_width: float # TODO
    avatar_side: side # TODO
    slide_side: side # TODO


    def __init__(self):
        self.style = None
        self.avatar_position = None
        self.avatar_scale = None
        self.output_dim = None
        self.slides_scale = None
        self.slides_position = None
        self.true_background = None
        self.avatar_width = None
        self.avatar_side = None
        self.slide_side = None
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c = cls()
        c.style = style_type(data["style"]) if "style" in data else data["type"]
        c.avatar_position = (float(data["avatar_position"][0]), float(data["avatar_position"][1])) if "avatar_position" in data else (0,0)
        c.avatar_scale = float(data["avatar_scale"]) if "avatar_scale" in data else 0.4
        c.output_dim = data["output_dim"]
        c.true_background = data["true_background_color"] if "true_background_color" in data else data["true_background"] if "true_background" in data else "white"
        c.avatar_side = side(data["avatar_side"]) if "avatar_side" in data else "right"
        #c.slides_scale = data["slides_scale"]
        #c.slides_position = (data["slides_position"][0], data["slides_position"][1]) if data["slides_position"] != None else None
        #c.true_background = data["true_background"]
        #c.avatar_width = data["avatar_width"]
        #c.avatar_side = side(data["avatar_side"]) if data["avatar_side"] != None else None
        #c.slide_side = side(data["slide_side"]) if data["slide_side"] != None else None
        return c