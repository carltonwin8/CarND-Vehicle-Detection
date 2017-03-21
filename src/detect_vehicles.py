#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to run in order to detect vehicles in a video

@author: Carlton Joseph
"""
import utils
import argparse
import config
from moviepy.editor import VideoFileClip

def main():
    """
    Main vehicle detection function
    """
    parser = argparse.ArgumentParser(description='Process video file.')
    parser.add_argument("videos", help="video sequence",type=int, nargs='?', const=1, default=1)
    args = parser.parse_args()
    
    videos_in = config.get_videos(args.videos)
    detect = utils.detect(True)
    
    for video_in in videos_in:
        video_out = utils.get_video_out(video_in)
        print("From =>", video_in, "To =>", video_out)

        clip2 = VideoFileClip(video_in)
        clip = clip2.fl_image(detect.cars)
        clip.write_videofile(video_out, audio=False)

if __name__ == "__main__":
    main()
