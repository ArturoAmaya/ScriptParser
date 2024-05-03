from dataclasses import dataclass, asdict
from enum import Enum

""" 
These are the nominal transitions supported by normal xfade
I additionally support custom and concat (i.e. no transition)
fade (default)	fadeblack	fadewhite	distance
			
wipeleft	wiperight	wipeup	wipedown
			
slideleft	slideright	slideup	slidedown
			
smoothleft	smoothright	smoothup	smoothdown
			
circlecrop	rectcrop	circleclose	circleopen
			
horzclose	horzopen	vertclose	vertopen
			
diagbl	diagbr	diagtl	diagtr
			
hlslice	hrslice	vuslice	vdslice
			
dissolve	pixelize	radial	hblur
			
wipetl	wipetr	wipebl	wipebr
			zoomin transition for xfade
fadegrays	squeezev	squeezeh	zoomin
			
hlwind	hrwind	vuwind	vdwind
			
coverleft	coverright	coverup	coverdown
			
revealleft	revealright	revealup	revealdown """

class transition_type(str, Enum):
    FADE = "fade"
    FADEBLACK = "fadeblack"
    FADEWHITE = "fadewhite"
    DISTANCE = "distance"
    WIPELEFT = "wipeleft"
    WIPERIGHT = "wiperight"
    WIPEUP = "wipeup"
    WIPEDOWN = "wipedown"
    SLIDELEFT = "slideleft"
    SLIDERIGHT = "slideright"
    SLIDEUP = "slideup"
    SLIDEDOWN = "slidedown"
    SMOOTHLEFT = "smoothleft"
    SMOOTHRIGHT = "smoothright"
    SMOOTHUP = "smoothup"
    SMOOTHDOWN = "smoothdown"
    CIRCLECROP = "circlecrop"
    RECTCROP = "rectcrop"
    CIRCLECLOSE = "circleclose"
    CIRCLEOPEN = "circleopen"
    HORZCLOSE = "horzclose"
    HORZOPEN = "horzopen"
    VERTCLOSE = "vertclose"
    VERTOPEN = "vertopen"
    DIAGBL = "diagbl"
    DIAGBR = "diagbr"
    DIAGTL = "diagtl"
    DIAGTR = "diagtr"
    HLSLICE = "hlslice"
    HRSLICE = "hrslice"
    VUSLICE = "vuslice"
    VDSLICE = "vdslice"
    DISSOLVE = "dissolve"
    PIXELIZE = "pixelize"
    RADIAL = "radial"
    HBLUR = "hblur"
    WIPETL = "wipetl"
    WIPETR = "wipetr"
    WIPEBL = "wipebl"
    WIPEBR = "wipebr"
    FADEGRAYS = "fadegrays"
    SQUEEZEV = "squeezev"
    SQUEEZEH = "squeezeh"
    ZOOMIN = "zoomin"
    HLWIND = "hlwind"
    HRWIND = "hrwind"
    VUWIND = "vuwind"
    VDWIND = "vdwind"
    COVERLEFT = "coverleft"
    COVERRIGHT = "coverright"
    COVERUP = "coverup"
    COVERDOWN = "coverdown"
    REVEALLEFT = "revealleft"
    REVEALRIGHT = "revealright"
    REVEALUP = "revealup"
    REVEALDOWN = "revealdown"
    # special ones
    CUSTOM = "custom" # this is a surprise tool that will help us later
    CONCAT = "concat" # concatenation AND unsupported, error-type

@dataclass
class transition_in:
    t_type: transition_type
    duration: float

    def __init__(self):
        self.t_type = None
        self.duration = 1.0

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data):
        c = cls()
        c.t_type = transition_type(data["t_type"]) if data["t_type"] != None else None
        c.duration = data["duration"]
        return c