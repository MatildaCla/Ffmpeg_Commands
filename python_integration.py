import subprocess


def trim_video(name):
    seconds = input("Enter the length in seconds:")
    subprocess.run(['trimVideo.cmd', name, seconds])
    return 0


def overlay_yuv_histogram(name):
    subprocess.run(['YUV_histogram_overlay.cmd', name])
    return 0


def resize_video(name):
    print("Enter the width and height of the resulting video in pixel. "
          "Alternatively -1 can entered for one of the values to keep the aspect ratio.\n")
    width = input("Enter the width in px:")
    height = input("Enter the height in px:")
    subprocess.run(['resizeVideo.cmd', name, width, height])
    return 0


def resize_video_fixed_sizes(name):
    subprocess.run(['resizeToSpcifiedSizes.cmd', name])
    print("The video was resized to the following sizes: 720p, 480p, 360x240, 160x120")
    return 0


def transform_mono_stereo(name):
    subprocess.run(['MonoToStereo_StereoToMono.cmd', name])
    print("The audio channel was changed to mono if the original file was in stereo "
          "OR to stereo if the original file was mono")
    return 0


if __name__ == '__main__':
    vidName = input("Please enter the name of the video file:\n")

    # Call whichever of the above defined functions are needed
