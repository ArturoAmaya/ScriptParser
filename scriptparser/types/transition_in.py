from dataclasses import dataclass
from enum import Enum

class transition(Enum):
    FADE = "fade"


@dataclass
class transition_in:
    t_type: transition
    duration: float

    def __init__(self):
        self.t_type = None
        self.duration = 0.0