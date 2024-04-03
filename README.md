# ScriptParser
A *VERY* basic python script parser for HeyGen scripts.
Basically all I'm doing is creating .md files with the following syntax/structure:

```
Name: Arturo Amaya
Lecture Name: Lecture 10
HeyGen API key: *key*
Creatomate API key: *key*
Avatar ID: *ID*
Voice ID: *ID*
Slides:
    *link*
    *link*
    *link*
    *link*
--

Welcome to a script made for UCSD's online master's classes. Every snippet here represents something that will be said by the avatar. Whenever you want to change slides simply use two backslashes together, like so. \\ That will change the slides. Slides are provided in the header individually, for now. \\ 

The contents of the slides are, for now, not dynamic. I don't know how to parse things yet. I am still trying to learn more on the subject. \\ I can however use the basic Python string manipulation functions to streamline my process. It has become too annoying to do in Postman. \\

There are a few things I still have to consider. The new HeyGen API seems to be more powerful. \\ My toodoo list includes the following: find out if or how to do transitions between clips in heygen, how HeyGen templating works, explore more creatomate and its own templates, and explore remotion, the react alternative to the JSON-API based approach I'm currently taking. \\ Thank ends my TED talk, thank you. 
```


