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