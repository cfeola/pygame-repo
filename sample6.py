#Frames per second manipulation

#required 
import pygame
pygame.init();

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Frames per second")
def redraw():
	gameDisplay.fill(white)
	gameDisplay.fill(green, rect=[100,100, 40,40])
	pygame.draw.circle(gameDisplay, blue, (50,100), 20, 0)
	pygame.draw.circle(gameDisplay, black, (200,200),20, 0)
	pygame.draw.lines(gameDisplay, black, False, [(100,100), (150,200), (200,100)], 1)

pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
	gameDisplay.fill(white)
	redraw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
	
	x_pos +=x_delta
	y_pos +=y_delta
	gameDisplay.fill(red, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()		
	clock.tick(25)



#required
pygame.quit()
quit()				#exits python