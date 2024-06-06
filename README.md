# ScriptParser
This is a basic script parser for generating AI videos, from text to final cut. Uses HeyGen to generate AI avatars and feed them things to say. I use a markdown syntax discussed in $\verb|syntax.md|$ and exemplified by all the files in the examples folder as well as the notebook_scripts folder. Sample notebooks are available below. Check the tags on github to see how the tool has evolved, or just scroll all the way down to use the latest version.

Note to self for the future: use the clock emoji to introduce 0.5 second pauses to the video through the API. might be necessary for handling transitions.

--------------------------------------------

v0.01a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.01a?labpath=example.ipynb)

--------------------------------------------

v0.01b0 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.01b0?labpath=example.ipynb) (A fun thing I found out is that if you give it a script with a link like [4] it'll just say "four") lol (only applies to this version)

--------------------------------------------

v0.02 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.02?labpath=example.ipynb)

---------------------------------------------

v0.02a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.02a?labpath=example.ipynb)

---------------------------------------------

v0.03 binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.03?labpath=example.ipynb)

Supported syntax:

    - Composition: can set position, scale, style, output_dim and background parameters within PIP format. 

        Ex: [type: pip, scale:0.5, position:(0.25;0.5)] This command will place the middle of the avatar in 25% of the way along the x dimension from the left, and halfway down from the top. It will be at half scale. The other parameters: style, output_dim and background will be set to defaults (normal, 1280x720 and #FFFFF respectively)
        
    - Transition: any transition including concatenation, any duration

        Ex: {0.5, wipeleft} This will invoke a wipeleft transition that lasts 0.5 seconds

 A quirk of the current version is that it will regex search for any [] or {} in a line regardless of where it is in the line. This will change but in theory it means you could write blah blah balh blah [command] blah blah blah and it'll accept it. Do with that what you will, it will not last too long

 -------------------------------------------
 v0.04a binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.04a?labpath=example.ipynb)

 Please note that moreso than other versions this version is a little experimental. I wrote it, realized there's a a few potential bugs and such BUT under the right cirucmstances it works and it's a lot of added versatility so it deserves to be published here. Version B, or 0.05 or whatever the next version is called will address some if not all of issues or observations I logged in notes.md

 -------------------------------------------
 v0.04b binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArturoAmaya/ScriptParser/v0.04b?labpath=example.ipynb)

 Added midclip composition:
 Refer to the example below:
        
        {hlwind, 3.0} [style:circle, background:#F5E3A2, position:(0.75;0.75)]This is a different video. If everything worked, it's been stitched together with the previous video with a visual and audio cross fade. The only clip composition that is currently supported is the picture in picture made by heygen with default a setting of placing the avatar at half scale in the bottom right of the slide. [type: avatar-only, style:closeUp, position:(0.25;0.75)]Slides advance in order with the each paragraph.Future versions of this program will expand on these functionalities. I will figure out how to import a PDF instead of a series of images. I will support more complex clip compositions such as side by side, avatar-only, slide-only and [type:pip, style:normal, position:(0.75;0.75)]imported media as well as more advanced transitions like sudden changes mid-sentence or wipes and slides or cross dissolves. The markdown syntax will obviously evolve concurrently.

The [type: avatar-only, style:closeUp, position:(0.25;0.75)] is invoked without a {} and without a new line. In this case the script grabs the text before the mid-sentence cut (or mid-clip cut) and adds it to the text of the new clip. In this case there are three videos in one paragraph. They all have different compositions but exactly the same text. That means they produce the same words at the same times, meaning we can use the caption files to choose when to cut the clips. Right now I use the caption files made by HeyGen which don't have word level precision. The script tries to find a best match and cut there. For example, the first cut will try to find the closest timestamp to the phrase "Slides advance in order with" in the captions and cut there. The videos are then trimmed and concatenated together. This gives gives the video a more organic feel, I think. 

v0.05 binder: 

Changed avatar commands to use () not [] inside composition commands