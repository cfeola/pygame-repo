
import pygame

pygame.init()

pygame.display.set_caption('Finding Nemo')

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

sharkbite = pygame.mixer.Sound("chomp.wav")
find_nemo = pygame.mixer.Sound("yay.wav")
# pygame.mixer.music.play(-1)

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

# time = 100 
# pygame.time.set_timer(pygame.KEYDOWN + 1, 1000)

class Marlin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('fish.gif')
		self.image = pygame.transform.scale(self.image, (100,50))
		self.rect = self.image.get_rect()
		self.rect.x = 70
		self.rect.y = 50

class Bruce(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('bruce_shark.gif')
		self.image = pygame.transform.scale(self.image, (200,110))
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y = 0

class Nemo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('nemo3.gif')
		self.image = pygame.transform.scale(self.image, (55,40))
		self.rect = self.image.get_rect()
		self.rect.x = 620
		self.rect.y = 310


background_img = pygame.image.load('Anemone.jpg')
backgroundRect = background_img.get_rect()
size = (width, height) = background_img.get_size()
screen = pygame.display.set_mode(size)


sprite_group = pygame.sprite.Group()

# Create Marlin 
Marlin = Marlin()
sprite_group.add(Marlin)

# Create Bruce 
Bruce = Bruce()
sprite_group.add(Bruce)

# Create Nemo
Nemo = Nemo()
sprite_group.add(Nemo)

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	sprite_group.update()
	

	if event.type == pygame.KEYDOWN:
		
		if event.key == pygame.K_LEFT and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			Marlin.rect.x -= 10
			Bruce.rect.x += 20
			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				print("GAME OVER")
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				print("YOU FOUND NEMO!")


		if event.key == pygame.K_RIGHT and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			Marlin.rect.x += 10
			Bruce.rect.x -= 20
			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				print("GAME OVER")
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				print("YOU FOUND NEMO!")

		if event.key == pygame.K_UP and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			Marlin.rect.y -= 10
			Bruce.rect.y -= 20
			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				print("GAME OVER")
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				print("YOU FOUND NEMO!")

		if event.key == pygame.K_DOWN and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			Marlin.rect.y += 10
			Bruce.rect.y += 20	
			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				print("GAME OVER")
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				print("YOU FOUND NEMO!")
	

	screen.blit(background_img, backgroundRect)
	
	sprite_group.draw(screen)
	
	pygame.display.flip()

	# hit = pygame.sprite.spritecollide(fish_img, bruce_img, True)
	# if hit:
	# 	gameExit = True

	pygame.display.update()
	clock.tick(25)

pygame.quit()
quit()