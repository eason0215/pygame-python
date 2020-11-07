import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('')

running = True

while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    
    
    
    
    
    
    
    
    
    
    pygame.display.flip()
pygame.quit()
