import math
import pygame

class ship:
    SIZE = 30
    def __init__(self, x = 0, y=0, dx=5, dy=8, color=(0,0,255)):
        self.image = 0
        self.lives = 3
        self.x = center
        self.y = bottom
        self.step_size = 3
        self.laser_list = []
        
    #ball methods
    #draw: Ball, image -> image
    #draw the ball on an image
    def draw(self, image):
        pygame.draw.circle(image, 
                           self.color,
                           (self.x, self.y),
                           self.size)
        return image
    
    #move: Ball -> None
    def move(self):
        self.move_horz()
        self.move_vert()
    
    #write a comment
    def right(self):
        return self.x + self.size
    
    #write a comment
    def left(self):
        return self.x - self.size

    #write a comment
    def top(self):
        pass        
        
    #write a comment
    def bottom(self):
        pass            
    
    #move: Ball -> None
    #move the move horizontally
    #Hint: add x + dx 
    def move_horz(self):
        self.x = self.x + self.dx
    
    #move: Ball -> None
    #move the move vertically
    #Hint: add y + dy
    def move_vert(self):
        pass
    
    #write a comment
    def set_color(self, color):
        pass
    
    #write a comment
    def bounce_horiz(self):
        self.dx = self.dx * -1
    
    #write a comment
    def bounce_vert(self):
        pass
    

