ffmpeg -i %1 -vf scale=1280:720 %1_720p.mp4

ffmpeg -i %1 -vf scale=640:480 %1_480p.mp4

ffmpeg -i %1 -vf scale=360:240 %1_360x240.mp4

ffmpeg -i %1 -vf scale=160:120 %1_160x120.mp4