from dataclasses import dataclass

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