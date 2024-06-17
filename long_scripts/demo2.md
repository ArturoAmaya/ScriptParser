Name: Arturo Amaya
Lecture Name: Lecture 10
HeyGen API key: NTYwZDhlZDhiZWIxNDUyNGE4OWU2NmVhZjBlNmFlZWItMTcxNzc5MjQ3OQ==
Default Composition:[type:pip]
Default Transition: {type: fade, duration: 1.0}
Default Avatar: (id:Luke_public_3_20240306, voice_id:5dddee02307b4f49a17c123c120a60ca, position:0.75;0.5, scale:1.5, style:closeUp, cbc:#453423, bc:#FFEE22)
Slides:
    https://drive.google.com/file/d/1JaUxTeLHEmQJqfU6uidRqYJrRUsu4Lfx/view?usp=sharing
    https://drive.google.com/file/d/1RWi9fGRAdglGB_-DDLxkzYDPPJBtN07V/view?usp=sharing
    https://drive.google.com/file/d/13R1pHWEooQiUWJlIQMw4QUbok7S0VdWI/view?usp=sharing
    https://drive.google.com/file/d/1NjQmiHkVqLx4Zk6KaYgowEc4Pfl9isOd/view?usp=sharing
--

[type:pip] (id:Mason_public_20240304, voice_id:26b2064088674c80b1e5fc5ab1a068ea, style:circle, cbc:#EE3423, scale:0.5, position:0.5;0.5)Hi everyone, welcome back to CSE 240A. I'm your instructor, Lenny McTwisties. I hope everyone had a good weekend and has come back refreshed and ready to learn! Alright, let's get to it!

Let's get started with our snippet of computer history. These computers right here are called UNIVACS. Very expensive. In 1954 there were only 4 of them in operation but they were crucial in the places where it was used, which can be seen here on the left. Univac stands for UNIversal Automatic Computer. Despite only holding 1,000 words in its memory, the UNIVAC was used for important census-related calculations and even helped man land on the moon.

Let's recap real quick. Last week I showed you this snippet of code with that we optimized in class. There were some missing statements that I've now corrected. You'll note that in the second column SLT was SGT before and that was SEQ before that. This makes out final cycle time 9, which is the same as before but is now actually correct. Apologies for the mistake. Let's move on, though.

We were talking about how we have to unroll a loop in order to get some important optimizations. Within our steady state of the loop we know that we're going to be doing the next computations so we can reorder them and do more than one at a time. (position:0.25;0.75, voice_id:26b2064088674c80b1e5fc5ab1a068ea) You can see here the loop after it has been unrolled. We adjust the SD statements to have a negative 8 offset to accomodate some of the reordering of some of the statements. 