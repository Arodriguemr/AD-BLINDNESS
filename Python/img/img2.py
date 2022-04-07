import cv2
import numpy as np
import imutils

Low_red1 = np.array([0,140,90], np.uint8)
Hight_red1 = np.array([8,255,255], np.uint8)

Low_red2 = np.array([160,140,90], np.uint8)
Hight_red2 = np.array([180,255,255], np.uint8)

img = cv2.imread('Ishihara_3.jpg')
img = imutils.resize(img, width= 350)

# Llevar a otros colores
Gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Detectar Rojo
Red_mask1 = cv2.inRange(HSV_img, Low_red1, Hight_red1)
Red_mask2 = cv2.inRange(HSV_img, Low_red2, Hight_red2)
Final_mask = cv2.add(Red_mask1, Red_mask2)
Final_mask = cv2.medianBlur(Final_mask, 1)
Final_mask = cv2.bitwise_and(img, img, mask = Final_mask)


cv2.imshow('Original', img)
cv2.imshow('Final Mask', Final_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()