
import pygame
import sys

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Finding Nemo')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
gameExit = False
fish_img = pygame.image.load('fish.gif')
fish_img = pygame.transform.scale(fish_img, (100,50))
background_img = pygame.image.load('Anemone.jpg')
backgroundRect = background_img.get_rect()
size = (width, height) = background_img.get_size()
screen = pygame.display.set_mode(size)

def fish(x,y):
	gameDisplay.blit(fish_img, (x,y))

x =  (display_width * 0.1)
y = (display_height * 0.1)


while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	x_delta=0;
	y_delta=0;
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
    
 
	x += x_delta
	y += y_delta
          
	gameDisplay.fill(white)
	
	screen.blit(background_img, backgroundRect)
	fish(x,y)
        
	pygame.display.update()
	clock.tick(25)

pygame.quit()
quit()