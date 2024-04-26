from dataclasses import dataclass, asdict

@dataclass
class avatar_video:
    id: str
    url: str
    video: object
    metadata: object
    filename: str

    def __init__(self):
        self.id = None
        self.url = None
        self.video = None
        self.metadata = None
        self.filename = None
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c =cls()
        c.id = data["id"]
        c.url = data["url"]
        c.video = data["video"]
        c.metadata = data["metadata"]
        c.filename = data["filename"]
        return c