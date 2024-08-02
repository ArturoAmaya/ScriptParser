# ScriptParser

This is a basic script parser for generating AI videos, from text to final cut. Uses HeyGen to generate AI avatars and feed them things to say. I use a markdown syntax discussed in $\verb|syntax.md|$ and exemplified by all the files in the examples folder as well as the notebook_scripts folder. Sample notebooks are available below. Check the tags on github to see how the tool has evolved, or just scroll all the way down to use the latest version.

Note to self for the future: use the clock emoji to introduce 0.5 second pauses to the video through the API. might be necessary for handling transitions.

Please click [here](https://drive.google.com/file/d/1KiqV0E-sYHMi1N6KijxRI9_aMKPk3Y9x/view?usp=sharing) to see a 27-minute mini-lecture made with this tool using lecture material from professor Bryan Chin's lecture from CSE 240A, a wonderful class.

Here is a link to the HEAD of the repo in notebook form. Anyone is welcome to use it, but I make no promises as to stability or usability.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/HEAD?labpath=example.ipynb)

------------------------------------------

v0.08 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.08?labpath=example.ipynb) Added ffmpeg pip. It is unoptimized, not as fast as it could be. Oh well. It works is the important thing for now. It takes an additional parameter of avatar_position and avatar_scale. 

avatar_position describes where the top left of the avatar video will be with respect to the entire canvas. Takes two floats 0-1;0-1 describing the x and y. Also takes macros tl, tr, bl, br meaning top left, top right, bottom left, bottom right. default value is 0.6;0.6
avatar_scale describes how large the avatar video should be with respect to its original size. One float, 0-1. Defaults to 0.4. height and width are both scaled by the same amount.

Please note that to use this properly you need to have the avatar positioned in the middle its own canvas. So almost always follow this up with (position:0.5;0.5, scale:1.0)

Example usage:

[type: fpip, avatar_scale:0.3, avatar_position: 0.5;0.6](position:0.5;0.5, scale:1.0)


------------------------------------------

v0.07 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.07?labpath=example.ipynb) Added side-by-side type. Use [type:side-by-side]. It also takes tbc (a hex color string with no '#') and avatar_side, which is left or right (which side of the canvas the avatar clip should be in). Make sure to place the avatar in the middle of the composition for it to make sense. Defaults to right side and white background.

Sample command: 

[type:side-by-side, tbc:000000, avatar_side:left] (style:normal, position:0.5;0.5, scale:1.0)

------------------------------------------

v0.06 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.06?labpath=example.ipynb) Added voiceover. Simply use [type:voiceover]. The tool will take care of downloading slides. It is a little brittle so if you choose to use it pleases use the google drive link format. We are unfortunately tied to that for now.

------------------------------------------
v0.05a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.05a?labpath=example.ipynb)

Added long-form video wrapper. Not recommended for notebook use put I'll put it up here anyway. It's not recommended because longer videos take forever. I've fixed that on my local machine by using a hw-accelerator. The discussion of the effectiveness of that method for scaling up can be found in the stats folder, but it doesn't work for the notebook because the notebook doesn't have any hardware acceleration. Might be worth it to put this on a Google Colab notebook, though. They have TPUs and GPUs available for short amounts of time. 

------------------------------------------
v0.05 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.05?labpath=example.ipynb)

Changed avatar commands to use () not [] inside composition commands

-------------------------------------------
v0.04b binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.04b?labpath=example.ipynb)

Added midclip composition:
Refer to the example below:
        
        {hlwind, 3.0} [style:circle, background:#F5E3A2, position:(0.75;0.75)]This is a different video. If everything worked, it's been stitched together with the previous video with a visual and audio cross fade. The only clip composition that is currently supported is the picture in picture made by heygen with default a setting of placing the avatar at half scale in the bottom right of the slide. [type: avatar-only, style:closeUp, position:(0.25;0.75)]Slides advance in order with the each paragraph.Future versions of this program will expand on these functionalities. I will figure out how to import a PDF instead of a series of images. I will support more complex clip compositions such as side by side, avatar-only, slide-only and [type:pip, style:normal, position:(0.75;0.75)]imported media as well as more advanced transitions like sudden changes mid-sentence or wipes and slides or cross dissolves. The markdown syntax will obviously evolve concurrently.

The [type: avatar-only, style:closeUp, position:(0.25;0.75)] is invoked without a {} and without a new line. In this case the script grabs the text before the mid-sentence cut (or mid-clip cut) and adds it to the text of the new clip. In this case there are three videos in one paragraph. They all have different compositions but exactly the same text. That means they produce the same words at the same times, meaning we can use the caption files to choose when to cut the clips. Right now I use the caption files made by HeyGen which don't have word level precision. The script tries to find a best match and cut there. For example, the first cut will try to find the closest timestamp to the phrase "Slides advance in order with" in the captions and cut there. The videos are then trimmed and concatenated together. This gives gives the video a more organic feel, I think. 

-------------------------------------------
v0.04a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.04a?labpath=example.ipynb)

Please note that moreso than other versions this version is a little experimental. I wrote it, realized there's a a few potential bugs and such BUT under the right cirucmstances it works and it's a lot of added versatility so it deserves to be published here. Version B, or 0.05 or whatever the next version is called will address some if not all of issues or observations I logged in notes.md

---------------------------------------------

v0.03 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.03?labpath=example.ipynb)

Supported syntax:

    - Composition: can set position, scale, style, output_dim and background parameters within PIP format. 

        Ex: [type: pip, scale:0.5, position:(0.25;0.5)] This command will place the middle of the avatar in 25% of the way along the x dimension from the left, and halfway down from the top. It will be at half scale. The other parameters: style, output_dim and background will be set to defaults (normal, 1280x720 and #FFFFF respectively)
        
    - Transition: any transition including concatenation, any duration

        Ex: {0.5, wipeleft} This will invoke a wipeleft transition that lasts 0.5 seconds

 A quirk of the current version is that it will regex search for any [] or {} in a line regardless of where it is in the line. This will change but in theory it means you could write blah blah balh blah [command] blah blah blah and it'll accept it. Do with that what you will, it will not last too long

---------------------------------------------

v0.02a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.02a?labpath=example.ipynb)

--------------------------------------------

v0.02 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.02?labpath=example.ipynb)

--------------------------------------------

v0.01b0 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.01b0?labpath=example.ipynb) (A fun thing I found out is that if you give it a script with a link like [4] it'll just say "four") lol (only applies to this version)

--------------------------------------------

v0.01a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.01a?labpath=example.ipynb)
