from dataclasses import dataclass

@dataclass
class caption:
    caption_url: str
    caption_filename: str
    parsed_caption: list[tuple[float, float, str]]
