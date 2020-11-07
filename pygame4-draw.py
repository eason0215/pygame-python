import pygame
import random
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.init()
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('image')
clock = pygame.time.Clock()


background = pygame.image.load('galaxy.png')
background.convert()

ship = pygame.image.load('spaceship-removebg-preview.png')
ship.convert()

ship = pygame.transform.scale(ship, (100, 100))

#bgm = pygame.mixer.music.load('ghost.mp3')
#pygame.mixer.music.play(loops = -1)


ship_x = 300
ship_y = 450
running = True
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    (ship_x, ship_y) = pygame.mouse.get_pos()    
    
    
    screen.blit(background, (0, 0))   
    screen.blit(ship, (ship_x, ship_y))
    
    
    
    
    
    
    
    
    
    
    pygame.display.flip()
pygame.quit()
