from dataclasses import dataclass

@dataclass
class avatar_video:
    id: str=None
    url: str=None
    video: object=None
    metadata: object=None

    def __init__(self):
        self.id = None
        self.url = None
        self.video = None
        self.metadata = None