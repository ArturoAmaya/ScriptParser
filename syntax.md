# Script Syntax
This document should serve to define the syntax that will b parsed by the script parser. It will a bit rambl-y while I get my thoughts down. 

## Header
This section of the document will identify basic global parameters:
- (User) name [string]: Name of the user
- Lecture Name [string]: The name of the lecture, and the name of the output video (in .mp4 format)
- HeyGen API key [string]: The HeyGen API key that will be used for the requests.
- Default Avatar ID [string]: The identifying id of the avatar to be used by default. 
- Default Voice ID [string]: The id of the voice to be used by default.
- Slides [list[string]]: A list of links to the images to be used as slide backgrounds. They will be used sequentially unless overwritten.
- Default Composition: The type of clip the script will generate for every clip unless overridden. If not specified, will default to Heygen Picture in Picture.
- Default Transition: The type of transition the script will generate between clips unless overridden. If not specified, will default to Fade in.

Most of the parameters here are obvious. I'm not going to clarify how a name works. Having said that, there are things that require clarification. Notably, I must clarify the composition and transition.

## Body
The body is simple. write text. Broadly speaking, each paragraph represents a new clip, which means a new slide. Newlines with no transition information represent a default transition, as do transition commands with no parameters. Paragraphs with no composition information represent a default composition, and composition commands invoked mid paragraph imply a concatenation transition between the two sections of the scene (concatenation means no transition, just a sudden change). Transition commands mid-paragraph work the same way as if they had been called with a new line.

### Transition
Transitions are relatively simple. I will say transitions are invoked with opening and closing "{}". That is, an empty {} indicates a default transition with its default parameters. Inside I will use key-value pairs. Every key-value in the {} overwrites the corresponding key in the default. A transition has quite simple parameters. It has a type and a type and a duration (in seconds).

- type [enum[str]]: The type of transition. I will support all of the transitions supported by FFMPEG's [xfade command](https://trac.ffmpeg.org/wiki/Xfade). In addition I will support concat, which means no transition. Concat needs no duration value
- duration [float]: The duration of the transition. In seconds.

Since there are only two parameters in a command and they are different types, I will accept arguments separated by a comma in any order. Thus, the following are all equivalent:

- {type: fade, duration: 5}
- {type: fade, duration: 5.0}
- {type: fade, 5}
- {type: fade, 5.0}
- {5, fade}
- {5.0, fade}
- {fade, 5}

The recommended from is in key-value pair format. I personally will probably default to the last format for simplicity.

### Composition
Composition refers to how a particular clip is constructed. Composition commands are triggered with [] and inside use key-value pairs to override defaults. 

There are a few compositions that I wish to support. Currently I support picture in picture made by heygen. I wish to also support non-heygen pip, side by side, avatar-only, and media-only. 

Each of those has parameters that become important as they get picked. 

- HeyGen Pip: 
Avatar position, Avatar Scale, avatar style, Output Dimension
- Non-Hey Gen Pip: 
Avatar position, Avatar Scale, Slides position, Slide scale, true background, avatar background, output dimension.
- Side-by-Side: avatar position, avatar scale, slides position, slide scale, true background, avatar background, output dimension [avatar width, avatar_side, slides_side]
- Avatar Only: Avatar position, avatar scale, Avatar style, avatar background, true background.
- Media Only: media url

The common attributes that are required are:
- avatar position [tuple[float,float]]: position of the top left of the avatar video with respect to the whole scene and the dimensions. (0,0) means top left of the scene. Values are [0.0,1.0] (I believe, I should test that on heygen).
- avatar scale [float]: scale of the avatar. [0.0,2.0]
- avatar style [enum]: normal, closeUp or circle
- output dimension [tuple[int, int]]: output dimension in pixels. Defaults to 1280,720 while I have a trial plan. 
- Slides position [tuple[float,float]]: same as avatar_position
- Slides scale: same as avatar scale
- true background: color of overall background. CSS keywords supported along with #XXXXXX style. 
- avatar_background: color of avatar's background if necessary. 
- avatar_width [float]: how wide the side-by-side snippet of the avatar should be. TODO
- avatar_side [enum]: what side the avatar is on, left or right. TODO
- slide_side [enum]: what side the slides should be on. TODO
- media url: url of the media to be displayed. TODO

So scene is defined by type and all of the above parameters. Not all of them matter for all types.


