Ok so hardware high bitrate is SO fast, but it is also so big (it's the top series of squares in file size and bottom line of time taken by a solid margin)

Hardware low bitrate does decent, but it's visually noticeably worse

Software Multithread 16 threads does the same as default for file size, but takes marginally more time than the default.

Multithread 30 has the same file sizes as HW low bitrate, but takes way too much time in comparison.

Default seems to be the best combo of size and speed which is disappointing to say the least. It takes about two hours to make a 50 minute video on an M2 Pro chip which is top of the line (albeit a bit old). That's crazy


OK, so I had an idea. What if we read the high bitrate GPU version and just output it using CPU? That is, run the hw accelerated version for the original video then just read in and out. It should take the CPU about 20 minutes to reencode this large high-bitrate video file.

The result should expect to take 40 minutes but have about 600MB of size for the final file. Let's test it out. 

It is exactly as predicted. Took about 49 minutes to make. The slowest part is by far the CPU reencoding but it dramatically reduces the final fize. In the comparing_single_methods_and_combo.png image you can tell that the HW then SW time taken line follows the HW hight bitrate pretty well then jumps up at the end, but its endpoint is significantly lower than that of any of the non-HW lines. Then the file size, it is only marginally larger than the SW multithread 16 (which is the same size as software default) but it's less than all the other dots plotted on the graph.

It is indeed the best of both worlds !! yay!


The space_to_time_ratio tableau shows that from a pareto front-type analysis using SW encoding for small videos is more worth it than the HW-encoded clips. They don't take too much longer as long as the clips don't go over 15 minutes. They are significantly smaller, though. I will thus retain the approach of SW-encoding for now. Systems that have lots of HDD memory or don't care about its use can easily see that maximizing speed is through Hw encoding, though.