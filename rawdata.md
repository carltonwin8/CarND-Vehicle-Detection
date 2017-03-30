```


../test_images/test1.jpg
1.7 Seconds to process ../test_images/test1.jpg with s_ssahb16_hc3_YCrCb.p and ss (True)
[((0, 400), (64, 464)), ((0, 416), (64, 480)), ((0, 432), (64, 496)), ((0, 448), (64, 512)), ((0, 464), (64, 528))]
[((0, 416), (64, 480)), ((80, 432), (144, 496)), ((128, 400), (192, 464)), ((144, 400), (208, 464)), ((160, 400), (224, 464))]
6.5 Seconds to process ../test_images/test1.jpg with s_ssahb16_hc3_YCrCb.p and ss (False)
[((0, 400), (100, 500)), ((0, 425), (100, 525)), ((0, 450), (100, 550)), ((0, 475), (100, 575)), ((0, 500), (100, 600))]
[((0, 400), (100, 500)), ((0, 425), (100, 525)), ((0, 525), (100, 625)), ((0, 550), (100, 650)), ((25, 400), (125, 500))]
8.2 Seconds to process 1 images
../test_images/test1.jpg
1.7 Seconds to process ../test_images/test1.jpg with s_ssahb32_hc3_YCrCb.p and ss (True)
[((0, 400), (64, 464)), ((0, 416), (64, 480)), ((0, 432), (64, 496)), ((0, 448), (64, 512)), ((0, 464), (64, 528))]
[((0, 416), (64, 480)), ((80, 432), (144, 496)), ((128, 400), (192, 464)), ((144, 400), (208, 464)), ((160, 400), (224, 464))]
6.6 Seconds to process ../test_images/test1.jpg with s_ssahb32_hc3_YCrCb.p and ss (False)
[((0, 400), (100, 500)), ((0, 425), (100, 525)), ((0, 450), (100, 550)), ((0, 475), (100, 575)), ((0, 500), (100, 600))]
[((0, 400), (100, 500)), ((0, 425), (100, 525)), ((0, 525), (100, 625)), ((0, 550), (100, 650)), ((25, 400), (125, 500))]
8.3 Seconds to process 1 images
16.6 Seconds for 1 image in [3], [16, 32], ['YCrCb'].

1.6 Seconds to process ../test_images/test1.jpg with b_ssahb16_hc3_YCrCb.p and ss (True)
[((0, 400), (64, 464)), ((0, 416), (64, 480)), ((0, 432), (64, 496)), ((0, 448), (64, 512)), ((0, 464), (64, 528))]
[((832, 432), (896, 496)), ((864, 400), (928, 464))]
6.4 Seconds to process ../test_images/test1.jpg with b_ssahb16_hc3_YCrCb.p and ss (False)
[((0, 400), (100, 500)), ((0, 425), (100, 525)), ((0, 450), (100, 550)), ((0, 475), (100, 575)), ((0, 500), (100, 600))]
[((800, 400), (900, 500)), ((825, 400), (925, 500)), ((825, 425), (925, 525)), ((850, 400), (950, 500)), ((1050, 400), (1150, 500))]
8.1 Seconds to process 1 images
../test_images/test1.jpg
1.7 Seconds to process ../test_images/test1.jpg with b_ssahb32_hc3_YCrCb.p and ss (True)
[((0, 400), (64, 464)), ((0, 416), (64, 480)), ((0, 432), (64, 496)), ((0, 448), (64, 512)), ((0, 464), (64, 528))]
[((832, 432), (896, 496)), ((864, 400), (928, 464)), ((832, 400), (896, 464)), ((832, 416), (896, 480)), ((848, 432), (912, 496))]
6.7 Seconds to process ../test_images/test1.jpg with b_ssahb32_hc3_YCrCb.p and ss (False)
[((0, 400), (100, 500)), ((0, 425), (100, 525)), ((0, 450), (100, 550)), ((0, 475), (100, 575)), ((0, 500), (100, 600))]
[((800, 400), (900, 500)), ((825, 400), (925, 500)), ((825, 425), (925, 525)), ((850, 400), (950, 500)), ((1050, 400), (1150, 500))]
8.4 Seconds to process 1 images
16.4 Seconds for 1 image in [3], [16, 32], ['YCrCb'].


>>> runfile('/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src/detect_vehicles.py', args='-d big -c 18 train', wdir='/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src')
big data set with 8792 car & 8968 not cars, trained for ssahb16, hogc3 for YCrCb
14208 in training set with feature vector length of 6108
Features extracted in 151.0 seconds and trained SVC in 8.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
b_ssahb16_hc3_YCrCb.p generated in 162.0 seconds
Total time 162.0 seconds
[1490827396.027615, 1490827396.1296704, 1490827558.2315042, 1490827558.2323978]
>>> runfile('/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src/detect_vehicles.py', args='-d big -c 16 train', wdir='/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src')
Reloaded modules: lesson_functions, config, utils
big data set with 8792 car & 8968 not cars, trained for ssahb32, hogc3 for RGB
14208 in training set with feature vector length of 8460
Features extracted in 150.0 seconds and trained SVC in 43.0 with accuracy 0.98.
Using 9 orientations 8 pixels per cell and 2 cells per block
b_ssahb32_hc3_RGB.p generated in 197.0 seconds
Total time 197.0 seconds
[1490827594.4689891, 1490827594.5844588, 1490827791.3692775, 1490827791.7536108]
>>> runfile('/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src/detect_vehicles.py', args='-d big -c 18 train', wdir='/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src')
Reloaded modules: lesson_functions, config, utils
big data set with 8792 car & 8968 not cars, trained for ssahb16, hogc3 for YCrCb
14208 in training set with feature vector length of 6108
Features extracted in 150.0 seconds and trained SVC in 24.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
b_ssahb16_hc3_YCrCb.p generated in 177.0 seconds
Total time 177.0 seconds
[1490828098.1085892, 1490828098.213524, 1490828275.0664296, 1490828275.0671985]
>>> runfile('/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src/detect_vehicles.py', args='-d big -c 15 train', wdir='/home/carltonj2000/cj/mounts/local/cj1Tera2/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCar/lecture20_assignment/CarND-Vehicle-Detection/src')

Reloaded modules: lesson_functions, config, utils
big data set with 8792 car & 8968 not cars, trained for ssahb32, hogc3 for YCrCb
14208 in training set with feature vector length of 8460
Features extracted in 151.0 seconds and trained SVC in 34.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
b_ssahb32_hc3_YCrCb.p generated in 189.0 seconds
Total time 189.0 seconds
[1490828438.4015892, 1490828438.514898, 1490828627.0547562, 1490828627.0559998]

small data set with 1196 car & 1125 not cars, trained for ssahb16, hogc3 for YCrCb
1856 in training set with feature vector length of 6108
Features extracted in 19.0 seconds and trained SVC in 1.0 with accuracy 1.0.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb16_hc3_YCrCb.p generated in 20.0 seconds
small data set with 1196 car & 1125 not cars, trained for ssahb32, hogc3 for YCrCb
1856 in training set with feature vector length of 8460
Features extracted in 19.0 seconds and trained SVC in 1.0 with accuracy 0.99.
Using 9 orientations 8 pixels per cell and 2 cells per block
s_ssahb32_hc3_YCrCb.p generated in 20.0 seconds
Total time 40.0 seconds
[1490828856.0732548, 1490828856.0940971, 1490828875.8188405, 1490828875.8195126, 1490828895.8067007, 1490828895.807323]


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

```
