import math
import pygame

class Ship:
   def __init__(self, x = 0, y=0, dx=5, dy=8):
      self.image = pygame.image.load("ship.png").convert()
      self.lives = 3 
      self.x = x
      self.y = y
      self.step_size = 3
      self.lazer_list = [] 
      
   def draw(self, image):
      image.blit(self.image, (self.x, self.y))
      return image
    
   def move_left(self, limit):
      pass
   def more_right(self, limit):
      pass
   def shoot(self):
      pass
   
   
   
