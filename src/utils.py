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
import lesson_functions as lf
import time

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

def get_example_fns(train_big):
    """Get image files name based on configuration"""
    if train_big:            
        img_set = config.large_img_set
    else:
        img_set = config.small_img_set
    return get_image_fns(img_set)

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

def save_trained_svm(fn, svc, X_scaler):
    
    pkl = {}
    pkl["svc"] = svc
    pkl["X_scaler"] = X_scaler
    pickle.dump(pkl, open(fn, "wb"))
     
def load_trained_svm(fn):
    pkl = pickle.load(open(fn, "rb"))
    return pkl["svc"], pkl["X_scaler"]

def get_video_out(v_in):
    return config.video_out_dir + v_in.split('/')[-1]

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

class detect():
    def __init__(self, heat_only):
            self.svc, self.X_scaler = load_trained_svm()
            self.heat_only = heat_only

    def cars(self, img):
        return lf.get_cars(img, self.svc, self.X_scaler, heat_only=self.heat_only)

class time_log():
    def __init__(self,tlog):
        self.tlog = tlog
    def time(self):        
        t = time.time()
        self.tlog.append(t)
        return t
    
def gen_trained_sets(train_big, cfg):
    tlog = []
    tl = time_log(tlog)
    t1 = tl.time()
    hog_channels, ssahbs, colors = config.get_hogc_ssahb_color(cfg)
    cars, not_cars = get_example_fns(train_big)
    print('Training on data set big is {}'.format(train_big))
    for ssahb in ssahbs:
        for hog_channel in hog_channels:
            for color in colors:
                print('big {}, {} car & {} not cars, trained for ssahb{}, hogc{} for {}'.format(train_big,
                      len(cars), len(not_cars), ssahb, hog_channel, color))
                hc = hog_channel if hog_channel < 3 else "ALL"
                t3 = tl.time()
                svc, X_scaler = lf.train_svm(cars, not_cars, color_space=color, 
                                             hog_channel=hc, hist_bins=ssahb,
                                             spatial_size=(ssahb,ssahb))
                t4 = tl.time()
                tfnp = '_ssahb{}_hc{}_{}.p'.format(ssahb, hog_channel, color)
                tfn = 'b' + tfnp if train_big else 's' + tfnp
                print('{} generated in {} seconds'.format(tfn, round(t4-t3, 0)))
                fn = config.train_dir + tfn
                save_trained_svm(fn, svc, X_scaler)

    t5 = tl.time()
    print('Total time {} seconds'.format(round(t5-t1, 0)))
    print(tl.tlog)