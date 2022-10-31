# S2
The solutions for the Seminar 2 exercises.

All .cmd files can be run in the command line to compete the tasks. The explicit use is explained below. 
Alternatively, the file python_integration.py can be used to execute the functions.

Example results for all the functions can be found in the results folder. The original video that was manipulated by the functions to create the results is:
https://www.youtube.com/watch?v=7Nn7NZI_LN4&ab_channel=CatNaviDesk


# 1) Trim Video
The file trimVideo.cmd can be called to trim a video. A new video called "*originalFileName*_*numberOfSeconds*_seconds.mp4" will be created. 
When calling the trimVideo.cmd two arguments need to be passed: The original video file and the desired length of the new video in seconds.

# 2) YUV Histogram
YUV_histogram_overlay.cmd will take a video and output a new video which has the YUV histogram of the current frame overlayed. The name of the original video file needs to be passed as an argument.
The new video is saved as "*originalVideoName*YUV.mp4".

# 3) Resize Video
resizeVideo.cmd and resizeToSpcifiedSizes.cmd both take a video and resize it.
resizeVideo.cmd takes three arguments: the file name of the original video, the new width in pixels, the new height in pixels. If -1 is passed for either width or height the dimension will be calculated automatically while keeping the aspect ratio.

resizeToSpcifiedSizes.cmd takes only one argument: the video file name. It outputs four new files in the following dimensions: 
· 720p
· 480p
· 360x240
· 160x120

The new videos are saved as "*originalVideoName*_*width*x*height*.mp4".

# 4) Audio Channels
MonoToStereo_StereoToMono.cmd takes a video and converts the audio channels either to mono or stereo depending on the input video. Only the name of the original video file needs to be passed as an argument.
The converted video is saved as "*originalVideoName*_mono.mp4" or "*originalVideoName*_stereo.mp4".
