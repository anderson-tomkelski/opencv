import cv2, numpy as np

# B = 0, G = 0, R = 255
#image = np.full((480, 640, 3), (0, 0, 255), np.uint8)
# BGR = 255
image = np.full((480, 640, 3), 255, np.uint8)
# BGR = 0
image.fill(0)
# Set pixels
image[240, 160] = image[240, 320] = image[240, 480] = (255, 255, 255)
image[:, :, 0] = 255
image[:, 320, :] = 255
image[100:600, 100:200, 2] = 255
cv2.imshow('white', image)
cv2.waitKey()
cv2.destroyAllWindows()
