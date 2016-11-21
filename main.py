#! /usr/bin/python
import pygame

deepblue = (26, 0, 255)
mintcream = (254, 255, 250)

pygame.init()
size = (500, 500)
surface = pygame.display.set_mode(size)

surface.fill(deepblue)
position = (250, 250)
radius = 50
linewidth = 2

pygame.draw.circle (surface, mintcream, position, radius, linewidth)


position = (280, 300)
radius = 80
linewidth = 2

pygame.draw.circle (surface, mintcream, position, radius, linewidth)

pygame.display.update()

for event in pygame.event.get(): print (event)
