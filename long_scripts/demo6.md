Name: Arturo Amaya
Lecture Name: Lecture 10
HeyGen API key: M2M4YTQ2MTJlMTRjNDk0YWFiOTJhZjg1YzQyZDJmZTktMTcxMjEwNzE3Nw==
Default Composition: [type:pip]
Default Transition: {type: fade, duration: 1.0}
Default Avatar: (id:Luke_public_3_20240306, voice_id:5dddee02307b4f49a17c123c120a60ca, position:0.25;0.75, scale: 0.5, style:closeUp, cbc:#453423, bc:#FFEE22)
Slides:
    https://drive.google.com/file/d/1V7GTM62P1PBksIivup_43pONLnV2QgbJ/view?usp=sharing
    https://drive.google.com/file/d/1oYpschSuskjUntOzKOXEcYNQ702PBDmO/view?usp=sharing
    https://drive.google.com/file/d/1ve5z1YNy7_CzsIGnD7f1H3rL4I875bg3/view?usp=sharing
    https://drive.google.com/file/d/1YmToqqCbWMHUZpvC0Qrw9EVQRLthHFsW/view?usp=sharing
--

So now we're going to go to address 40. Now, 40 is from line 32, which I think is we haven't seen before.  Okay. So I'm going to put that here. Because I recently just touched the top line, so I'm going to replace the bottom line. 

Now I get a miss here. I want to read 16. So the most recent line that I access is the bottom one, so I want to replace the top one. Now in order to bring in line 16, I've got to evict this one, which means I got to write it back like that, and then I'm going to read in the new line.  Okay.

And finally, let's do a store miss on line 52, address 52. Now, 52 is in this bottom cache block, and that was previously in the cache. This is no longer a compulsory or cold miss, Because infinite cache would still have that line. This one now becomes a capacity miss B's fully associated cash, the reason I can't have this line in there is because the fulci cash wasn't big enough.  Okay. Then I store to it. That was an example of a store miss, which we'll talk about those too. In this case, I'm storing to the cash and I'm deciding to allocate a cash line on a store miss, and that's something that's a policy that we'll talk about. Any questions? Pretty fast. Yeah. This last miss was a capacity miss of this one 16 Yeah, I think so because we had that line earlier. Yeah. Yeah. Conflict misses can only happen in non fully associative caches.  Okay. And yeah.  Okay. Any other questions?  Okay. So hopefully, I went kind of fast, but that's kind of review, hopefully, and we're going to go a little deeper into caches now.

(position:0.75;0.75) Set associated caches, say I'm going to have multiple ways. I like to call them ways, not sets. I have two blocks per set. So I can put them in zero or one, set zero or set one.  Okay. I'm sorry, set zero one way zero or way one. So I by having two way set associative, I basically have four sets now instead of eight sets, but each set has two ways.  Okay. So now I could accommodate 12 and 20 at the same time, but not the next block that's also mod four. That's the same residual mod four.  Okay. So these are kind of the degrees of freedom, fully associate direct map and way set associative. The index is the pointer to the set. Where this might be cashed.  Okay? A set is a collection of cash box with the same cash index. I have a better picture in a minute.  Okay.

(position:0.75;0.75) I like this picture which I stole from Professor Tilson.  Okay. You can think of a cache as three dimension. I've never really thought of it this way before. I've got a number of dimensions. The sets are indexed in the y axis here, which is how I like to think about it. The blocks is axis in the x direction. The bigger the cache line size, the wider this x dimension is. And then the sets is in the z direction. Those are the ways. A number of cache lines that have the same set can have multiple ways, multiple sci.  Okay. I don't usually draw it in three dimensions, but it's interesting way to think about it.  Okay.