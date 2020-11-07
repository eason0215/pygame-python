import pygame
import random

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('drawer')
clock = pygame.time.Clock()
running = True
x = random.randint(0, height)
y = 0
snowlist = []

for i in range(1000):
    x = random.randint(0, width)
    y = random.randint(-600, -10)
    snowlist.append([x, y])

blockcolor = WHITE
(pos_x, pos_y) = (300, 400)
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('u are so sucks')
            print(pygame.mouse.get_pos())
            blockcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('fuck u')
                pos_y = pos_y - 10
            if event.key == pygame.K_s:
                print('shit')
                pos_y = pos_y + 10
            if event.key == pygame.K_a:
                print('bagayalo')
                pos_x = pos_x - 10
            if event.key == pygame.K_d:
                print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
                pos_x = pos_x + 10
      
        
    #(pos_x, pos_y) = pygame.mouse.get_pos()        
    pygame.draw.rect(screen, blockcolor, (pos_x, pos_y, 50, 10))
            
            
    for i in range(len(snowlist)):
        x = snowlist[i][0]
        y = snowlist[i][1]
             
        if y > height:
            y = random.randint(-600, -10)
        y = y + 5   
        
        snowlist[i][1] = y
        
        pygame.draw.circle(screen, blockcolor, (x, y), 10)         
        
    
    
    
    
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
