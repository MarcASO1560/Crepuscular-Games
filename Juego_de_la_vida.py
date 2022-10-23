#Importaciones de codigo.
import pygame
import numpy as np
import time
import math
from pygame.constants import K_SPACE
#Preparación de espacio en pantalla.
Bucle=True
espacio=largo,alto=1000,1000
CeldasX=140
CeldasY=140
DimensionX=(largo-1)/CeldasX
DimensionY=(alto-1)/CeldasY
ColorFondo=25,25,25
#Preparando el estado del juego con numpy.
Estado_de_juego=np.zeros((CeldasX,CeldasY))
#Utilización de pygame para generar la ventana del espacio.
ventana=pygame.display.set_mode(espacio)
ventana.fill(ColorFondo)
Pausa=False
#Funcionamiento del bucle.
while Bucle:
#El fondo de la ventana va a ser el explicado en las variables.
    ventana.fill(ColorFondo)
#Botones.
    Nuevo_estado_de_juego=np.copy(Estado_de_juego)
    Evento_Boton=pygame.event.get()
    for event in Evento_Boton:
    #Botón de pausa.
        Presionado=pygame.key.get_pressed()
        if event.type==pygame.KEYDOWN and Presionado[K_SPACE]:
            Pausa=not Pausa
    #Botón de salida.
        if event.type==pygame.QUIT:
            quit()
    #Botón para pintar y borrar.
        Click_Raton=pygame.mouse.get_pressed()
        if sum(Click_Raton)>0:
            PosicionX,PosicionY=pygame.mouse.get_pos()
            if PosicionX>0 and PosicionX<largo-1 and PosicionY>0 and PosicionY<alto-1:
                Nuevo_estado_de_juego[math.floor(PosicionX/DimensionX),math.floor(PosicionY/DimensionY)]=Click_Raton[0] and not Click_Raton[2]
#Estructura del juego.
    for x in range(0,CeldasY):
        for y in range(0,CeldasX):
            if not Pausa:
    #Explicación de la acción según las celdas del entorno de la celda principal.
                Celda_vecina=Estado_de_juego[(x-1)%CeldasX,(y-1)%CeldasY]+\
                            Estado_de_juego[(x)%CeldasX,(y-1)%CeldasY]+\
                            Estado_de_juego[(x+1)%CeldasX,(y-1)%CeldasY]+\
                            Estado_de_juego[(x-1)%CeldasX,(y)%CeldasY]+\
                            Estado_de_juego[(x+1)%CeldasX,(y)%CeldasY]+\
                            Estado_de_juego[(x-1)%CeldasX,(y+1)%CeldasY]+\
                            Estado_de_juego[(x)%CeldasX,(y+1)%CeldasY]+\
                            Estado_de_juego[(x+1)%CeldasX,(y+1)%CeldasY]
                if Estado_de_juego[x,y]==0 and Celda_vecina==3:
                    Nuevo_estado_de_juego[x,y]=1
                elif Estado_de_juego[x,y]==1 and (Celda_vecina<2 or Celda_vecina>3):
                    Nuevo_estado_de_juego[x,y]=0
    #Explicación de los vectores que conforman la cuadricula.
            Cuadricula=[((x)*DimensionX,(y)*DimensionY),
                        ((x+1)*DimensionX,(y)*DimensionY),
                        ((x+1)*DimensionX,(y+1)*DimensionY),
                        ((x)*DimensionX,(y+1)*DimensionY)]
            if Nuevo_estado_de_juego[x,y]==0:
                pygame.draw.polygon(ventana,(0,64,0),Cuadricula,1)
            else:
                pygame.draw.polygon(ventana,(0,255,0),Cuadricula,0)
    #Hacer que los calculos se representen en pantalla y que dure un tiempo delimitado.
    Estado_de_juego=np.copy(Nuevo_estado_de_juego)
    pygame.display.flip()
    time.sleep(0.001)