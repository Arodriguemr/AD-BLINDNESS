from re import S
from cv2 import VideoCapture
import numpy as np
import cv2 
import numpy as np

def nix(x):
    pass

#Trackbar
cv2.namedWindow('PRUEBA-4')

cv2.createTrackbar("H", "PRUEBA-4", 0, 179, nix)
cv2.createTrackbar("S", "PRUEBA-4", 255, 255, nix)
cv2.createTrackbar("V", "PRUEBA-4", 255, 255, nix)

hsv = np.zeros((250,500,3), np.uint8)

while True:
    h = cv2.getTrackbarPos('H', 'PRUEBA-4')
    s = cv2.getTrackbarPos('S', 'PRUEBA-4')
    v = cv2.getTrackbarPos('V', 'PRUEBA-4')

    hsv[:] = (h,s,v)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("PRUEBA-4", bgr)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()






















