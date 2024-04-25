from dataclasses import dataclass, asdict
from enum import Enum

class style_type(Enum):
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