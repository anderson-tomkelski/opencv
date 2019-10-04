import cv2
import numpy as np
import matplotlib.pyplot as plt

grey = cv2.imread('louvre.jpeg', 0)

hist, bins = np.histogram(grey, 256, [0, 255])
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

#cv2.imshow('original grey', grey)
#cv2.waitKey()
#cv2.destroyAllWindows()
