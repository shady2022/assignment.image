import cv2

image = cv2.imread("3.jpg")
rows, cols = image.shape[ : 2]

m = cv2.getRotationMatrix2D((cols /2, rows /2), 180, 1)
rotate = cv2.warpAffine (image, m, (cols, rows))


cv2.imshow(" ", rotate)
cv2.waitKey()

#import imutils
#imutils.rotate_bound(image, 180)