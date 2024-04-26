from dataclasses import dataclass, asdict
from enum import Enum

class transition_type(str, Enum):
    FADE = "fade"


@dataclass
class transition_in:
    t_type: transition_type
    duration: float

    def __init__(self):
        self.t_type = None
        self.duration = 0.0

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c = cls()
        c.t_type = transition_type(data["t_type"]) if data["t_type"] != None else None
        c.duration = data["duration"]
        return c