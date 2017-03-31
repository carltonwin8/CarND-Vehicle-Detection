#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script used during the development and debug phase for visualization
and used to generate the images used for the documentation.

@author: Carlton Joseph
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import utils
import config
import lesson_functions as lf
import cv2
import time
import numpy as np

def select_example_images(execute):
    """Selects and example image to work with"""
    if not execute:
        return
    cars, notcars = utils.get_example_fns()
    utils.store_example_images(cars, notcars)
    
def gen_hog(execute, show=True, save=False):
    """Generates the hog visualization for images"""
    if not execute:
        return

    imgs = [(config.vehicle, config.get_vehicle_hog()),
            (config.get_not_vehicle(), config.get_not_vehicle_hog())]
    for img in imgs:
        img_in = mpimg.imread(img[0])
        image = cv2.cvtColor(img_in, cv2.COLOR_RGB2GRAY)
        orient, pix_per_cell, cell_per_block = 9, 8, 2
        features, hog_image = lf.get_hog_features(image,orient,pix_per_cell,cell_per_block)
        if show:
            plt.subplot(121)
            plt.imshow(image, cmap='gray')
            plt.title('Example Image')
            plt.subplot(122)
            plt.imshow(hog_image, cmap='gray')
            plt.title('HOG Visualization')
        if save:
            img_out = img[1]
            cv2.imwrite(img_out, utils.scale_img(hog_image))
                
def train_svm(execute):
    """Traines the SVM"""
    if not execute:
        return
    
    cars, notcars = utils.get_example_fns()
    lc, lnc = len(cars), len(notcars)
    print('{} cars + {} not cars = {} images'.format(lc, lnc, lc + lnc))
    t=time.time()
    svc, X_scaler = lf.train_svm(cars, notcars)
    t2 = time.time()
    print('{} Seconds to read {} images'.format(round(t2-t, 2), len(cars) + len(notcars)),
          ', extract & scale features and train the SVC')
    utils.save_trained_svm(svc, X_scaler)

def process_image(imgfn, svc, X_scaler,
                  ssahb, channel, color, train_big, dc, heat_only, ss):
    """Searches for cars in images while varying features"""
    image = mpimg.imread(imgfn)
    
    if ss: # select subsampeling algorithm
        heat_thres = 2
        scales = [1, 1.5]
        windows = []
        for scale in scales:
            windows.extend(lf.find_cars(image, svc, X_scaler, 
                               spatial_size=(ssahb, ssahb), hist_bins=ssahb,
                               scale=scale))
        heatmap, labels = lf.heat_map(image, windows, heat_thres)
        cars = np.copy(image)
        if not heat_only:
            cars = lf.draw_boxes(cars, windows, color=(0, 0, 255), thick=6)
        cars = lf.draw_labeled_bboxes(cars, labels)
    else:
        cars = dc.get_cars(image)
#    hot_windows = lf.detect_cars_in_image(image, svc, X_scaler)
#    threshold = 4
#    heatmap, labels = lf.heat_map(image, hot_windows, threshold)
    return cars
                            

        
def process_images(execute, show=False, save=True):
    """Searches for cars in images while varying features"""
    channels, ssahbs, colors = config.get_channel_ssahb_color(15)
    imgfns = config.get_images(8)
    heat_only = False
    train_big = True
    xy_windows = config.get_xy_windows(1)

    t0 = time.time()
    for ssahb in ssahbs:
        for channel in channels:
            for color in colors:
                tfn, dfn = utils.trained_fn(train_big, ssahb, channel, color)
                svc, X_scaler = utils.load_trained_svm(tfn)
                dc = utils.detect(channel, ssahb, color, train_big, heat_only,
                                  xy_windows, True, 2, 1)
                t1 = time.time()
                for imgfn in imgfns:
                    print(imgfn)
                    for ss in [True]:
                        t2 = time.time()
                        cars = process_image(imgfn, svc, X_scaler,
                                      ssahb, channel, color, train_big, dc, 
                                      heat_only, ss)
                        if show:
                            plt.imshow(cars)
                            plt.show()
                        if save:
                            fn = utils.save_fn(train_big, ssahb, channel, color, ss, imgfn)
                            cv2.imwrite(fn, cv2.cvtColor(cars, cv2.COLOR_BGR2RGB))
                                    
                        t3 = time.time()
                        fmtstr = '{} Seconds to process {} with {} and ss ({})'
                        print(fmtstr.format(round(t3-t2, 1), imgfn, dfn, ss))    
                        if ss:
                            print(lf.log.ss.windows[0:5])
                            print(lf.log.ss.hot_windows[0:5])
                        else:
                            print(lf.log.nss.windows[0:5])
                            print(lf.log.nss.hot_windows[0:5])
                print('{} Seconds to process {} images'.format(round(t3-t1, 1), len(imgfns)))
    fmt_str = '{} Seconds for {} image in {}, {}, {}.'
    print(fmt_str.format(round(t3-t0, 1), len(imgfns), channels, ssahbs, colors))    

def main():
    """
    Description
    """
    select_example_images(False)
    gen_hog(False, save=False, show=False)    
    train_svm(False)
    process_images(True, show=False, save=True)
    
if __name__ == "__main__":
    main()
