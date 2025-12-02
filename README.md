# music-duplicate-sorter
Got music files that shares the same names but you just want to get ones with lyrics, album cover or one with the highest bit rate? 

It groups files by “same song name” (ignoring punctuation, spaces, underscores, etc.)

For each group of duplicates, it scores the files based on:

+ Embedded lyrics (+2)

+ Highest bit rate (+1)

+ Album cover (+1)

If multiple files tie on score, it picks the one with the shortest filename

Finally, it moves the selected “best” file for each song to the output folder
\textbf{amogus}
