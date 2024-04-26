from dataclasses import dataclass, asdict
from enum import Enum

class style_type(str,Enum):
    PIP = "pip"
    AVATAR = "avatar-only"
    SBS = "side-by-side"
    SLIDE = "slide-only"

@dataclass
class style:
    style: style_type
    avatar_scale: float
    slides_scale: float
    avatar_position: tuple[float,float] # where the top left point of the avatar should be wrt to the canvas. 0-1 as a percentage of size
    slides_position: tuple[float,float] # same as above

    def __init__(self):
        self.style = None
        self.avatar_scale = None
        self.slides_scale = None
        self.avatar_position = None
        self.slides_position = None
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c = cls()
        c.style = style_type(data["style"])
        c.avatar_scale = data["avatar_scale"]
        c.slides_scale = data["slides_scale"]
        c.avatar_position= (data["avatar_position"][0], data["avatar_position"][1])
        c.slides_position = (data["slides_position"][0], data["slides_position"][1])
        return c