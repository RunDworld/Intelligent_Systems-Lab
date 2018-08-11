import pygame

screen_x = 680
screen_y = 680

BLACK = (0,0,0)
WHITE = (255,255,255)


pygame.init()
size = (screen_x,screen_y)
screen = pygame.display.set_mode(size)
agent = pygame.image.load('rsz_hunter7.jpg')
wump = pygame.image.load('rsz_wump.jpg')
gold = pygame.image.load('rsz_gold.jpg')



locate = {
			1:[35,5],2:[175,5],3:[345,5],4:[515,5],
			5:[5,175],6:[175,175],7:[345,175],8:[515,175],
			9:[5,345],10:[175,345],11:[345,345],12:[515,345],
			13:[5,515],14:[175,515],15:[345,515],16:[515,515]
		}


occupied = []



def drawBoard():

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [int(screen_x/4), 5],[int(screen_x/4), int(screen_y-5)],5)
    pygame.draw.line(screen, BLACK, [int(2*screen_x/4), 5],[int(2*screen_x/4), int(screen_y-5)],5)
    pygame.draw.line(screen, BLACK, [int(3*screen_x/4), 5],[int(3*screen_x/4), int(screen_y-5)],5)
    pygame.draw.line(screen, BLACK, [5, int(screen_y/4)],[int(screen_x-5), int(screen_x/4)],5)
    pygame.draw.line(screen, BLACK, [5, int(2*screen_x/4)],[int(screen_x-5), int(2*screen_x/4)],5)
    pygame.draw.line(screen, BLACK, [5, int(3*screen_x/4)],[int(screen_x-5), int(3*screen_x/4)],5)
    screen.blit(agent,tuple(locate[1]))
    screen.blit(gold,tuple(locate[4]))
    screen.blit(wump,tuple(locate[7]))


    # while 1:
    # 	ab,ac = pygame.mouse.get_pos()
    # 	print(str(ab)+"--"+str(ac))