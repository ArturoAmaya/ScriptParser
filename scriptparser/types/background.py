from dataclasses import dataclass, asdict
from enum import Enum

class background_source(Enum):
    URL = "url"
    COMMAND = "command"

@dataclass
class background:
    background_source_type: background_source
    background_url: str | None  
    background_command: str | None

    def __init__(self):
        self.background_source_type = None
        self.background_url = None
        self.background_command = None

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        #c = cls()
        #c.background_source_type = background_source(data["background_source_type"])
        #c.background_url = data["background_url"]
        #c.background_command = data["background_command"]
        pass
