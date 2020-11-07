import pygame
import random
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.init()
millisecond = pygame.time.get_ticks()

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

font = pygame.font.Font(None, 50)



ship_x = 300
ship_y = 450
stonelist = []
for i in range(50):
    x = random.randint(0, width)
    y = random.randint(-600, 0)
    stonelist.append([x, y])
score = 0
running = True
while running:
    
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    (ship_x, ship_y) = pygame.mouse.get_pos()    
    
    
    screen.blit(background, (0, 0))
    #score display
    text = font.render('score :' + str(score), True, RED)
    screen.blit(text, (10, 400))
    #second display
    millisecond2 = pygame.time.get_ticks()
    second = (millisecond2 - millisecond) / 1000
    text = font.render('second :' + str(second), True, RED)
    screen.blit(text, (190, 400))
    #ship display
    screen.blit(ship, (ship_x, ship_y))
    
    #drop stone
    for i in range(len(stonelist)):
        if stonelist[i][1] > height:
            y = random.randint(-600, 0)
            x = random.randint(0, width)
            stonelist[i][0] = x
            stonelist[i][1] = y
       
        y = stonelist[i][1] + 1
        stonelist[i][1] = y
        
        pygame.draw.circle(screen, WHITE, (stonelist[i][0], stonelist[i][1]), 15) 
    
    
    
    
    
    #detect collide
    for i in range(len(stonelist)):
        if ((stonelist[i][0] <= ship_x) and (ship_x <= stonelist[i][0] + 30)
        and (stonelist[i][1] < ship_y < stonelist[i][1] + 30)):
            score = score + 1
            
    if score > 100:
        text = font.render('you win', True, RED)
        screen.blit(text, (250, 250))
    
    
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
