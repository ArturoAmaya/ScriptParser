from dataclasses import dataclass
from .avatar_video import avatar_video as vid
from .background import background as bkgnd
from .caption import caption as cap
from .slide import slide as img
from .style import style as slay
from .transition_in import transition_in as in_

@dataclass
class scene:
    number: int
    style: slay
    slide: img
    background: bkgnd
    transition_in: in_
    avatar_video: vid
    text: str
    clip: object
    caption: cap

    def __init__(self):
        self.number = None
        self.style = slay()
        self.slide = img()
        self.background = bkgnd()
        self.transition_in = in_()
        self.avatar_video = vid()
        self.text = None
        self.clip = None
        self.caption = cap()

