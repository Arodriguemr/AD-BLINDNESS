import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 

    height, width, _ = frame.shape
    # dividir pantalla
    cx = int(width/2)
    cy = int(height/2)
    # tomar valor con puntero
    puntero = hsv[cy, cx]
    hue_value = puntero[0]

    # definir rango de colores

    color = "Indefinido"
    if hue_value < 5:
        color = "ROJO"

    elif hue_value > 22 and hue_value < 33:
        color = "AMARILLO"
    
    elif hue_value > 33 and hue_value < 78:
        color = "VERDE"

    elif hue_value > 78 and hue_value < 131:
        color = "AZUL"    

    else:
        color = "ROJO"

    B, G, R = int(puntero[0]), int(puntero[1]), int(puntero[2])
    cv2.putText(frame, color, (50, 100), 5, 3,(B, G, R), 2)
    cv2.circle(frame, (cx, cy), 5, (50, 50, 50), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

























