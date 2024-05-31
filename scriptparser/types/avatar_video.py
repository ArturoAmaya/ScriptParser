from dataclasses import dataclass, asdict
from enum import Enum

class avatar_style(str,Enum):
    NORMAL = "normal"
    CLOSEUP = "closeUp"
    CIRCLE = "circle"

@dataclass
class avatar_video:
    avatar_id: str # avatar id
    voice_id:str
    video_id:str # this is the video id in the response payload
    url: str
    video: object
    metadata: object
    filename: str

    # this information is sent to heygen and used to compose the clip
    # scene has similar values that dictate where the clip made by heygen goes
    position: tuple[float,float] # # where the top left point of the avatar should be wrt to the heygen clip. 0-1 as a percentage of size
    style: avatar_style
    circle_background: str
    background: str
    scale: float 


    def __init__(self):
        self.avatar_id = None
        self.voice_id=None
        self.video_id=None
        self.url = None
        self.video = None
        self.metadata = None
        self.filename = None
        
        self.position = None
        self.style = None
        self.background = None
        self.scale = None
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c =cls()
        c.avatar_id = data["avatar_id"] if "avatar_id" in data else None
        c.voice_id = data["voice_id"] if "voice_id" in data else None
        c.video_id = data["video_id"] if "video_id" in data else None
        c.url = data["url"] if "url" in data else None
        c.video = data["video"] if "video" in data else None
        c.metadata = data["metadata"] if "metadata" in data else None
        c.filename = data["filename"] if "filename" in data else None

        c.position = (data["position"][0], data["position"][1]) if "position" in data else None
        c.style = avatar_style(data["style"]) if "style" in data else None
        c.circle_background = data["circle_background"] if "circle_background" in data else None
        c.background = data["background"] if "background" in data else None
        c.scale = data["scale"] if "scale" in data else None
        return c