import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('drawer')

running = True

while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.lines(screen, WHITE, True, [(30, 30), (300, 30), (300, 300), (30, 300), (30, 30)], 38)        
    pygame.draw.lines(screen, RED, True, [(300, 30), (400, 100), (300,300)], 38)
    
    pygame.display.flip()
pygame.quit()
