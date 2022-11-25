import pygame
from pygame import QUIT, K_LEFT, K_RIGHT, K_UP, K_SPACE

hahaha = False
screen = pygame.display.set_mode((600, 600))
negro = (0, 0, 0)
verde = (0, 255, 0)
blanco = (255,255,255)
personaje = pygame.Rect((0, 0, 30, 30))
dy = 0
x = 40
y = 200
GRAVEDAD = 0.02
pos_suelo = 400

while not hahaha:
    for e in pygame.event.get():
        if e.type == QUIT:
            hahaha = True
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
        x -= 1
    elif key[K_RIGHT]:
        x += 1
         
    if dy == 0:
        if key[K_SPACE] or key[K_UP]:
            dy -= 2
    else:
        y += dy
        dy += GRAVEDAD
        if y > pos_suelo:
            dy = 0
            y = pos_suelo
    
    personaje.bottom = int(y)
    personaje.centerx = int(x)
    screen.fill(negro)
    pygame.draw.line(screen, blanco, (0, 400), (600, 400))
    screen.fill(verde, personaje)
    pygame.display.flip()
    pygame.time.wait(2)