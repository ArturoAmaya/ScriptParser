from dataclasses import dataclass, asdict

@dataclass
class caption:
    caption_url: str
    caption_filename: str
    parsed_caption: list[tuple[float, float, str]]

    def __init__(self):
        self.caption_url = None
        self.caption_filename = None
        self.parsed_caption = None

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls,data):
        c = cls()
        c.caption_url = data["caption_url"]
        c.caption_filename = data["caption_filename"]
        c.parsed_caption = data["parsed_caption"]
        #
        return c