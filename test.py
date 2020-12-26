import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('')

class ball(pygame.sprite.Sprite):
    x = 0
    y = 0
    dx = 0
    dy = 0
    
    
    
    
    def __init__(self, ox, oy, radius, speedx, speedy):
        self.color = RED
        super().__init__()
        self.image = pygame.image.load('circle.png')
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = ox
        self.rect.y = oy
        
        self.dx = speedx
        self.dy = speedy
        self.x = ox
        self.y = oy

running = True
Ball = ball(10, 10, 10, 10, 10)
ballgroup = pygame.sprite.Group()
ballgroup.add(Ball)
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Ball.rect.x = Ball.rect.x - 100
                y_change = 0
            if event.key == pygame.K_RIGHT:
                Ball.rect.x = Ball.rect.x + 100
                y_change = 0
    
    
        
        

    
    
    
    
    
    
    
    
    
    ballgroup.draw(screen)
    pygame.display.flip()
pygame.quit()
