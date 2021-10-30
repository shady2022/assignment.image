import cv2

person = cv2.imread('ostad.jpg', 0)

for i in range(300):
    if i <= 150:
        for j in range(150-i, 300-i):
            if (j >= 0):
                person[i, j] = 0
    else:
        for j in range(0, 300-i):
            if (j >= 0):
                person[i, j] = 0
    
cv2.imwrite('ostad.jpg', person)
cv2.imshow('m', person)
cv2.waitKey()