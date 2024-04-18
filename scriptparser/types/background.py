from dataclasses import dataclass
from enum import Enum

class background_source_type(Enum):
    URL = "url"
    COMMAND = "command"

@dataclass
class background:
    background_source_type: background_source_type
    background_url: str | None  
    background_command: str | None
