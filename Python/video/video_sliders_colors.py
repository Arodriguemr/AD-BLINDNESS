# Codificacion de colores con HSV
# Hue: codifica la tonalidad del color de -> Rojo, Amarillo y Verde.
# Saturation: codifica la pureza del color, entre mayor sea el color mas puro es.
# Value: codifica la luminosidad, entre menor sea mas oscuro es el color

import cv2
import numpy as np

# En caso de no detectar colores:
def nix(x):
    pass

# Creacion de ventana con Sliders:
cv2.namedWindow('Parameters')
cv2.resizeWindow('Parameters', 300, 300)

# Crear Slider para H
cv2.createTrackbar('Minimal Hue', 'Parameters', 0, 179, nix)
cv2.createTrackbar('Maximal Hue', 'Parameters', 0, 179, nix)

# Crear Slider para S
cv2.createTrackbar('Minimal Saturation', 'Parameters', 0, 255, nix)
cv2.createTrackbar('Maximal Saturation', 'Parameters', 0, 255, nix)

# Crear Slider para V (Value = Luminosidad)
cv2.createTrackbar('Minimal Value', 'Parameters', 0, 255, nix)
cv2.createTrackbar('Maximal Value', 'Parameters', 0, 255, nix)

# Crear filtro Kernel: Suaviza los pixeles en caso de tener impuresas en los colores (reflejos de la luz que pueden hacer aparecer pixeles blancos)
cv2.createTrackbar('Kernel X', 'Parameters', 1, 30, nix)
cv2.createTrackbar('Kernel Y', 'Parameters', 1, 30, nix)

# Crear Video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
        # ret: almacena la lectura de imagen si se esta haciendo bien
        # frame: almacena fotogramas
    font = cv2.FONT_HERSHEY_SIMPLEX
    if ret: 
        # Con esto convertimos de RGB a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Leer posicion de los Sliders H, S, V
        Min_Hue = cv2.getTrackbarPos('Minimal Hue', 'Parameters')
        Max_Hue = cv2.getTrackbarPos('Maximal Hue', 'Parameters')

        Min_Saturation = cv2.getTrackbarPos('Minimal Saturation', 'Parameters')
        Max_Saturation = cv2.getTrackbarPos('Maximal Saturation', 'Parameters')

        Min_Value = cv2.getTrackbarPos('Minimal Value', 'Parameters')
        Max_Value = cv2.getTrackbarPos('Maximal Value', 'Parameters')

        Min_Value = cv2.getTrackbarPos('Minimal Value', 'Parameters')
        Max_Value = cv2.getTrackbarPos('Maximal Value', 'Parameters')

        # Establecer rangos minimos y maximos
        dark_color = np.array([Min_Hue, Min_Saturation, Min_Value])
        bright_color = np.array([Max_Hue, Max_Saturation, Max_Value])


        # Detectar pixeles que esten entre los rangos anteriores
        mask = cv2.inRange(hsv, dark_color, bright_color)


        # Mostrar en Rojo
        Red_mask = cv2.bitwise_and(frame, frame, mask = mask)
        Yellow_mask = cv2.bitwise_and(frame, frame, mask = mask)
        Green_mask = cv2.bitwise_and(frame, frame, mask = mask)
        #Three_Colors = Red_mask, Yellow_mask, Green_mask 


        # Slide Filtro/Kernel
        kernel_X = cv2.getTrackbarPos('Kernel X', 'Parameters')
        kernel_Y = cv2.getTrackbarPos('Kernel Y', 'Parameters')

        # Filtro de Suavizado
        kernel = np.ones((kernel_X, kernel_Y), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)



        # Crear contorno de los objetos
            # RETR_LIST guarda los contornos
            # CHAIN_APPROX_SIMPLE metodo de aproximacion de contorno eliminando redundacias, quitando pixeles redundantes
        outline, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, outline, -1, (0,0,0), 2)

        # Monstrar la imagen de camara y las mascaras creadas
        cv2.imshow('Original Camera', frame)
        cv2.imshow('Camera 2', mask)
        cv2.imshow('Red Mask Camera', Red_mask)
        cv2.imshow('Yellow Mask Camera', Yellow_mask)
        cv2.imshow('Green Mask Camera', Green_mask)
        #cv2.imshow('Three Colors', Three_Colors)

        #Cerrar aplicacion
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break
cap.release()