import cv2

img = cv2.imread("1.jpg")
#img = cv2.imread("2.jpg")


rows = img.shape[0]
cols = img.shape[1]
print(img)


for i in range(rows):
    for j in range(cols):
        img[i, j]=255 - img[i, j]



cv2.imshow("behtar shod!", img)
cv2.waitKey()
 