Name: Arturo Amaya
Lecture Name: Lecture 10
HeyGen API key: MTFjNTNmMjJjZjBlNGRlN2I4NWRiYTM0YTNkMzZjN2QtMTcwODk3Mjg0NQ==
Default Avatar ID: Luke_public_3_20240306
Default Voice ID: 5dddee02307b4f49a17c123c120a60ca
Default Composition: [type:pip, style:closeUp, position:(0.75;0.75)]
Default Transition: {type: fade, duration: 1.0}
Slides:
    https://drive.google.com/file/d/1p5OyujCWBFxLogcAllLe_fPR_A72fyS2/view?usp=share_link
    https://drive.google.com/file/d/1aCsa_WcVk4goJPBOKtSmZpIsKJNOWaw-/view?usp=share_link
    https://drive.google.com/file/d/1y-ly8HI061xbp25DQ3mhUOEwrIxqIbbd/view?usp=share_link
    https://drive.google.com/file/d/1xh1JPrktNOeri7bHAwu_kDc9SIt4_mjp/view?usp=share_link
    https://drive.google.com/file/d/1az8Qxl913EG1jh2GJdlTmdCrK_FWHB-D/view?usp=share_link
    https://drive.google.com/file/d/1dBosQvnt3V7eccNrVvJdRqyEIj7tHY9V/view?usp=share_link
    https://drive.google.com/file/d/1Mc0xorooDDiMyeSOf6k0j8ttes3n02Sp/view?usp=share_link 
--

Welcome to an alpha version of UCSD's markdown to lecture pipeline. This early version only supports basic concatenation of videos and has little to no input verification, so please use with caution. {} Also make sure each paragraph has less than 2000 characters. The only interesting thing it does is fade in between videos. To indicate you want a different clip to begin, simply introduce a newline like this 🕓🕓🕓🕓🕓🕓🕓🕓🕓🕓

{dissolve, 5.0} [style:circle, position:(0.5;0.75)]This is a different video. If everything worked, it's been stitched together with the previous video with a visual and audio cross fade. The only clip composition that is currently supported is the picture in picture made by heygen with default a setting of placing the avatar at half scale in the bottom right of the slide. Slides advance in order with the each paragraph.

{circlecrop}[style: normal, scale:0.7]Future versions of this program will expand on these functionalities. I will figure out how to import a PDF instead of a series of images. I will support more complex clip compositions such as side by side, avatar-only, slide-only and imported media as well as more advanced transitions like sudden changes mid-sentence or wipes and slides or cross dissolves. The markdown syntax will obviously evolve concurrently.
{zoomin, 1.0}This also counts as a new line in this version. Make sure that you don't use more than 5 paragraphs because each API key only has 5 POST requests available per day. Have fun with it.To supply your own slides make sure they are in jpg format and are publicly accessible. You can use these sample slides if you wish as well.