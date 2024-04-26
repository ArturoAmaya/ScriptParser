from dataclasses import dataclass, asdict
from enum import Enum

class slide_source(str, Enum):
    URL = "url"

@dataclass
class slide:
    slide_source_type: slide_source
    slide_url: str | None
    slide_img: object
    slide_filename: str

    def __init__(self):
        self.slide_source_type = None
        self.slide_url = None
        self.slide_img = None
        self.slide_filename = None
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c = cls()
        c.slide_source_type = slide_source(data["slide_source_type"])
        c.slide_url = data["slide_url"]
        c.slide_img = data["slide_img"]
        c.slide_filename = data["slide_filename"]
        return c