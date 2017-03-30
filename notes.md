# Vehicle Detection Project Notes

This is my scratch pad for ideas and is not official documentation.

## Stats

big data set has 8792 car & 8968 not cars,
small data set has 1196 car & 1125 not cars

  - Color space is YCrCb with all channels.
  - HS is the hist_bins and spatial_size
  - orientation = 9
  - SS is sub-sampling the hog of a full image
  - Detection times measure for test1.jpg

| Train Total | Extract | Train | Train Data | HS | Accuracy | Detect SS | Detect NSS | Machine  |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 20 | 19 | 1 | small | 16 | 1.00 | 1.7 | 6.5 | workstation |
| 20 | 19 | 1 | small | 32 | 0.99 | 1.7 | 6.6 | workstation |
| 162 | 150 | 8 | big | 16 | 0.99 | 1.6 | 6.4 | workstation |
| 189 | 151 | 34 | big | 32 | 0.99 | 1.7 | 6.7 | workstation |

## Brain Storming

The parameter that I settled on are:
  - orientation = 9
  - hist_bins = 32
  - spatial_size = (32, 32)
  - train big data set


### TO DO
  - create all the visualization images

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
