import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.init()
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('drawer')
clock = pygame.time.Clock()

running = True

rect_x = 0
rect_y = 0

while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.lines(screen, WHITE, True, [(30, 30), (470, 30), (470, 470), (30, 470), (30, 30)], 38) 
    rect_x = rect_x + 1   
    rect_y = rect_y + 1  
    pygame.draw.rect(screen, RED, [rect_x, rect_y, 250, 250], 55)      
    pygame.draw.circle(screen, RED, (100, 100), 38) 
    pygame.draw.circle(screen, RED, (100, 400), 38)    
    pygame.draw.ellipse(screen, RED, [250, 250, 250, 250], 10)
    pygame.draw.arc(screen, BLACK, [200, 200, 200, 200], (0 * 3.14) / 180, (180 * 3.14) / (180), 5)
    pygame.draw.polygon(screen, BLACK, [(30, 25), (65, 98), (87, 87), (324, 54), (76, 213)])
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
