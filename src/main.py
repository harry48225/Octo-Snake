#Snake game in python with pygame

import pygame
from random import randrange
pygame.font.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

def gameover():
    
    font = pygame.font.Font(None, 60)
    gameovertext = font.render('GAMEOVER', True, (53, 239, 59))
    screen.blit(gameovertext, (0,0))
    pointrender = font.render('Length: {0}'.format(snake.len), True, (0,255,0))
    screen.blit(pointrender, (0, 460))
    pygame.display.flip()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
class SnakeHEAD(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((25,25))
        self.image.fill((255,255,255))
        
        self.rect = self.image.get_rect()
        self.len = 4
   
        self.direction = 'RIGHT'

        self.internaltick = 10
        
    def move(self, direction):
        
        if self.direction != direction:

            if direction != 'FORWARD':
                
                self.direction = direction

            snakeBODY.update()   
                
            
            snakeBODY.add(SnakeBODY(self.rect.x, self.rect.y, self.len-2))
    
            if self.direction == 'UP' and self.rect.y >= 25:

                self.rect.y -= 25
                
            elif self.direction == 'LEFT' and self.rect.x >= 25:

                self.rect.x -= 25
                
            elif self.direction == 'RIGHT' and self.rect.x <= 450:

                self.rect.x += 25
                
            elif self.direction == 'DOWN' and self.rect.y <= 450:

                self.rect.y += 25
            self.internaltick = 0
    def update(self):
        
        if self.internaltick == 10:


            self.move('FORWARD')

            self.internaltick = 0

        
        screen.blit(snake.image, (snake.rect.x,snake.rect.y))
        snakeBODY.draw(screen)
        
        intersectlist = pygame.sprite.spritecollide(self, snakeBODY, False)
        if len(intersectlist) > 0:
            
            print 'Gameover'
            gameover()

        self.internaltick +=1
        print self.internaltick
class SnakeBODY(pygame.sprite.Sprite):
    
    def __init__(self, x, y, life):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = snake.image
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.life = life
        
    def update(self):
        
        if self.life <= 0:
            
            self.kill()
            
        else:
            
            self.life -= 1
        pass


class apple(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (randrange(25,425,25), randrange(25,425,25))
        collsions = pygame.sprite.spritecollide(self, snakeBODY, False)
        while len(collsions) > 0:
            self.rect.topleft = (randrange(25,425,25), randrange(25,425,25))
            collsions = pygame.sprite.spritecollide(self, snakeBODY, False)
            
        screen.blit(self.image, (self.rect.x, self.rect.y))
            
    def update(self):
        
        
        if self.rect.colliderect(snake.rect):
            
            snake.len += 4
            for body in snakeBODY:
                body.life += 4
            apples.append(apple())
            self.kill()
            return True
            
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return False
        
#Main game loop
snake = SnakeHEAD()
snakeBODY = pygame.sprite.Group()
apples = [apple()]
movementdirection = 'RIGHT'
font = pygame.font.Font(None, 60)
while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    keypressed = pygame.key.get_pressed()
    
    if keypressed[pygame.K_w] and snake.direction != 'DOWN':
        movementdirection = 'UP'
    elif keypressed[pygame.K_s] and snake.direction != 'UP':
        movementdirection = 'DOWN'
    elif keypressed[pygame.K_a] and snake.direction != 'RIGHT':
        movementdirection = 'LEFT'
    elif keypressed[pygame.K_d] and snake.direction != 'LEFT':
        movementdirection = 'RIGHT'

    snake.move(movementdirection)

    screen.fill((0,0,0))

    snake.update()
    for appley in apples:
        if appley.update():
            apples.remove(appley)
    
    pointrender = font.render('Length: {0}'.format(snake.len), True, (0,255,0))
    screen.blit(pointrender, (0, 460))
    pygame.display.flip()
    clock.tick(60)
    