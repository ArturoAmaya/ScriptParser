from dataclasses import dataclass
from enum import Enum

class slide_source(Enum):
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