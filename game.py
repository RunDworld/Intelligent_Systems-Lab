import pygame
import wumpus as wmp

pygame.init()

pygame.display.set_caption("Wumpus World")
clock = pygame.time.Clock()

def gamepl():
	wmp.drawBoard()
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				break
			if event.type == pygame.MOUSEBUTTONDOWN:
				ab,ac = pygame.mouse.get_pos()
				print(str(ab)+"--"+str(ac))
		pygame.display.update()
		clock.tick(30)

gamepl()
pygame.quit()
quit()