#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""
import os
import glob
import matplotlib.image as mpimg
import numpy as np
import cv2
import config

def get_image_fns(base_dirs):
    images = []
    
    for base_dir in base_dirs:
        for dir in os.listdir(base_dir):
            sub_dir = os.path.join(base_dir, dir)
            for file_ext in ['jpeg','png']:
                pattern = sub_dir + '/*.' + file_ext
                images.extend(glob.glob(pattern))
    
    cars = []
    notcars = []
    for image in images:
        if 'non' in image:
            notcars.append(image)
        else:
            cars.append(image)
            
    return cars, notcars

def get_example_out_fn(img):
    imgs = img.split("/")
    fn = "_".join([imgs[-3],imgs[-2],imgs[-1]])
    out_fn = os.path.join(config.output_dir, fn)
    return out_fn

def store_example_image(imgs):
    """Extracts the middle image out of a list of images"""
    index = int(len(imgs)/2) 
    img = imgs[index]
    image = mpimg.imread(img)
    fn = get_example_out_fn(img)
    mpimg.imsave(fn, image)

def store_example_images(cars, notcars):
    store_example_image(cars)
    store_example_image(notcars)
    
def print_img_info(img):
    print(img.shape, type(img), np.max(img), np.min(img))

def scale_img(img):
    return (img*255/np.max(img)).astype(int)