import cv2
import numpy as np


cap= cv2.VideoCapture(0)

def nix(x):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 500, 240)
cv2.createTrackbar('HUE Min', 'HSV', 0, 179, nix)
cv2.createTrackbar('HUE Max', 'HSV', 179, 179, nix)
cv2.createTrackbar('SAT Min', 'HSV', 0, 255, nix)
cv2.createTrackbar('SAT Max', 'HSV', 255, 255, nix)
cv2.createTrackbar('VAL Min', 'HSV', 0, 255, nix)
cv2.createTrackbar('VAL Max', 'HSV', 255, 255, nix)


while True:

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)

    cv2.imshow('Original', img)
    cv2.imshow('HSV', imgHsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
