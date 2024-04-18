from dataclasses import dataclass

@dataclass
class caption:
    caption_url: str
    caption_filename: str
    parsed_caption: list[tuple[float, float, str]]

    def __init__(self):
        self.caption_url = None
        self.caption_filename = None
        self.parsed_caption = None