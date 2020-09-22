from picamera import PiCamera
from time import sleep
import os

# Whether or not to use test values
TEST = True

# TODO: finalize real values
NUM_PICS = 40
NUM_PICS_PER_VIDEO = 20 if TEST else 144
FRAMERATE = 2 if test else 24
TIMELAPSE_INTERVAL = 2 if TEST else 600
PHOTOS_PATH = "./photos_test/" if TEST else "./photos/"
VIDEOS_PATH = "./videos_test/" if TEST else "./videos/"
PHOTO_NAME = "p_"
VIDEO_NAME = "v_"
VIDEO_LIST = "./vlist.txt"
MASTER_VIDEO = VIDEOS_PATH + ("master_test.mp4" if TEST else "master.mp4")

# ?TODO: make number of images per video configurable with option "-frames:v n"

"""
Calls an ffmpeg command to turn photos into a video.

@param video_name
@param photo_index: index of photo from which to start making the video 
"""
def make_video(video_name, photo_index = 0):
    os.system((
        "ffmpeg -framerate {3} -start_number {0} -i '{1}_%d.jpg' -c:v libx264 {2}.mp4"
        .format(photo_index, PHOTOS_PATH + PHOTO_NAME, video_name, FRAMERATE)
    ))

"""
Concatenates one video to another using ffmpeg.

@param video_path: current video
@param new_clip_path: the video to append
"""
def append_video(video_path, new_clip_path):
    # Create list file if it doesn't exist,
    # else clear content in existing file
    if os.path.isfile(VIDEO_LIST) == False
        os.system("touch {0}".format(VIDEO_LIST))
    else
        os.system.(">> {0}".format(VIDEO_LIST))
    # populate list file
    os.system((
        "printf 'file {0}\nfile {1}' >> {2}"
        .format(video_path, new_clip_path, VIDEO_LIST)
    ))
    # concat videos in list
    # ex: ffmpeg -f concat -safe 0 -i list.txt -c copy ./out.mp4
    os.system((
        "ffmpeg -f concat -safe 0 -i {0} -c copy {1}{2}"
        .format(VIDEO_LIST, VIDEOS_PATH, MASTER_VIDEO)
    ))

# TODO: while loop or use timestamp limit
def start_timelapse(stop_time = False):
    camera = PiCamera()
    for n in range(NUM_PICS):
        camera.capture('./photos_test/tanuki_' + str(n) + '.jpg')
        sleep(2)
        if (n+1) % NUM_PICS_PER_VIDEO == 0:
            video_count = int((n+1) / NUM_PICS_PER_VIDEO)
            new_video_path = VIDEOS_PATH + VIDEO_NAME + str(video_count)
            make_video(new_video_path)
            append_video(MASTER_VIDEO, new_video_path)
            
# run le code
start_timelapse()
