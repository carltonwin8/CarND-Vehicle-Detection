# Vehicle Detection Project

The notes for this project are best viewed on line at the
[github repo](https://github.com/carltonwin8/CarND-Vehicle-Dection).
It is easier to follow the link to the source code referenced in this documentation.
This readme is my completion of the Udacity project template provided at
[this repo](https://github.com/udacity/CarND-Vehicle-Dection).

The project code is developed using the
[spyder IDE](https://pythonhosted.org/spyder/)
and is made up of the following files.

  - [detect_vehicles.py](_modules/detect_vehicles.html) -
    The main vehicle detection module.
    The functions used to process various videos while varying some parameters.
  - [gen_output.py](_modules/gen_output.html) -
    Script used during the development and debug phase for visualization
    and used to generate the images used for the documentation.
  - [utils.py](_modules/utils.html)
    and
    [config.py](_modules/config.html)
    Utility procedures and setup information.
  - [lesson_functions.py](_modules/lesson_functions.html) -
    Module containing procedures provide in the
    [Udacity Self-Driving Car Engineer Nanodegree](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013)
    lecture notes.

The following steps are done to complete this project.

  - A Linear SVM classifier is trained on a set of images labeled as car and not-cars.
  - A feature vector made up of the following features is used for training.
      - A Histogram of Oriented Gradients (HOG),
      - A color transform with binned colors
      - A histograms of color
  - The feature vector is normalized and randomized before training and testing.
  - Vehicle are identify in an image by using a sliding-window technique to segment
    the image into blocks that are fed into the trained classifier.
  - The above process is applied to the images in a video stream to identify the cars.
  - A head map identifying the locations of cars by summing all the blocks within
    an image that is identified as a car.
  - The head map is also calculated from the last n fames of the image in order to
    reject outliers and follow detected vehicles.
  - Bounding boxes are drawn around detected vehicles.
  - The above procedure was run on
    [test_video.mp4](test_video.mp4)
    and also on
    [project_video.mp4](project_video.mp4)


# Histogram of Oriented Gradients (HOG)

The
[get_hog_features](_modules/lesson_functions.html#get_hog_features)
function was called in order to generate the HOG images for the
for one of each of the `vehicle` and `non-vehicle` classes.
The
[select_example_images](_modules/gen_output.html#select_example_images)
function was use to select the middle images from the small training data set
in order to get a feel for what the `skimage.hog()` output looks like.
The
[gen_hog](_modules/gen_output.html#gen_hog)
function called the
[get_hog_features](_modules/lesson_functions.html#get_hog_features)
function, noted above, with the default values show in the
[params.hog](_modules/config.html#params.hog)
configuration.

Here is an example using the `YCrCb` color space and HOG parameters of `orientations=8`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:

<table width="100%">
<tr width="100%">
  <th align="center">Car</th>
  <th align="center">Car HOG</th>
  <th align="center">Not Car</th>
  <th align="center">Not Car HOG</th>
</tr>
<tr width="100%">
  <td width="23%"><img src="output_images/vehicles_smallset_cars1_183.jpeg" width="100%" ></td>
  <td width="23%"><img src="output_images/vehicles_smallset_cars1_183_hog.jpeg" width="100%"></td>
  <td width="23%"><img src="output_images/non-vehicles_smallset_notcars1_extra511.jpeg" width="100%"></td>
  <td width="23%"><img src="output_images/non-vehicles_smallset_notcars1_extra511_hog.jpeg" width="100%"></td>
</tr>
</table>

I started by reading in all the `vehicle` and `non-vehicle` images.
I then explored different color spaces and different `skimage.hog()`
parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).

#### 2. Explain how you settled on your final choice of HOG parameters.

I tried various combinations of parameters and...

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I trained a linear SVM using...

###Sliding Window Search

####1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

I decided to search random window positions at random scales all over the image and came up with this (ok just kidding I didn't actually ;):

![alt text][image3]

####2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

Ultimately I searched on two scales using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result.  Here are some example images:

![alt text][image4]
---

### Video Implementation

####1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./project_video.mp4)


####2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  

Here's an example result showing the heatmap from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:

### Here are six frames and their corresponding heatmaps:

![alt text][image5]

### Here is the output of `scipy.ndimage.measurements.label()` on the integrated heatmap from all six frames:
![alt text][image6]

### Here the resulting bounding boxes are drawn onto the last frame in the series:
![alt text][image7]



---

###Discussion

####1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  

## CJ Notes To add

 - Did not make use small boxes for scanning for cars because that
   means they are far away and are not a immediate concern
