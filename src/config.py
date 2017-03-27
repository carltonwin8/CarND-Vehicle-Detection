#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module used to store common/global variables used by all other modules

@author: Carlton Joseph
"""
import cv2

train_big = True

small_img_set = ["../../non-vehicles_smallset", "../../vehicles_smallset"]
large_img_set = ["../../non-vehicles", "../../vehicles"]

output_dir = "../output_images/"
video_out_dir = "../../out/"
img_out_dir = "../../outimg/"
train_dir = "../../training/"
_not_vehicle = "non-vehicles_smallset_notcars1_extra511.jpeg"
_vehicle = "vehicles_smallset_cars1_183.jpeg"
not_vehicle = output_dir + _not_vehicle
vehicle = output_dir + _vehicle
get_hog_fn = lambda name: name.split('.')[0] + '_hog.' + name.split('.')
get_vehicle_hog = lambda: get_hog_fn(_vehicle)
get_not_vehicle_hog = lambda: get_hog_fn(_not_vehicle)
get_option = lambda opts, i: opts[i -1 if i < len(opts) else len(opts) - 1]
get_option.__doc__ = "Index into an array 1 based with overflow protection"

videos = [
    ["../../in/project_video_1s.mp4"], #1
    ["../../in/project_video_s20t6.mp4"], #2
    ["../../in/project_video_s38t5.mp4"], #3
    ["../../in/project_video_4s.mp4"], #4
    ["../../in/project_video_s20t6.mp4",
     "../../in/project_video_s38t5.mp4"], #5
    ["../../in/project_video_s20t7.mp4",
     "../../in/project_video_s38t6.mp4"], #6
    ["../project_video.mp4"] #7
]
get_videos = lambda x: get_option(videos,x)  

images = [
    ["../test_images/test1.jpg"], #1
    ["../test_images/test2.jpg"], #2
    ["../test_images/test3.jpg"], #3
    ["../test_images/test4.jpg"], #4
    ["../test_images/test5.jpg"], #5
    ["../test_images/test6.jpg"], #6
    ["../../bbox-example-image.jpg"], #7
    ["../test_images/test1.jpg",
     "../test_images/test2.jpg",
     "../test_images/test3.jpg",
     "../test_images/test4.jpg",
     "../test_images/test5.jpg",
     "../test_images/test6.jpg"] #8
]
get_images = lambda x: get_option(images,x)

channel_ssahb_color = [
    ([0, 1, 2, 3], [16, 32], ["RGB", "HSV", "LUV", "HLS", "YUV", "YCrCb"]), #1
    ([1], [16], ["LUV"]), #2
    ([0], [16], ["RGB"]), #3
    ([0, 1, 2, 3], [16], ["RGB", "HSV", "LUV", "HLS", "YUV", "YCrCb"]), #4
    ([0, 1, 2, 3], [32], ["RGB", "HSV", "LUV", "HLS", "YUV", "YCrCb"]), #5
    ([1], [16], ["LUV", "YUV"]), #6 - with small data set got 1.0 for accuracy
    ([0, 1, 2, 3], [16, 32], ["RGB", "HSV", "HLS", "YUV", "YCrCb"]), #7 remove LUV since it blows up
    ([3], [16], ["RGB", "HSV", "HLS", "YUV", "YCrCb"]), #8 
    ([0, 1, 2, 3], [32], ["RGB", "HSV", "HLS", "YUV", "YCrCb"]), #9 remove LUV since it blows up
    ([1], [16], ["RGB"]), #10
    ([1], [16], ["YCrCb"]), #11
    ([0, 1, 2, 3], [16, 32], ["YCrCb"]), #12
    ([0, 1, 2], [16], ["YCrCb"]), #13
    ([0, 1, 2], [32], ["YCrCb"]), #14
    ([3], [32], ["YCrCb"]), #15
    ([3], [32], ["RGB"]), #16
    ([3], [16], ["RGB"]), #17
]
get_channel_ssahb_color = lambda x: get_option(channel_ssahb_color,x)

color_conv_map = {
    'RGB': (cv2.COLOR_RGB2GRAY, cv2.COLOR_RGB2GRAY), # COLOR_RGB2GRAY is a dummy never used
    'HSV': (cv2.COLOR_RGB2HSV, cv2.COLOR_HSV2RGB),
    'LUV': (cv2.COLOR_RGB2LUV, cv2.COLOR_LUV2RGB),
    'HLS': (cv2.COLOR_RGB2HLS, cv2.COLOR_HLS2RGB),
    'YUV': (cv2.COLOR_RGB2YUV, cv2.COLOR_YUV2RGB),
    'YCrCb': (cv2.COLOR_RGB2YCrCb, cv2.COLOR_YCrCb2RGB)      
}
