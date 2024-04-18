from dataclasses import dataclass
from enum import Enum

class transition_type(Enum):
    FADE = "fade"


@dataclass
class transition_in:
    t_type: transition_type
    slide_url: str
    slide_img: object