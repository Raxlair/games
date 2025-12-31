from pygame import mixer
import pygame
import random

class Character():
    def __init__(self):
        self.x=0
        self.y=0

class Player(Character):
    
    def __init__(self):
        self.x=500
        self.y=500

        self.health = 100
        self.highscore = 0
        self.score = 0

        self.death = False
        self.difficulty = ""
        self.difficultySpeed = 0
    
    def Movement(self, playerSpeed):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]: 
            self.x = self.x - playerSpeed
        if keys[pygame.K_d]:
            self.x = self.x + playerSpeed
        if keys[pygame.K_w]:
            self.y = self.y - playerSpeed
        if keys[pygame.K_s]:
            self.y = self.y + playerSpeed
        
        playerIcon = pygame.image.load("images/player.png").convert()
        playerIcon = pygame.transform.scale(playerIcon ,(350, 237.5)) #change size of player
        screen.blit(playerIcon,(self.x,self.y))

    def checkDeath(self):
        if self.health <= 0:
            self.death = True
            mixer.music.load("audio/death.mp3")
            mixer.music.set_volume(1)
            mixer.music.play()
            
            while self.death == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    
                    if self.score > self.highscore:
                        self.highscore = self.score
                        mixer.music.load("audio/yay.mp3")
                        mixer.music.set_volume(1)
                        mixer.music.play()
                
                    screen.fill((0, 0, 0))
                    textSurface = Font.render("You are dead", True, (255, 255, 255))
                    screen.blit(textSurface, (800, 300))
                    textSurface = Font.render(f"Score: {self.score}", True, (255, 255, 255))
                    screen.blit(textSurface, (800, 400))
                    textSurface = Font.render(f"High Score: {self.highscore}", True, (255, 255, 255))
                    screen.blit(textSurface, (800, 500))       
                    textSurface = Font.render(f"Press ENTER to play again", True, (255, 255, 255))
                    screen.blit(textSurface, (800, 600)) 
                    pygame.display.update()

                    keys = pygame.key.get_pressed() 
                    if keys[pygame.K_RETURN]: 
                        #return values to base values
                        self.death = False
                        self.x=500
                        self.y=500
                        self.health = 100
                        self.score = 0                        

    def showHealth(self):
        xHealth = 1700
        yHealth = 50

        textSurface = Font.render(f"Health: {self.health}", True, (255, 255, 255))
        screen.blit(textSurface, (xHealth, yHealth))       

    def showScore(self):
        xScore = 50
        yScore = 50
        yHighscore = 100

        textSurface = Font.render(f"{self.score} points", True, (255, 255, 255))
        screen.blit(textSurface, (xScore, yScore))    
        
        self.score = self.score + 1

        textSurface = Font.render(f"Current Highscore: {self.highscore} points", True, (255, 255, 255))
        screen.blit(textSurface, (xScore, yHighscore))   

    def selectDifficulty(self):
        screen.fill((0, 0, 0))
        textSurface = Font.render("Press button to select difficulty", True, (255, 255, 255))
        screen.blit(textSurface, (800, 300))
        textSurface = Font.render(f"1 - Easy", True, (255, 255, 255))
        screen.blit(textSurface, (800, 400))
        textSurface = Font.render(f"2 - Medium", True, (255, 255, 255))
        screen.blit(textSurface, (800, 500))       
        textSurface = Font.render(f"3 - Hard", True, (255, 255, 255))
        screen.blit(textSurface, (800, 600)) 
        pygame.display.update()

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_1]: 
            self.difficulty = "easy"
            self.difficultySpeed = 50
        if keys[pygame.K_2]:
            self.difficulty = "medium"
            self.difficultySpeed = 25
        if keys[pygame.K_3]:
            self.difficulty = "hard"
            self.difficultySpeed = 10  
        
class Enemy(Character):
    def __init__(self):
        self.x=random.randint(0,1800)
        self.y=random.randint(0,980)
        self.height = random.randint(25, 200)
        self.width = random.randint(25, 200)
        
    def draw(self):
        self.enemyIconOriginal = pygame.image.load("images/evil.png").convert_alpha()
        self.enemyIcon = pygame.transform.scale(self.enemyIconOriginal, (self.height, self.width)) #change size of enemy
        screen.blit(self.enemyIcon,(self.x,self.y))

    def movement(self):
        self.xDestination = player.x
        self.yDestination = player.y

        enemySpeed = player.score/player.difficultySpeed

        if self.x < self.xDestination:
            self.x = self.x + enemySpeed
        if self.x > self.xDestination:
            self.x = self.x - enemySpeed
        if self.y < self.yDestination:
            self.y = self.y + enemySpeed
        if self.y > self.yDestination:
            self.y = self.y - enemySpeed
    
    def attack(self, damage, range):
        if (player.x+175 - range <= self.x <= player.x+175 + range and player.y+118.75 - range <= self.y <= player.y+118.75 + range):
            player.health = player.health - damage
            mixer.music.load("audio/damage.mp3")
            mixer.music.set_volume(1)
            mixer.music.play()

    def reset(self):
        if player.health <= 0:
            self.x=random.randint(0,1800)
            self.y=random.randint(0,980)
            self.height = random.randint(25, 200)
            self.width = random.randint(25, 200)

#initialise pygame and mixer
pygame.init()
mixer.init()
#start game window
screen = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
pygame.display.set_caption("game :?")
pygame_icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(pygame_icon)

screen.fill((0, 0, 0))
pygame.display.flip()

#handle background
bg = pygame.image.load("images/cat.png").convert()
bg = pygame.transform.scale(bg ,(1920,1080))

#handles the font settings
Font=pygame.font.SysFont('timesnewroman',  30)

player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.selectDifficulty()

    if player.difficulty == "easy":
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.blit(bg,(0,0))    
            player.Movement(40)

            enemy1.draw()
            enemy1.movement()
            enemy1.attack(5,100)

            player.showHealth()
            player.showScore()

            pygame.display.update()
            enemy1.reset()
            player.checkDeath()
        
        pygame.quit()
    
    elif player.difficulty == "medium":
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.blit(bg,(0,0))    
            player.Movement(40)

            enemy1.draw()
            enemy1.movement()
            enemy1.attack(5,100)

            enemy2.draw()
            enemy2.movement()
            enemy2.attack(5,100)

            player.showHealth()
            player.showScore()

            pygame.display.update()
            enemy1.reset()
            enemy2.reset()
            player.checkDeath()
        
        pygame.quit()

    elif player.difficulty == "hard":
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.blit(bg,(0,0))    
            player.Movement(40)

            enemy1.draw()
            enemy1.movement()
            enemy1.attack(5,100)

            enemy2.draw()
            enemy2.movement()
            enemy2.attack(5,100)

            enemy3.draw()
            enemy3.movement()
            enemy3.attack(5,100)

            player.showHealth()
            player.showScore()

            pygame.display.update()
            enemy1.reset()
            enemy2.reset()
            enemy3.reset()
            player.checkDeath()
        
        pygame.quit()

pygame.quit()