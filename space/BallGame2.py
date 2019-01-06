from BasicGame import *
from pygame import *
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform

#add your classes here
from Ball import *

#constants
FPS = 40 #Frames per second

class BallGame(BasicGame):
    def __init__(self):
        self.w, self.h = 800, 600
        self.bkg_color = (255,255,255)
        BasicGame.__init__(self, size=(self.w, self.h), fill=(self.bkg_color))
        
        #create walls for the game
        self.LEFT_WALL = 0
        self.RIGHT_WALL = self.w
        self.TOP_WALL = 0
        self.BOTTOM_WALL = self.h
        
        #create a single ball
        self.ball = Ball(self.w / 2, self.h / 2)
        
    def update(self):
        self.keyPoll()
        self.ball.move()
        self.handle_collisions(self.ball)
        
    def handle_collisions(self, ball):
        if ball.right() > self.RIGHT_WALL:
            ball.bounce_horiz()
        if ball.left() < self.LEFT_WALL:
            ball.bounce_horiz()                    
        #add code for the other three walls
        
        
    def keyPoll(self): 
        #use this function if you want to handle multiple key presses
        #this function must be called in update
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            print ("scooby")
            pass #maybe "right" player moves down and right at same time?
        if keys[pygame.K_d] and keys[pygame.K_x]:
            pass #maybe "left" player moves down and right
        
    def keyUp(self, key):
        if key == pygame.K_DOWN:
            print ('down')
        elif key == pygame.K_RIGHT:
            print ('right')
        else:
            pass
        
    def mouseUp(self, button, pos):
        if button == 1:
            pass
     
    def mouseDown(self, button, pos):
        if button == 1:
            pass    
        
    def mouseMotion(self, buttons, pos, rel):
        left, mid, right = buttons
        if left == 1:
            pass
             
    def draw(self):
        self.screen.fill(self.bkg_color) #clear screen
        self.ball.draw(self.screen)
    
        
s = BallGame()
s.mainLoop(FPS)