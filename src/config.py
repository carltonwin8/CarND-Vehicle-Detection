#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module used to store common/global variables used by all other modules

@author: Carlton Joseph
"""
class params():
    @staticmethod
    def hog(x=1):
        """Returns hog parameters orientations, pixels_per_cell and cells_per_block"""
        if x == 1:
            return [[9, 8, 2]]
        elif x == 2:
            return [[9, 8, 2]]
        else:
            return [[9, 8, 2]]

train_big = False

small_img_set = ["../../non-vehicles_smallset", "../../vehicles_smallset"]
large_img_set = ["../../non-vehicles", "../../vehicles"]

output_dir = "../output_images/"

not_vehicle = "non-vehicles_smallset_notcars1_extra511.jpeg"
vehicle = "vehicles_smallset_cars1_183.jpeg"

def get_hog_fn(name):
    """Takes a file name and return is with _hog appended"""
    fn, ext = name.split('.')
    return output_dir + fn + '_hog.' + ext

def get_not_vehicle_hog():
    return get_hog_fn(not_vehicle)
    
def get_vehicle_hog():
    """Path and filename for a vehicle image"""
    return get_hog_fn(vehicle)

def get_not_vehicle():
    """Path and filename for not a vehicle image"""
    return output_dir + not_vehicle
    
def get_vehicle():
    """Path and filename for a vehicle image"""
    return output_dir + vehicle

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
