#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module used to store common/global variables used by all other modules

@author: Carlton Joseph
"""


def get_videos(x):
    if x == 1:
        return ["../../project_video_1s.mp4"]
    elif x == 2:
        return ["../../project_video_s20t6.mp4"]
    elif x == 3:
        return ["../../project_video_s38t5.mp4"]
    elif x == 4:
        return ["../../project_video_4s.mp4"]
    elif x == 5:
        return ["../../project_video_s20t6.mp4",
                "../../project_video_s38t5.mp4"]
    elif x == 6:
        return ["../../project_video_s20t7.mp4",
                "../../project_video_s38t6.mp4"]
    else:
        return ["../project_video.mp4"]


def get_images(x):
    if x == 1:
        return ["../test_images/test1.jpg"]
    elif x == 2:
        return ["../test_images/test2.jpg"]
    elif x == 3:
        return ["../test_images/test3.jpg"]
    elif x == 4:
        return ["../test_images/test4.jpg"]
    elif x == 5:
        return ["../test_images/test5.jpg"]
    elif x == 6:
        return ["../test_images/test6.jpg"]
    else:
        return ["../test_images/test1.jpg",
                "../test_images/test2.jpg",
                "../test_images/test3.jpg",
                "../test_images/test4.jpg",
                "../test_images/test5.jpg",
                "../test_images/test6.jpg"]
