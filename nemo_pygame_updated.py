
import pygame

pygame.init()

pygame.display.set_caption('Finding Nemo')

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

background_music = pygame.mixer.Sound("Just-keep-swimming-swimming-swimming_2_.wav")
sharkbite = pygame.mixer.Sound("chomp.wav")
find_nemo = pygame.mixer.Sound("yay.wav")

black = (0,0,0)
white = (255,255,255)

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
frame_count = 0 
frame_rate = 25
start_time = 5

class Marlin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('fish.bmp')
		self.image = pygame.transform.scale(self.image, (100,50))
		self.rect = self.image.get_rect()
		self.rect.x = 70
		self.rect.y = 50

class Bruce(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('bruce_shark.bmp')
		self.image = pygame.transform.scale(self.image, (200,110))
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y = 0

class Nemo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('nemo3.bmp')
		self.image = pygame.transform.scale(self.image, (55,40))
		self.rect = self.image.get_rect()
		self.rect.x = 620
		self.rect.y = 310

class Dory(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('Dory.bmp')
		self.image = pygame.transform.scale(self.image, (70,70))
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y = 290

background_img = pygame.image.load('Anemone.bmp')
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

# Create Dory 
Dory = Dory()
sprite_group.add(Dory)

gameExit = False

pygame.mixer.Sound.play(background_music, loops = -1)

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	sprite_group.update()
	
	if event.type == pygame.KEYDOWN:
		
		if event.key == pygame.K_LEFT and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			if Bruce.rect.x > width:
				Bruce.rect.x = 500
				Bruce.rect.y = 0
			elif Marlin.rect.x < -60:
				Marlin.rect.x = 70
				Marlin.rect.y = 50
			else:
				Marlin.rect.x -= 10
				Bruce.rect.x += 20

			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				font = pygame.font.SysFont(None, 75)
				game_over_string = "GAME OVER"
				game_over_text = font.render(game_over_string, True, white)
				screen.blit(game_over_text, [200,150])
				pygame.display.flip()
				print("GAME OVER")
				exit()
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				font = pygame.font.SysFont(None, 75)
				you_found_nemo_string = "YOU FOUND NEMO!"
				you_found_nemo_text = font.render(you_found_nemo_string, True, white)
				screen.blit(you_found_nemo_text, [100,150])
				pygame.display.flip()
				print("YOU FOUND NEMO!")
				exit()

		if event.key == pygame.K_RIGHT and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			if Bruce.rect.x < -120:
				Bruce.rect.x = 500
				Bruce.rect.y = 0
			elif Marlin.rect.x > width:
				Marlin.rect.x = 70
				Marlin.rect.y = 50
			else:
				Marlin.rect.x += 10
				Bruce.rect.x -= 20

			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				font = pygame.font.SysFont(None, 75)
				game_over_string = "GAME OVER"
				game_over_text = font.render(game_over_string, True, white)
				screen.blit(game_over_text, [200,150])
				pygame.display.flip()
				print("GAME OVER")
				exit()
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				font = pygame.font.SysFont(None, 75)
				you_found_nemo_string = "YOU FOUND NEMO!"
				you_found_nemo_text = font.render(you_found_nemo_string, True, white)
				screen.blit(you_found_nemo_text, [100,150])
				pygame.display.flip()
				print("YOU FOUND NEMO!")
				exit()

		if event.key == pygame.K_UP and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			if Bruce.rect.y < -120:
				Bruce.rect.x = 500
				Bruce.rect.y = 0
			elif Marlin.rect.y < -60:
				Marlin.rect.x = 70
				Marlin.rect.y = 50				
			else:
				Marlin.rect.y -= 10
				Bruce.rect.y -= 20

			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				font = pygame.font.SysFont(None, 75)
				game_over_string = "GAME OVER"
				game_over_text = font.render(game_over_string, True, white)
				screen.blit(game_over_text, [200,150])
				pygame.display.flip()
				print("GAME OVER")
				exit()
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				font = pygame.font.SysFont(None, 75)
				you_found_nemo_string = "YOU FOUND NEMO!"
				you_found_nemo_text = font.render(you_found_nemo_string, True, white)
				screen.blit(you_found_nemo_text, [100,150])
				pygame.display.flip()
				print("YOU FOUND NEMO!")
				exit()

		if event.key == pygame.K_DOWN and not pygame.sprite.collide_rect(Marlin,Bruce) and not pygame.sprite.collide_rect(Marlin, Nemo):
			if Bruce.rect.y > height:
				Bruce.rect.x = 500
				Bruce.rect.y = 0
			elif Marlin.rect.y > height:
				Marlin.rect.x = 70
				Marlin.rect.y = 50
			else:
				Marlin.rect.y += 10
				Bruce.rect.y += 20	

			if pygame.sprite.collide_rect(Marlin,Bruce):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(sharkbite, loops = 0)
				font = pygame.font.SysFont(None, 75)
				game_over_string = "GAME OVER"
				game_over_text = font.render(game_over_string, True, white)
				screen.blit(game_over_text, [200,150])
				pygame.display.flip()
				print("GAME OVER")
				exit()
			if pygame.sprite.collide_rect(Marlin, Nemo):
				pygame.mixer.Sound.stop(background_music)
				pygame.mixer.Sound.play(find_nemo, loops = 0)
				font = pygame.font.SysFont(None, 75)
				you_found_nemo_string = "YOU FOUND NEMO!"
				you_found_nemo_text = font.render(you_found_nemo_string, True, white)
				screen.blit(you_found_nemo_text, [100,150])
				pygame.display.flip()
				print("YOU FOUND NEMO!")
				exit()

			
	screen.blit(background_img, backgroundRect)
	
	sprite_group.draw(screen)
	
	# Timer
	total_time = start_time - (frame_count // frame_rate)
	
	if total_time == 0:
		font = pygame.font.SysFont(None, 50)
		game_over_string = "GAME OVER"
		game_over_text = font.render(game_over_string, True, white)
		screen.blit(game_over_text, [250,150])
		pygame.display.flip()
		print("GAME OVER")
		exit()
		
	minutes = total_time // 60
	seconds = total_time % 60
	time_string = "{0:02}:{1:02}".format(minutes, seconds)
	time_text = font.render(time_string, True, black)
	screen.blit(time_text, [315,0])
	frame_count += 1
	clock.tick(frame_rate)

	pygame.display.update()
	pygame.display.flip()


pygame.quit()
quit()