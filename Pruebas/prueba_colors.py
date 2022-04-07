import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

# Convierte de RGB a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


#############-- SEMAFORO --#############
# Color Rojo
    lower_red = np.array([161, 155, 84], np.uint8)
    upper_red = np.array([179, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

# Color Verde
    lower_green = np.array([25, 52, 72], np.uint8)
    upper_green = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

# Color Azul 
    lower_blue = np.array([94, 80, 2], np.uint8)
    upper_blue = np.array([126, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

# All Colors
    lower_color = np.array([0, 42, 0], np.uint8)
    upper_color = np.array([179, 255, 255], np.uint8)
    color_mask = cv2.inRange(hsv, lower_color, upper_color)
    colors = cv2.bitwise_and(frame, frame, mask=color_mask)


    cv2.imshow('frame', frame)
    cv2.imshow('Result', colors)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
