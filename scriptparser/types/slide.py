from dataclasses import dataclass
from enum import Enum

class slide_source_type(Enum):
    URL = "url"

@dataclass
class slide:
    slide_source_type: slide_source_type
    slide_url: str | None
    slide_img: any
