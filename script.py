import pygame
import random

class Character():
    def __init__(self):
        self.x=0
        self.y=0

class Player(Character):
    
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
        if player.x == enemy1.x and player.y == enemy1.y:
            print("you are dead")

class Enemy(Character):
    def __init__(self):
        self.x=random.randint(0,1800)
        self.y=random.randint(0,980)
        self.enemyIconOriginal = pygame.image.load("images/evil.png").convert_alpha()
        self.enemyIcon = pygame.transform.scale(self.enemyIconOriginal, (random.randint(25, 200), random.randint(25, 200))) #change size of enemy
        
    def draw(self):
        screen.blit(self.enemyIcon,(self.x,self.y))

#initialise pygame
pygame.init()
#start game window
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
pygame.display.set_caption("Pygame")
pygame_icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(pygame_icon)

screen.fill((0, 0, 0))
pygame.display.flip()

bg = pygame.image.load("images/cat.png").convert()
bg = pygame.transform.scale(bg ,(1920,1080))

screen.blit(bg,(0,0)) 
pygame.display.update()

player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))    
    player.Movement(30)
    enemy1.draw()
    enemy2.draw()
    enemy3.draw()
    pygame.display.update()

    player.checkDeath()
    print("a")

pygame.quit()