import cv2

img = cv2.imread('./louvre.jpeg')
print('shape:', img.shape)
print('dtype:', img.dtype)

resized_img = cv2.resize(img, (128, 256))
resized_img = cv2.resize(img, (0, 0), resized_img, 0.25, 0.5)
resized_img = cv2.resize(img, (0, 0), resized_img, 2, 4, cv2.INTER_NEAREST)
print('resized to 128x256 image shape:', resized_img.shape)
img_flip_along_x = cv2.flip(img, 0)

orig_size = img.shape[0:2]
cv2.imshow("orig", img)
cv2.imshow("filp", img_flip_along_x)
cv2.waitKey(2000)

#cv2.imwrite('teste.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
#saved_img = cv2.imread('teste.png')
#assert saved_img.all() == img.all()
