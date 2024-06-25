Ok so hardware high bitrate is SO fast, but it is also so big (it's the top series of squares in file size and bottom line of time taken by a solid margin)

Hardware low bitrate does decent, but it's visually noticeably worse

Software Multithread 16 threads does the same as default for file size, but takes marginally more time than the default.

Multithread 30 has the same file sizes as HW low bitrate, but takes way too much time in comparison.

Default seems to be the best combo of size and speed which is disappointing to say the least. It takes about two hours to make a 50 minute video on an M2 Pro chip which is top of the line (albeit a bit old). That's crazy


OK, so I had an idea. What if we read the high bitrate GPU version and just output it using CPU? That is, run the hw accelerated version for the original video then just read in and out. It should take the CPU about 20 minutes to reencode this large high-bitrate video file.

The result should expect to take 40 minutes but have about 600MB of size for the final file. Let's test it out