import sys

import cv2 as cv

if len(sys.argv) < 2:
    print("specify an image path")
    quit(1)

image_path = sys.argv[1]
image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

prev_width = image.shape[1]
next_width = 60
resize_ratio = prev_width // next_width
prev_height = image.shape[0]
next_height = prev_height // resize_ratio
image = cv.resize(image, (next_width, next_height))

for row in image:
    for v in row:
        c = "💩" if v < 128 else "　"
        print(c, end='')
    print()
