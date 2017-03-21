#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module used to store common/global variables used by all other modules

@author: Carlton Joseph
"""
class hog():
    def __init__(self, orientations, pixels_per_cell, cells_per_block):
        self.orientations
        self.pixels_per_cell
        self.cells_per_block
        
class color_hist():
    def __init__(self, nbins, bins_range):
        self.orientations
        self.pixels_per_cell
        self.cells_per_block

class spatial():
    def __init__(self, size):
        self.size = size
    
class params():
    def __init__(self, hog, color, spatial, color_space):
        self.hogs = self.get_hogs(hog)
        self.color_hists = self.get_color_hists(color)
        self.spatials = self.get_spatials(spatial)
        self.color_spaces = self.get_color_spaces(color_space)
        self.hog = hog(9, 8, 2)
        self.color_hist = color_hist(32, (0, 256))
        self.spatial = spatial((32,32))
        self.color_space = "RGB"
        
    @staticmethod
    def get_hogs(x=1):
        """hog parameters orientations, pixels_per_cell and cells_per_block"""
        if x == 1:
            return [hog(9, 8, 2)]
        elif x == 2:
            return [hog(9, 8, 2)]
        else:
            return [hog(9, 8, 2)]
        
    @staticmethod
    def get_color_hists(x=1):
        """color histogram parameters nbin and bins_range"""
        if x == 1:
            return [color_hist(32, (0, 256))]
        elif x == 2:
            return [color_hist(16, (0, 256))]
        else:
            return [color_hist(16, (0, 256)), color_hist(32, (0, 256))]
    
    @staticmethod
    def get_spatials(x=1):
        """bin spatial parameters size"""
        if x == 1:
            return [spatial((32,32))]
        elif x == 2:
            return [spatial((16,16))]
        else:
            return [spatial((16,16),(32,32))]
    
    @staticmethod
    def get_color_spaces(x=1):
        """bin spatial parameters size"""
        if x == 1:
            return ["RGB"]
        elif x == 2:
            return ["LUV"]
        elif x == 3:
            return ["HSV"]
        elif x == 4:
            return ["HLS"]
        elif x == 5:
            return ["YUV"]
        elif x == 5:
            return ["YCrCb"]
        else:
            return ["RGB","YCrCb"]
        
train_big = True

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

video_out_dir = "../../out/"
def get_videos(x):
    if x == 1:
        return ["../../in/project_video_1s.mp4"]
    elif x == 2:
        return ["../../in/project_video_s20t6.mp4"]
    elif x == 3:
        return ["../../in/project_video_s38t5.mp4"]
    elif x == 4:
        return ["../../in/project_video_4s.mp4"]
    elif x == 5:
        return ["../../in/project_video_s20t6.mp4",
                "../../in/project_video_s38t5.mp4"]
    elif x == 6:
        return ["../../in/project_video_s20t7.mp4",
                "../../in/project_video_s38t6.mp4"]
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
    elif x == 7:
        return ["../../bbox-example-image.jpg"]
    else:
        return ["../test_images/test1.jpg",
                "../test_images/test2.jpg",
                "../test_images/test3.jpg",
                "../test_images/test4.jpg",
                "../test_images/test5.jpg",
                "../test_images/test6.jpg"]

def trained_svm_fn():
    if train_big:
        bs = "b"
    else:
        bs = "s"
    return "../../svm_pickle_{}.p".format(bs)
