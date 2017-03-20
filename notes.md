# Vehicle Detection Project Notes

This is my scratch pad for ideas and is not official documentation.

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
|  5  | 1 | 408 | 138x93 | |
|  5  | 2 | 404 | 196x97 | |

## TO DO
 - verify that during training the images are scaled correctly
   because apperently jpeg's and png's are read in at different scales
