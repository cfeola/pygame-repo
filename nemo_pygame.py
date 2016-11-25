
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
# time = 100 
# pygame.time.set_timer(pygame.KEYDOWN + 1, 1000)

gameExit = False

fish_img = pygame.image.load('fish.gif')
fish_img = pygame.transform.scale(fish_img, (100,50))

background_img = pygame.image.load('Anemone.jpg')
backgroundRect = background_img.get_rect()

size = (width, height) = background_img.get_size()
screen = pygame.display.set_mode(size)

nemo_img = pygame.image.load('nemo3.gif')
nemo_img = pygame.transform.scale(nemo_img, (55,40))

bruce_img = pygame.image.load('bruce_shark.gif')
bruce_img = pygame.transform.scale(bruce_img, (200,110))

def fish(x,y):
	gameDisplay.blit(fish_img, (x,y))

def shark(a,b):
	gameDisplay.blit(bruce_img, (a,b))

x = 70
y = 50

a = 500
b = 0

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

		# elif event.type == pygame.KEYDOWN + 1:
		# 	time -= 1

		# elif time == 0:
		# 	gameExit == True

	x_delta = 0;
	y_delta = 0;
	
	a_delta = 0;
	b_delta = 0;

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_delta -= 10
			a_delta += 20
		if event.key == pygame.K_RIGHT:
			x_delta += 10
			a_delta -= 20
		if event.key == pygame.K_UP:
			y_delta -= 10
			b_delta -= 20
		if event.key == pygame.K_DOWN:
			y_delta += 10
			b_delta += 20
    
 
	x += x_delta
	y += y_delta
    
	a += a_delta
	b += b_delta

	gameDisplay.fill(white)
	
	screen.blit(background_img, backgroundRect)
	screen.blit(nemo_img, (620,310))
	#screen.blit(bruce_img, (500,0))
	fish(x,y)
	shark(a,b)
	
	pygame.display.update()
	clock.tick(25)

pygame.quit()
quit()