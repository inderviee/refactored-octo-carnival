from BasicGame import *
from pygame import *
from Ball import *
from math import *
from random import uniform
FPS = 30
pygame.display.init
bg = pygame.image.load("invaders.png").convert ()
gameDisplay.blit(bg, (0, 0))


class space_invaders_game(BasicGame):
    def __init__(self):
        self.w , self.h = 800 , 600
        self.bkg_color = (255,255,255)
        BasicGame.__init__(self, size = (self.w, self.h), fill=(self.bkg_color))
        
        self.LEFT_WALL = 0
        self.RIGHT_WALL = self.w
        self.TOP_WALL = 0
        self.BOTTOM_WALL = self.h
        
        self.ship = Ship(self.w // 2, self.h // 2)


    def handle_collisions(self, ship):
        pass
        
        
    def update(self):
        self.keypoll()
    def keypoll(self): 
        #use this function if you want to handle multiple key presses
        #this function must be called in update
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            print ("scooby")
            pass #maybe "right" player moves down and right at same time?
        if keys[pygame.K_d] and keys[pygame.K_x]:
            pass #maybe "left" player moves down and right
        
        
    def draw(self):
        self.screen.fill(self.bkg_color) #clear screen
        self.ship.draw(self.screen)   
                
s = space_invaders_game()
s.mainLoop(FPS)
