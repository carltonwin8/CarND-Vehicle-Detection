# Vehicle Detection Project Notes

This is my scratch pad for ideas and is not official documentation.

big data set has 8792 car & 8968 not cars,
small data set has 1196 car & 1125 not cars

## Brain Storming

### TO DO

  - generate trained file with correct hog, bin_spatial and color histograms.
    - need to identify which color space is used for the generation and note this value
    - can look at **find_cars** to determine what is bing used
      and then use the same thing for the training
    - need to scale hog, bin_spatial and color histograms correctly for
      training and in **find_cars***
    - after the classifier has been trained figure out the minimum parameters
      for **find_cars** and run that procedures
    - when that is done try this on the test images and 1 second videos
    - verify the timing difference vs the first implementation
    - run the full video
    - start doing averaging over frames
  - add all the visualization images
 - verify that during training the images are scaled correctly
   because apperently jpeg's and png's are read in at different scales

## Parameters

HOG

+ detect_cars_in_image color_space = 'RGB', spatial_size = (16, 16), hist_bins = 16,
                        orient = 9, pix_per_cell = 8, cell_per_block = 2, hog_channel = 0,
                        spatial_feat = True, hist_feat = True, hog_feat = True, y_start_stop = [400, 650]
  - search_windows clf, scaler, color_space='RGB', spatial_size=(32, 32), hist_bins=32, hist_range=(0, 256),
                          orient=9, pix_per_cell=8, cell_per_block=2, hog_channel=0,
                          spatial_feat=True, hist_feat=True, hog_feat=True):
     * single_img_features -  color_space='RGB', spatial_size=(32, 32), hist_bins=32,
                          orient=9, pix_per_cell=8, cell_per_block=2, hog_channel=0,
                          spatial_feat=True, hist_feat=True, hog_feat=True
  - train_svm color_space = 'RGB', spatial_size = (16, 16), hist_bins = 16,
                          orient = 9, pix_per_cell = 8, cell_per_block = 2, hog_channel = 0,
                          spatial_feat = True, hist_feat = True, hog_feat = True, y_start_stop = [400, 650]
     * extract_features - color_space='RGB', spatial_size=(32, 32), hist_bins=32,
                          orient=9, pix_per_cell=8, cell_per_block=2, hog_channel=0,
                          spatial_feat=True, hist_feat=True, hog_feat=True
     * find_cars - ystart=400, ystop=650, scale=1, spatial_size,=(32, 32) hist_bins=32
                          orient=9, pix_per_cell=8, cell_per_block=2
       + get_hog_features


## Vehicle Sizes in images

| Id | Description |
| --- | --- |
| 1 | Black car |
| 2 | White car |
| 3 | Small not discernibly |
| 4 | Gray small |

| Id | Image |
| --- | --- |
| 1 | test1.jpg |
| 2 | test2.jpg |
| 3 | test3.jpg |
| 4 | test4.jpg |
| 5 | test5.jpg |
| 6 | test6.jpg |
| 7 | bbox-example-image.jpg |

The Y location is the top of the box. Size is width x height.

| Image | Car | Y | Size | Notes |
| --- | --- | --- | --- |
|  1  | 1 | 407 | 134x88 | |
|  1  | 2 | 402 | 224x109 | |
|  2  | 1 | 411 | 18x16 | Only one vehicle far away |
|  3  | 2 | 413 | 94x56 | one vehicle middle distance |
|  4  | 1 | 407 | 134x90 | |
|  4  | 2 | 397 | 219x106 | |
|  5  | 1 | 405 | 129x82 | |
|  5  | 2 | 397 | 201x121 | |
|  6  | 1 | 408 | 138x93 | |
|  6  | 2 | 404 | 196x97 | |

## Training Output

