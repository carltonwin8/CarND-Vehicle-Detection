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

    imgs = [(config.get_vehicle(), config.get_vehicle_hog()),
            (config.get_not_vehicle(), config.get_not_vehicle_hog())]
    for img in imgs:
        img_in = mpimg.imread(img[0])
        image = cv2.cvtColor(img_in, cv2.COLOR_RGB2GRAY)
        for params in config.params.hog():
            orient, pix_per_cell, cell_per_block = params
            features, hog_image = lf.get_hog_features(image,
                                                      orient, 
                                                      pix_per_cell, 
                                                      cell_per_block,
                                                      vis=True,
                                                      feature_vec=False)
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
                
def train_svm(execute, show=True, save=False):
    """Traines the SVM"""
    if not execute:
        return
    
    cars, notcars = utils.get_example_fns()
    svc, X_scaler = lf.train_svm(cars, notcars)
    image = mpimg.imread('../../bbox-example-image.jpg')
    window_img = lf.detect_cars_in_image(image, svc, X_scaler)    
    plt.imshow(window_img)

def main():
    """
    Description
    """
    select_example_images(False)
    gen_hog(False, save=True, show=False)    
    train_svm(True)
    
if __name__ == "__main__":
    main()
