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
