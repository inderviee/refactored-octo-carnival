import random
import pygame
from pygame.locals import *
 
WIDTH = 600
HEIGHT = 600
MOVEMENT_AMOUNT = (WIDTH / 600) * (HEIGHT / 600) * .5
ALIEN_WIDTH = 50
ALIEN_HEIGHT = 40
ALIENS_PER_ROW = int((WIDTH / 600) * 10)
NUMBER_OF_ROWS = int((HEIGHT / 600) * 3)

pygame.init() 

class Entity(object):
 
    def __init__(self, width, height, imagePath):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
 
    def getWidth(self):
        return self.width
 
    def getHeight(self):
        return self.height
 
    def getX(self):
        return self.x
 
    def getY(self):
        return self.y
 
    def setX(self, x):
        self.x = x
 
    def setY(self, y):
        self.y = y
 
    def draw(self, screen):
        screen.blit(self.image, Rect(self.x, self.y, self.width, self.height))
 
    def drawColour(self, screen, newColour):
        self.image.fill(newColour[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
        screen.blit(self.image, Rect(self.x, self.y, self.width, self.height))
 
    def increaseX(self, amount):
        if self.x <= WIDTH - self.width and self.x >= 0:
            self.x = self.x + amount
        elif self.x < 0:
            self.x = 1
        else:
            self.x = WIDTH - self.width - 1
 
    def increaseY(self, amount):
        if self.y <= HEIGHT - self.height and self.y >= 0:
            self.y = self.y + amount
        elif self.y < 0:
            self.y = 1
        else:
            self.y = HEIGHT - self.height - 1
 
class Bullet(Entity):
 
    def __init__(self, width, height, imagePath):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.moving = False
 
    def isMoving(self):
        return self.moving
 
    def setMoving(self, moving):
        self.moving = moving
 
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Space Invaders")
 
cannon = Entity(80, 48, "cannons.png")
cannon.setX(int(WIDTH / 2) - int(cannon.width / 2))
cannon.setY(HEIGHT - cannon.getHeight())
 
bullets = []
aliens = []
 
aliensLeft = False
aliensDown = False
restart = False
 
bulletFireCooldown = 0
bulletFireCooldownUse = False
 
moveDownBool = False
moveLeftBool = False
dontMoveBool = False
lastY = 0
 
class Alien(Entity):
 
    def __init__(self, width, height, imagePath):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.lastY = 0
 
def createAliens():
    for y in range(0, NUMBER_OF_ROWS):
        for x in range(0, ALIENS_PER_ROW):
            alien = Alien(ALIEN_WIDTH, ALIEN_HEIGHT, "aliens.png")
            alien.setY(y * ALIEN_HEIGHT)
            alien.setX(x * ALIEN_WIDTH)
            aliens.append(alien)
 
def resetGame():
    global restart
    global moveLeftBool
    global dontMoveBool
    global moveDownBool
    global lastY
    restart = False
    aliens[:] = []
    createAliens()
    cannon.setX(int(WIDTH / 2) - int(cannon.width / 2))
    cannon.setY(HEIGHT - cannon.getHeight())
    moveLeftBool = False
    lastY = aliens[0].y
    moveDownBool = False
    dontMoveBool = False
 
def moveAliens():
    global moveLeftBool
    global dontMoveBool
    global moveDownBool
    global lastY
    for alien in aliens:
        if moveLeftBool:
            if not dontMoveBool:
                alien.increaseX(-MOVEMENT_AMOUNT / int((HEIGHT / 600) * 2) / 2)
                if alien.x <= 1:
                    moveLeftBool = False
                    moveDownBool = True
                    dontMoveBool = True
                    lastY = aliens[0].y
        else:
            if not dontMoveBool:
                alien.increaseX(MOVEMENT_AMOUNT / int((HEIGHT / 600) * 2) / 2)
                if alien.x >= WIDTH - ALIEN_WIDTH:
                    moveLeftBool = True
                    moveDownBool = True
                    dontMoveBool = True
                    lastY = aliens[0].y
        if moveDownBool:
            alien.increaseY(MOVEMENT_AMOUNT / int((HEIGHT / 600) * 2))
            if alien.y == lastY + ALIEN_HEIGHT:
                moveDownBool = False
                dontMoveBool = False
                print("Moved down", lastY)
        if alien.y >= HEIGHT - alien.height - cannon.height:
            resetGame()
 

createAliens()
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
 
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            cannon.increaseX(MOVEMENT_AMOUNT)
        if event.key == K_LEFT:
            cannon.increaseX(-MOVEMENT_AMOUNT)
        if event.key == K_SPACE and bulletFireCooldown == 0:
            bulletFireCooldownUse = True
            bullet = Bullet(10, 20, "bullet.png")
            bullet.setX(cannon.getX() + (cannon.getWidth() / 2) - (bullet.getWidth() / 2))
            bullet.setY(HEIGHT - cannon.getHeight() - bullet.getHeight())
            bullet.setMoving(True)
            bullets.append(bullet)
        if event.key == K_t:
            MOVEMENT_AMOUNT = (WIDTH / 600) * (HEIGHT / 600) * 15
        else:
            MOVEMENT_AMOUNT = (WIDTH / 600) * (HEIGHT / 600) * 20
 
    for bullet in bullets:
        bullet.setY(bullet.getY() - MOVEMENT_AMOUNT)
        bullet.draw(screen)
        if bullet.getY() == 0 - bullet.getHeight():
            bullet.setMoving(False)
            bullets.remove(bullet)
 
    if bulletFireCooldownUse:
        bulletFireCooldown = bulletFireCooldown + 60
        if bulletFireCooldown == int((HEIGHT / 600) * 300):
            bulletFireCooldownUse = False
            bulletFireCooldown = 0
 
    for alien in aliens:
        for bullet in bullets:
            if bullet.getX() >= alien.getX() and bullet.getX() + bullet.getWidth() <= alien.getX() + alien.getWidth():
                if bullet.getY() >= alien.getY() and bullet.getY() + bullet.getHeight() <= alien.getY() + alien.getHeight():
                    bullets.remove(bullet)
                    aliens.remove(alien)
        alien.draw(screen)
    moveAliens()
 
    if len(aliens) == 0:
        restart = True
    if restart:
        restart = False
        resetGame()
         
    cannon.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    screen.fill(Color("black"))
self.clock = pygame.time.Clock() #to track FPS   
pygame.exit()