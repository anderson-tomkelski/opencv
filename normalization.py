# When we set 0 for mean value of values and 1 for variance, the operation is called normalization
# This can be useful in computer vision algorithms for dealing with values with a certain range and with certain statistics.

import cv2
import numpy as np

image = cv2.imread('louvre.jpeg').astype(np.float32) / 255
image -= image.mean()
image /= image.std()

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()
