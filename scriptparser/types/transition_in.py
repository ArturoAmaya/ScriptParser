from dataclasses import dataclass
from enum import Enum

class transition(Enum):
    FADE = "fade"


@dataclass
class transition_in:
    t_type: transition
    slide_url: str
    slide_img: object

    def __init__(self):
        self.t_type = None
        self.slide_url = None
        self.slide_img = None