#This is the beginning everytime to make the window
import random
import pygame
pygame.init()
win = pygame.display.set_mode((1000,1000))


#this will save you from having to remember the numbers to use the colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,128)

bg = pygame.image.load('spacebg2.jpg')
# char = 

#You build the classes for the objects here
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([50,25])
        self.image = pygame.image.load('shuttle.png')
        # self.image.fill(blue)
        self.rect = self.image.get_rect()
        # self.standing = True
        self.image = pygame.transform.rotate(self.image, 270)
    def draw(self):
        
        win.blit(self.image,(self.rect.x, self.rect.y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Asteroid Medium.png')
        # self.image.fill(red)
        self.rect = self.image.get_rect()
        self.direction = 5

    def update(self):
        self.rect.x -= self.direction

   
        


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,5])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 10

#Youll need to create the objects and maybe make blank lists here to initailize them

ship = Ship()
ship.rect.x = 50
ship.rect.y = 500


enemy_list = pygame.sprite.Group()

for i in range(1,6):
    enemy = Enemy()
    enemy.rect.x = random.randint(750,950)
    enemy.rect.y = random.randint(50,950)
    enemy_list.add(enemy)


missile_list = pygame.sprite.Group()
enemycount = 0


#You put the redraw function here which updates the game repeatedly until certain conditions are met
def redraw():
    win.blit(bg,(0,0))
    font = pygame.font.SysFont('Times New Roman',30)
    text = font.render("Jp's Spaceship Vs. The Asteroids", False, white)
    textRect = text.get_rect()
    textRect.center = (1000//2,25)
    win.blit(text,textRect)                              
    ship.draw()
    enemy_list.update()
    enemy_list.draw(win)
    missile_list.update()
    missile_list.draw(win)
    pygame.display.update()
#This is where you run the game and quit when you press the x in the corner
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#Key Binding

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        ship.rect.y -= 20
    if key[pygame.K_DOWN]:
        ship.rect.y += 20
    if key[pygame.K_SPACE]:
        if len(missile_list) < 20:   
            missile = Missile()  
            missile.rect.x = ship.rect.x + 50
            missile.rect.y = ship.rect.y + 23
            missile_list.add(missile)
            

    for missile in missile_list:
        if missile.rect.x > 1000:
            missile_list.remove(missile)
        for enemy in enemy_list:
            if missile.rect.colliderect(enemy.rect):
                missile_list.remove(missile)
                enemy_list.remove(enemy)  
                enemy = Enemy()
                enemy.rect.x = random.randint(750,950)
                enemy.rect.y = random.randint(50,950)
                enemy_list.add(enemy)
                
                enemycount +=1

                if enemycount // 5 == 0:
                    enemy2 = Enemy()
                    enemy2.rect.x = random.randint(750,950)
                    enemy2.rect.y = random.randint(50,950)
                    enemy_list.add(enemy2)
                    

    for enemy in enemy_list:
        if enemy.rect.x < 50:
                    

            run = False

            
            

#You end calling the redraw function

    redraw()