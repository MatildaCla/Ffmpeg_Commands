ffmpeg -i %1 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" %1YUV.mp4