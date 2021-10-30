import cv2
import numpy as np

paper = np.zeros ([400, 400, 3], dtype= np.uint8)
flag = True
row,col= paper.shape
W=paper.shape[0]//8
h=paper.shape[1]//8
for i in range(0,paper.shape[0],W):
    for j in range(0,paper.shape[1],h):
        if  flag ==False :
            paper[i:i+W,j:j+h]=255
            flag=True
        else:
            paper[i:i+W,j:j+h] = 0
            flag= False
    if flag:
        flag=False
    else:
        flag =True
cv2.imshow('1',paper)
cv2.waitKey()