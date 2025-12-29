import pygame
import random

class Character():
    def __init__(self):
        self.x=0
        self.y=0

class Player(Character):
    
    def __init__(self):
        self.x=0
        self.y=0

        self.health = 100
    
    def Movement(self, playerSpeed):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]: 
            self.x = self.x - playerSpeed
        elif keys[pygame.K_d]:
            self.x = self.x + playerSpeed
        elif keys[pygame.K_w]:
            self.y = self.y - playerSpeed
        elif keys[pygame.K_s]:
            self.y = self.y + playerSpeed
        
        playerIcon = pygame.image.load("images/player.png").convert()
        playerIcon = pygame.transform.scale(playerIcon ,(350, 237.5)) #change size of player
        screen.blit(playerIcon,(self.x,self.y))

    def checkDeath(self):
        if self.x == enemy1.x and self.y == enemy1.y or self.health <= 0:
            print("you are dead")

    def showHealth(self):
        xHealth = 400
        yHealth = 400
        
        #textRender = Font.render("HEALTH:"+str(self.health),True, white)
        #screen.blit(textRender,(xHealth,yHealth))

        textSurface = Font.render(f"Score: {self.health}", True, (255, 255, 255))
        screen.blit(textSurface, (100, 100))

class Enemy(Character):
    def __init__(self):
        self.x=random.randint(0,1800)
        self.y=random.randint(0,980)
        self.enemyIconOriginal = pygame.image.load("images/evil.png").convert_alpha()
        self.enemyIcon = pygame.transform.scale(self.enemyIconOriginal, (random.randint(25, 200), random.randint(25, 200))) #change size of enemy
        
    def draw(self):
        screen.blit(self.enemyIcon,(self.x,self.y))

    def movement(self, enemySpeed):
        self.xDestination = player.x
        self.yDestination = player.y

        if self.x < self.xDestination:
            self.x = self.x + enemySpeed
        if self.x > self.xDestination:
            self.x = self.x - enemySpeed
        if self.y < self.yDestination:
            self.y = self.y + enemySpeed
        if self.y > self.yDestination:
            self.y = self.y - enemySpeed

#initialise pygame
pygame.init()
#start game window
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
pygame.display.set_caption("stock :?")
pygame_icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(pygame_icon)

screen.fill((0, 0, 0))
pygame.display.flip()

#handle background
bg = pygame.image.load("images/cat.png").convert()
bg = pygame.transform.scale(bg ,(1920,1080))

#handles the font settings
Font=pygame.font.SysFont('timesnewroman',  30)
white = (255, 255, 255)
green = (0, 255, 0)
transparent = (0,0,0)

player = Player()
enemy1 = Enemy()

player.showHealth()
pygame.display.flip

screen.blit(bg,(0,0)) 
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))    
    player.Movement(20)
    enemy1.draw()
    pygame.display.update()

    player.checkDeath()
    enemy1.movement(5)

pygame.quit()