small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc0 for RGB
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc0_RGB.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc0 for HSV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc0_HSV.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc0 for LUV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc0_LUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc0 for HLS
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc0_HLS.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc0 for YUV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc0_YUV.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc0 for YCrCb
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc0_YCrCb.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc1 for RGB
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc1_RGB.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc1 for HSV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc1_HSV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc1 for LUV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc1_LUV.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc1 for HLS
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc1_HLS.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc1 for YUV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc1_YUV.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc1 for YCrCb
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc1_YCrCb.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc2 for RGB
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc2_RGB.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc2 for HSV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc2_HSV.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc2 for LUV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc2_LUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc2 for HLS
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.96.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc2_HLS.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc2 for YUV
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc2_YUV.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc2 for YCrCb
1856 in training set with feature vector length of 2580
Features extracted in 8.0 seconds and trained SVC in 0.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc2_YCrCb.p generated in 8.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for RGB
1856 in training set with feature vector length of 6108
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_RGB.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for HSV
1856 in training set with feature vector length of 6108
Features extracted in 17.0 seconds and trained SVC in 0.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_HSV.p generated in 18.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for LUV
1856 in training set with feature vector length of 6108
Features extracted in 18.0 seconds and trained SVC in 0.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_LUV.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for HLS
1856 in training set with feature vector length of 6108
Features extracted in 17.0 seconds and trained SVC in 0.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_HLS.p generated in 18.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for YUV
1856 in training set with feature vector length of 6108
Features extracted in 17.0 seconds and trained SVC in 0.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_YUV.p generated in 18.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for YCrCb
1856 in training set with feature vector length of 6108
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_YCrCb.p generated in 18.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc0 for RGB
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 2.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc0_RGB.p generated in 10.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc0 for HSV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc0_HSV.p generated in 10.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc0 for LUV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc0_LUV.p generated in 10.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc0 for HLS
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc0_HLS.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc0 for YUV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc0_YUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc0 for YCrCb
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc0_YCrCb.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc1 for RGB
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 2.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc1_RGB.p generated in 10.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc1 for HSV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.96.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc1_HSV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc1 for LUV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc1_LUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc1 for HLS
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc1_HLS.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc1 for YUV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc1_YUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc1 for YCrCb
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc1_YCrCb.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc2 for RGB
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc2_RGB.p generated in 10.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc2 for HSV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc2_HSV.p generated in 10.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc2 for LUV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.97.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc2_LUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc2 for HLS
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.96.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc2_HLS.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc2 for YUV
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc2_YUV.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc2 for YCrCb
1856 in training set with feature vector length of 4932
Features extracted in 8.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc2_YCrCb.p generated in 9.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for RGB
1856 in training set with feature vector length of 8460
Features extracted in 17.0 seconds and trained SVC in 2.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_RGB.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for HSV
1856 in training set with feature vector length of 8460
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_HSV.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for LUV
1856 in training set with feature vector length of 8460
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_LUV.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for HLS
1856 in training set with feature vector length of 8460
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_HLS.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for YUV
1856 in training set with feature vector length of 8460
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_YUV.p generated in 19.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for YCrCb
1856 in training set with feature vector length of 8460
Features extracted in 17.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_YCrCb.p generated in 18.0 seconds
Total time 541.0 seconds
[1490211976.438653, 1490211976.4527042, 1490211985.0301905, 1490211985.0309446, 1490211993.3847666, 1490211993.3853335, 1490212002.1934946, 1490212002.1940558, 1490212010.5696406, 1490212010.5702002, 1490212018.8918335, 1490212018.8923934, 1490212027.3874636, 1490212027.399692, 1490212036.0491543, 1490212036.0498023, 1490212044.5901465, 1490212044.5907202, 1490212053.0006979, 1490212053.0012636, 1490212061.4003527, 1490212061.400912, 1490212069.3800502, 1490212069.38059, 1490212077.4687648, 1490212077.4693053, 1490212085.8909652, 1490212085.8915098, 1490212094.3426623, 1490212094.3432026, 1490212102.8635244, 1490212102.8642504, 1490212111.4065483, 1490212111.407087, 1490212119.5149097, 1490212119.5154533, 1490212127.574365, 1490212127.5749114, 1490212146.2223723, 1490212146.223108, 1490212164.5277205, 1490212164.5285723, 1490212183.0467005, 1490212183.0474043, 1490212201.3103244, 1490212201.6771843, 1490212219.4132123, 1490212219.413934, 1490212237.179248, 1490212237.1799617, 1490212247.4981878, 1490212247.4987848, 1490212257.0325425, 1490212257.033315, 1490212266.816682, 1490212266.8175325, 1490212276.0233755, 1490212276.0239239, 1490212285.2511554, 1490212285.2517579, 1490212294.7054777, 1490212294.706029, 1490212304.4283605, 1490212304.4289815, 1490212313.6996474, 1490212313.7002788, 1490212322.7126324, 1490212322.7133482, 1490212332.0314019, 1490212332.0323026, 1490212340.678183, 1490212340.6788971, 1490212349.423426, 1490212349.424155, 1490212358.9475553, 1490212358.9482787, 1490212368.4803016, 1490212368.481173, 1490212377.7748163, 1490212377.775511, 1490212387.0053756, 1490212387.0060205, 1490212395.5739105, 1490212395.5744762, 1490212404.272827, 1490212404.2734365, 1490212423.686701, 1490212423.687477, 1490212442.3461034, 1490212442.3468812, 1490212461.399568, 1490212461.4005334, 1490212480.523523, 1490212480.524289, 1490212499.024581, 1490212499.0253608, 1490212517.3489661, 1490212517.3497174]
