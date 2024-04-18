from dataclasses import dataclass
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
