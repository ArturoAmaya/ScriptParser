from dataclasses import dataclass
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
    avatar_position: tuple[float,float]
    slides_position: tuple[float,float]