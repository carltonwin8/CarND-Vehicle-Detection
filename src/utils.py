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
import cv2
import hashlib

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

def check_single(items):
    if len(items) > 1:
        raise ValueError('Single video generation supported at present')

    return items[0]

def check_singles(channels, ssahbs, colors):
    return check_single(channels), check_single(ssahbs), check_single(colors)

class detect():
    def __init__(self, channel, ssahb, color, train_big, heat_only):
            tfn, dfn = trained_fn(train_big, ssahb, channel, color)
            self.svc, self.X_scaler = load_trained_svm(tfn)
            self.heat_only = heat_only
            self.channel = channel
            self.ssahb = ssahb
            self.color = color

    def cars(self, img):
        return lf.get_cars(img, self.svc, self.X_scaler, 
                           self.color, self.channel, (self.ssahb, self.ssahb), self.ssahb, 
                           heat_only=self.heat_only)

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
    channels, ssahbs, colors = config.get_channel_ssahb_color(cfg)
    cars, not_cars = get_example_fns(train_big)
    for ssahb in ssahbs:
        for channel in channels:
            for color in colors:
                ds = "big" if train_big else "small"
                fmt_str = '{} data set with {} car & {} not cars, trained for ssahb{}, hogc{} for {}'
                print(fmt_str.format(ds, len(cars), len(not_cars), ssahb, channel, color))
                hc = channel if channel < 3 else "ALL"
                t3 = tl.time()
                svc, X_scaler = lf.train_svm(cars, not_cars, color_space=color, 
                                             channel=hc, hist_bins=ssahb,
                                             spatial_size=(ssahb,ssahb))
                t4 = tl.time()
                fn, tfn = trained_fn(train_big, ssahb, channel, color)
                print('{} generated in {} seconds'.format(tfn, round(t4-t3, 0)))
                save_trained_svm(fn, svc, X_scaler)

    t5 = tl.time()
    print('Total time {} seconds'.format(round(t5-t1, 0)))
    print(tl.tlog)
    
def show_feature_info(cat, notcar):
    fmtstr = "{} len={}, shape={}, min={}, max={}"
    print(fmtstr.format("car",len(car), car.shape, np.min(car), np.min(car)))
    print(fmtstr.format("notcar",len(notcar), notcar.shape, np.min(notcar), np.min(notcar)))
    
def trained_fn(train_big, ssahb, channel, color):
    tfnp = '_ssahb{}_hc{}_{}.p'.format(ssahb, channel, color)
    tfn = 'b' + tfnp if train_big else 's' + tfnp
    fn = config.train_dir + tfn
    return fn, tfn
    
def save_fn(train_big, ssahb, channel, color, fn):
    fnp = '_{}_s{}_h{}_{}.'.format('b' if train_big else 's',
            ssahb, channel, color)
    base, ext = fn.split('/')[-1].split('.')
    return config.img_out_dir + base + fnp + ext

def view_fn(train_big, ssahb, channel, color, fn):
    return save_fn(train_big, ssahb, channel, color, fn).replace("../../","../")

def basefn(imgfns, color, channel):
    file, ext = imgfns.split('/')[-1].split('.')
    fn = "{}_{}_{}.{}".format(file, color, channel, ext)
    return config.img_out_dir + fn

def gen_view_md():
    train_big = False
    channels, ssahbs, colors = config.get_hogc_ssahb_color(4)
    for ssahb in ssahbs:
        for color in colors:
            for channel in channels:
                imgfns = config.get_images(8)
                str = '| {}_s{}_h{}_{} '.format('b' if train_big else 's', 
                         ssahb, channel, color)
                str2 = '| '
                for imgfn in imgfns:
                    fn = basefn(imgfn, color, channel)
                    str2 += '| ![]({}) '.format(fn.replace("../../","../"))
                    str += '| ![]({}) '.format(view_fn(train_big, ssahb, channel, color, imgfn))
                str += "|"
                str2 += "|"
                print(str2)
                print(str)

#gen_view_md() # uncomment and run this file to get images file names

def gen_channels():
    """Shows all channel for a given image and color space by creating images"""
    for imgfns in config.get_images(8):
        image = mpimg.imread(imgfns)
        for color in ["RGB", "HSV", "LUV", "HLS", "YUV", "YCrCb"]:
            for channel in [0,1,2,3]:
                if color == "RGB":
                    img = image
                else:
                    img = cv2.cvtColor(image, config.color_conv_map[color][0])
                if channel > 2:
                    if color != "RGB":
                        img = cv2.cvtColor(img, config.color_conv_map[color][1])
                    imgC = cv2.cvtColor(img, config.color_conv_map["RGB"][1])
                else:
                    imgC = img[:, :, channel]
                cv2.imwrite(basefn(imgfns, color, channel), imgC)
                
#gen_channels() # uncomment and run this file to get images files

def check_md5sum():
    """Check to verify that all the trained svm are actually different"""
    files = os.listdir(config.train_dir)

    filehash = {}    
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    for file in files:
        with open(config.train_dir + file, 'rb') as f:
            while True:
                data = f.read(BLOCKSIZE)
                if not data:
                    break
                hasher.update(data)
        filehash[file] = hasher.hexdigest()
            
    for file in sorted(list(filehash.keys())):
        print('| {} | {} |'.format(file, filehash[file]))

    for hash in sorted(list(filehash.values())):
        print('| {} |'.format(hash))


#check_md5sum() # uncomment and run this file to get checksums
    