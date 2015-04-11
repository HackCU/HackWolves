import pygame

#Globals
BLACK = ( 0, 0, 0,)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
	pygame.init()
	
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.displau.set_mode(size)
	
	pygame.display.set_caption("THIS GAME IS AWESOME!")
	
	player = Player()
	
	level_list = []
	level_list.append(Level_01(player))
	level_list.append(Level_02(player))
	
	current_level_no = 0
	current_level = level_list[current_level_no]
	
	active_sprite_list = pygame.sprite.Group()
	player.level = current_level
	
	player.rect.x = 340
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)
	
	done = False
	
	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()
					
		active_sprite_list_update()
		
		current_level.update()
		
		if player.rect.right >= 500:
			diff = player.rect.right - 500
			player.rect.right = 500
			current_level.shift_world(-diff)
		
		if player.rect.left <= 120:
			diff = 120 - player.rect.left
			player.rect.left = 120
			current_level.shift_world(diff)
		
		current_position = player.rect.x + current_level.wordl_shift
		if current_position < current_level.level_limit:
			player.rect.x = 120
			if current_level_no < len(level_list)-1:
				current_level_no += 1
				current_level = level_list[current_level_no]
				player.level = current_level
		
		#drawing code should go here
		current_level.draw(screen)
		active_sprite_list.draw(screen)
		#end of drawing code section	
		
		clock.tick(60)
		
		pygame.display.flip()

	pygame.quit()
	
if __name__ == "__main__":
	main()
