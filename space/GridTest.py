import os
if os.name == 'nt':
    os.environ['SDL_VIDEODRIVER'] = 'windib'
import pygame
from pygame.locals import *
from Grid import *

class GridTest:
    def __init__(self):
        pygame.init()
        self.w, self.h = 600, 700
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.screen.fill((255,255,255))
        
        self.running = False
        self.clock = pygame.time.Clock() #to track FPS       
        
        self.board = Grid(6, 7, 100, pygame.Color("red"))
        
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONUP:
                self.board.click(event.pos)
        
    def mainLoop(self, fps=0):
        self.running = True
        self.fps= fps
        
        while self.running:
            pygame.display.set_caption("FPS: %i" % self.clock.get_fps())
            self.handleEvents()
            self.board.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.quit()    
        
s = GridTest()
s.mainLoop(9)
