# When you run this game you control the space ship and you have to destroy asteroids
# you control the ship with the up and down keys 
# you can shoot missiles with the space bar, but there is a limit so you can't spam
# The asteroids will gradually increase and you just have to hold them off as long as you can
# There is also a counter on the screen to count how many asteroids you have destroyed

#This is the beginning everytime to make the window
import random
import pygame
pygame.init()
screenwidth = 1500
screenheigt = 750
win = pygame.display.set_mode((screenwidth,screenheigt))


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
    # the ship draws once here but then it moves within the game loop since you have to press a button
    def draw(self):
        
        win.blit(self.image,(self.rect.x, self.rect.y))

# This is the class that creates the asteroids
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Asteroid Medium.png')
        # self.image.fill(red)
        self.rect = self.image.get_rect()
        self.direction = 5
    #This is how the enemy automotically moves each frame since you don't press a button
    def update(self):
        self.rect.x -= self.direction

# This is the class for the projectiles you can shoot from your ship
class Missile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,5])
        self.image.fill(green)
        self.rect = self.image.get_rect()
    # Similiar to the draw class above, however this class only initalized with a key press in the game loop
    def update(self):
        self.rect.x += 10

#Youll need to create the objects and maybe make blank lists here to initailize them

ship = Ship()
ship.rect.x = 50
ship.rect.y = 500


enemy_list = pygame.sprite.Group()

for i in range(1,10):
    enemy = Enemy()
    enemy.rect.x = random.randint(screenwidth - (screenwidth//5),screenwidth - 50)
    enemy.rect.y = random.randint(50,screenheigt - 50)
    enemy_list.add(enemy)


missile_list = pygame.sprite.Group()
enemycount = 0

destroyed = 0

#Trying to make a game over screen
def endgame():
    for enemy in enemy_list:
        if enemy.rect.x < 50:
            win.blit(bg,(0,0))
            font = pygame.font.SysFont('Times New Roman',30)
            text = font.render("Game Over, You destroyed {} Asteroids".format(destroyed), False, white)
            textRect = text.get_rect()
            textRect.center = (screenwidth//2,screenheigt//2)
            win.blit(text,textRect)   



#You put the redraw function here which updates the game repeatedly until certain conditions are met
def redraw():
    # Background 
    win.blit(bg,(0,0))
    #This is all the text on the screen
    font = pygame.font.SysFont('Times New Roman',30)
    text = font.render("Jp's Spaceship Vs. The Asteroids", False, white)
    textRect = text.get_rect()
    textRect.center = (screenwidth//3 , 25)
    win.blit(text,textRect)   
    font = pygame.font.SysFont('Times New Roman',30)
    text = font.render('Asteroids destroyed: {}'.format(destroyed), False, white)
    textRect = text.get_rect()
    textRect.center = ((screenwidth//3)*2 , 25)
    win.blit(text,textRect)                            
    # This function puts the ship on the screen
    ship.draw()
    #these functions update and then redraw the enemys each time
    enemy_list.update()
    enemy_list.draw(win)
    # It's also required for the missiles to update and draw each time it redraws
    missile_list.update()
    missile_list.draw(win)
    #Endgame runs every time to check and see if the game is over before it redraws again
    endgame()
    #And this is necessary every time at the end
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
        # this variable below will set how many missiles you can actually shoot at a time 
        if len(missile_list) < 20:   
            missile = Missile()  
            missile.rect.x = ship.rect.x + 50
            missile.rect.y = ship.rect.y + 23
            missile_list.add(missile)
            
    #this is how the missiles are destroyed when they collide with an asteroid or leave the screen
    for missile in missile_list:
        if missile.rect.x > screenwidth:
            missile_list.remove(missile)
        for enemy in enemy_list:
            if missile.rect.colliderect(enemy.rect):
                destroyed += 1
                missile_list.remove(missile)
                enemy_list.remove(enemy)  
                enemy = Enemy()
                enemy.rect.x = random.randint(screenwidth - (screenwidth//5),screenwidth - 50)
                enemy.rect.y = random.randint(50,screenheigt - 50)
                enemy_list.add(enemy)
                
                enemycount +=1
                #This if statement incrementally increases the enemies on every fifth enemy
                if enemycount %5 == 0:
                    enemy2 = Enemy()
                    enemy2.rect.x = random.randint(screenwidth - (screenwidth//5),screenwidth - 50)
                    enemy2.rect.y = random.randint(50,screenheigt - 500)
                    
                    enemy_list.add(enemy2)
                    
    #You end calling the redraw function

    redraw()