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
        
        playerIcon = pygame.image.load("images/player.png")
        screen.blit(playerIcon,(self.x,self.y))

    def checkDeath(self):
        if player.x == enemy.x and player.y == enemy.y:
            print("you are dead")

class Enemy(Character):
    def spawn(self):
        for x in range(random.randint(5,10)):
            self.x=random.randint(0,1920)
            self.y=random.randint(0,1080)
            enemyIconOriginal = pygame.image.load("images/evil.png").convert_alpha()
            enemyIcon = pygame.transform.scale(enemyIconOriginal, (random.randint(50, 1000), random.randint(50, 1000)))
            screen.blit(enemyIcon,(self.x,self.y))

player = Player()
enemy = Enemy()

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
enemy.spawn()
pygame.display.update()

enemy.spawn()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))    
    player.Movement(30)
    #enemy.spawn()
    pygame.display.update()

    player.checkDeath()
    print("a")

pygame.quit()