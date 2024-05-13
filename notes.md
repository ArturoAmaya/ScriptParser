Notes on current development version of avatar-only support. 

 - [ ] Need to be able to differentiate between avatar background, true background and circle background

 - [x] The slides being out of phase has been fixed for now but it is a place to pay attention to

 - [x] Need to be able to differentiate between [] and {} that are in the start of a line from those that are in the middle, because there's special behavior for [] commands that are alone in a a line

 - [x] Note that [] commands before {} don't work, because we get a blank string (since we cut at the {} but there's no text before it)

 - [ ] Support the sending one and using it for two videos for midline cut