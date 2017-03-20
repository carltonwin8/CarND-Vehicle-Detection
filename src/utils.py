#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""
import os
import glob
import matplotlib.image as mpimg
import numpy as np
import config
import pickle

def get_image_fns(base_dirs):
    """Get image filenames from a directory set"""
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

def get_example_fns():
    """Get image files name based on configuration"""
    if config.train_big:            
        cars, notcars = get_image_fns(config.large_img_set)
    else:
        cars, notcars = get_image_fns(config.small_img_set)
    return cars, notcars

def get_example_out_fn(img):
    """Creates an output filename based on an input filename"""
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
    """Saves the middle image of cars and notcars"""
    store_example_image(cars)
    store_example_image(notcars)

def print_img_info(img):
    """Prints some information about an image"""
    print(img.shape, type(img), np.max(img), np.min(img))

def scale_img(img):
    """Scales an image to full scale values"""
    return (img*255/np.max(img)).astype(int)

def save_trained_svm(svc, X_scaler):
    
    pkl = {}
    pkl["svc"] = svc
    pkl["X_scaler"] = X_scaler
    pickle.dump(pkl, open(config.trained_svm_fn(), "wb"))
     
def load_trained_svm():
    pkl = pickle.load(open(config.trained_svm_fn(), "rb"))
    return pkl["svc"], pkl["X_scaler"]


class car():
    def __init__(self, img, car, y_top, x, y):
        self.img = img
        self.car = car
        self.y_top = y_top
        self.x = x
        self.y = y
        
class car_analysis():
    """Analysis of car size measure on test images"""
    def __init__(self):
        self.cars = [car(1, 1, 407, 134, 88),
                     car(1, 2, 402, 224, 109),
                     car(2, 1, 411, 18, 16),
                     car(3, 2, 413, 94, 56),
                     car(4, 1, 407, 134, 90),
                     car(4, 2, 397, 219, 106),
                     car(5, 1, 405, 129, 82),
                     car(5, 2, 397, 201, 121),
                     car(6, 1, 408, 138, 93),
                     car(6, 2, 404, 196, 97)]