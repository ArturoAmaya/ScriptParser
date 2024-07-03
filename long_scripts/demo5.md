Name: Arturo Amaya
Lecture Name: Lecture 10
HeyGen API key: MTFjNTNmMjJjZjBlNGRlN2I4NWRiYTM0YTNkMzZjN2QtMTcwODk3Mjg0NQ==
Default Composition: [type:pip]
Default Transition: {type: fade, duration: 1.0}
Default Avatar: (id:Luke_public_3_20240306, voice_id:5dddee02307b4f49a17c123c120a60ca, position:0.25;0.75, scale: 0.5, style:closeUp, cbc:#453423, bc:#FFEE22)
Slides:
    https://drive.google.com/file/d/1f0sQdhUOb8KPPrHn8zcx-2a3FyPTys8p/view?usp=sharing
    https://drive.google.com/file/d/16ICuDKEWdFF0CkteD-5GLfiPuDwL8jUf/view?usp=sharing
    https://drive.google.com/file/d/1TqyvrZ1-szV2Uc4hNpdnlQo6EDjDtV86/view?usp=sharing
    https://drive.google.com/file/d/1Oqqry75uchhHZGxd_7TcIPS_ellzfn-U/view?usp=sharing
    https://drive.google.com/file/d/1CjW3zxc2X_S4TxTgOWx_cvXsXV-JRBQE/view?usp=sharing
--

So I'm going to access a location four. Location four happens in this first cache block. And so I want that data C, and so I'm going to go access it and put it into cache. Notice I put the tag here as zero because that's the cache that's the first address of the cache block. 

Now, I get another access, which is 24 and that's a miss. I look at the cache, it's not there. And so I load this line.  Okay. And I put 16 there. I've got two things in my cache. If I do one more access, what's going to happen? Well, two things could happen. 

So you're going to hit in the cash or going to miss access location eight. So this is location zero is eight. Because each of these is four bytes. That hits in this cache entry. That's great.  Okay.

And now we access location 48, which is not in the cache. So 48 is the bottom block and it's not block zero block 16, and now I'm going to replace somebody. Which one should I replace? The top one or the bottom one. Yeah. B that's not something not being used for a long time. Which of these should I replace? 01616 because I just hit on zero. That means I probably need to remember something. I hadn't put it in the slide here. But the tag has to have some information that says, Hey, I just use this cache line, probably it's still hot. Don't evict it if you can avoid it. I'm going to evict the bottom one. I put that data in there. 

Now let's do a store to address four. This data C here is going to become xx It's a hit X. Now notice what I did here, is I put this D next to that. Why did I do that? Right. Exactly. I signifies that the cash line is dirty because in the previous thing, I just evicted a cash line. I just erased it. I overwrote this bottom line. I just erased what was there before. I can't do that this one. When I evict, this modified data has to be written to Address four and made visible. Yeah. The previous miss, which one? So that miss was the first time we access this block here. So that would be compulsory. There's nothing we can do about it because if we've never accessed it before, even in infinite cash, we will have that miss. We'll talk about that maybe at the beginning of next time lecture. Compulsory misses are basically just take the stream of addresses and if the cache was infinitely big and you still have those misses, then they're compulsory. They're cold misses. Then as you make the cache smaller, the additional misses you get because the cache isn't big enough become capacity misses. That would be a fully associative cache that is smaller than infinite. Then if you now make it set associative, which we'll talk about what these things are those additional misses did become conflict misses. That's the way you do that. I think there's a homework problem like that.  Okay.