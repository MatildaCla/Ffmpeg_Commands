@echo off
ffprobe -i %1 -show_entries stream=channels -select_streams a:0 -of compact=p=0:nk=1 -v 0 > temp.txt
set /p channels=<temp.txt

if %channels%==2 (ffmpeg -i %1 -ac 1 %1_mono.mp4) else (ffmpeg -i %1 -ac 2 %1_stereo.mp4)

del temp.txt