import cv2
import numpy as np

img = cv2.imread('Ishihara_s.jpg')
img = cv2.resize(img,(300,300))

kernel = np.ones((5,5), np.uint8)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
# imgCanny = cv2.Canny(img, 200,200) #numeros opcionales, pueden variar
# imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
# imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)
B, G, R = cv2.split(img)

# cv2.imshow('GRAY', imgGray)
# cv2.imshow('BLUR', imgBlur)
# cv2.imshow('CANNY', imgCanny)
# cv2.imshow('DILATION', imgDilation)
# cv2.imshow('ERODED', imgEroded)

cv2.imshow('ORIGINAL', img)
cv2.imshow('EXTRACT', R)

cv2.waitKey(0)
