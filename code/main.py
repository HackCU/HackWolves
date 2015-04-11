import pygame

pygame.init()

BLACK = ( 0, 0, 0,)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Screen")

done = False

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	screen.fill(WHITE)
	
	pygame.draw.rect(screen, RED, [55, 200, 10, 5], 30)
	
	font = pygame.font.SysFont('Calibri', 25)# 25, True, False)
	text = font.render("HELLO, WORLD!", True, BLACK)
	screen.blit(text, [250,250])
	
	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()
