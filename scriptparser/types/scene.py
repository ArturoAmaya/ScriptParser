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
    audio_file: str # This is so that we can make the avatar lipsync
    audio_asset_id: str
    clip: object
    caption: cap
    # stuff to keep track of midline edits
    midline_cut: bool
    midline_text: str

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
        self.midline_cut = None
        self.midline_text = None
        self.audio_file = None
        self.audio_asset_id = None

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
        s.midline_cut = data["midline_cut"]
        s.midline_text = data["midline_text"]
        s.audio_file = data["audio_file"]
        s.audio_asset_id = data["audio_asset_id"]

 
