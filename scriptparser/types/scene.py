from dataclasses import dataclass, asdict
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

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        s = cls()
        s.number = data["number"]
        s.style = slay.from_dict(data["style"])
        s.slide = img.from_dict(data["slide"])
        s.background = bkgnd.from_dict(data["background"])
        s.transition_in = in_.from_dict(data["transition_in"])
        s.avatar_video = vid.from_dict(data["avatar_video"])
        s.text = data["text"]
        s.clip = None # really don't know what happnes if you save this while it has a value like a video
        s.caption = cap.from_dict(data["caption"])
 
