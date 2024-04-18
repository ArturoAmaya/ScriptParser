from dataclasses import dataclass
from .avatar_video import avatar_video
from .background import background
from .caption import caption
from .slide import slide
from .style import style
from .transition_in import transition_in

@dataclass
class scene:
    number: int
    style: style
    slide: slide
    background: background
    transition_in: transition_in
    avatar_video: avatar_video
    text: str
    clip: object
    caption: caption

