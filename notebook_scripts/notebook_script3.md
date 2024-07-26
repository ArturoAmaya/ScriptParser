Name: Arturo Amaya
Lecture Name: Example
HeyGen API key: NWQyZTUwNGRlNjhlNDU5OGJkOGQxMWQwYTM1ZjcwYmQtMTcxNDQyMzMzOQ==
Default Composition:[type:pip]
Default Transition: {type: fade, duration: 1.0}
Default Avatar: (id:Luke_public_3_20240306, voice_id:5dddee02307b4f49a17c123c120a60ca, position:0.75;0.5, scale:1.5, style:closeUp, cbc:#453423, bc:#FFEE22)
Slides:
https://drive.google.com/file/d/1y-ly8HI061xbp25DQ3mhUOEwrIxqIbbd/view?usp=share_link
    https://drive.google.com/file/d/1xh1JPrktNOeri7bHAwu_kDc9SIt4_mjp/view?usp=share_link
    https://drive.google.com/file/d/1az8Qxl913EG1jh2GJdlTmdCrK_FWHB-D/view?usp=share_link
    https://drive.google.com/file/d/1dBosQvnt3V7eccNrVvJdRqyEIj7tHY9V/view?usp=share_link
    https://drive.google.com/file/d/1Mc0xorooDDiMyeSOf6k0j8ttes3n02Sp/view?usp=share_link 
    https://drive.google.com/file/d/1p5OyujCWBFxLogcAllLe_fPR_A72fyS2/view?usp=share_link
    https://drive.google.com/file/d/1aCsa_WcVk4goJPBOKtSmZpIsKJNOWaw-/view?usp=share_link
--

[type:avatar-only] (id:Mason_public_20240304, voice_id:26b2064088674c80b1e5fc5ab1a068ea, style:circle, cbc:#EE3423, scale:0.5, position:0.5;0.5) This is a script that is available for notebook users to use. I promise to not really use these for my testing insofar that is possible so that demo users can use the tool.

[type: side-by-side] {dissolve} (position:0.5;0.5) Feel free to edit the script I've included here to make things more interesting and test out your own videos. There are a few examples of syntax scattered through these notebooks. Feel free to make things as wacky and weird as you like. Or just run the given script. If you want to learn more about the script syntax, just go to the syntax file, or the example jupyter notebook. 

[type:pip] (id:Mason_public_20240304, voice_id:26b2064088674c80b1e5fc5ab1a068ea, style:circle, cbc:#EE3423, scale:0.5, position:0.5;0.5)Hi everyone, welcome back to CSE 240A. I'm your instructor, Lenny McTwisties. I hope everyone had a good weekend and has come back refreshed and ready to learn! Alright, let's get to it! Let's recap real quick. Last week I showed you this snippet of code with that we optimized in class. There were some missing statements that I've now corrected. You'll note that in the second column SLT was SGT before and that was SEQ before that. This makes our final cycle time 9, (position:0.25;0.75) which is the same as before but is now actually correct. Apologies for the mistake. Let's move on, though.We were talking about how we have to unroll a loop in order to get some important optimizations. Within our steady state of the loop we (position: 0.3;0.4, id:Mason_public_20240304, voice_id:26b2064088674c80b1e5fc5ab1a068ea) know that we're going to be doing the next computations so we can reorder them and do more than one at a time.  You can see here the loop after it has been unrolled. We adjust the SD statements to have a negative 8 offset to accomodate some of the reordering of some of the statements. 