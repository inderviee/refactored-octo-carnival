#Task: create a two-dimensional grid container that can be used for making games.
#How: write the bodies of the functions below.
import pygame


class Grid:
    def __init__(self, num_cols, num_rows, size, start_value):
        #create a list of lists with start_value as the initial value of each cell.
        #create a pygame.Surface that is a square size x size
        self.box = pygame.Surface((size,size))
        #create a font object for drawing text
        self.grid = [[start_value] * num_cols for i in range(num_rows)]
        
        self.font = pygame.font.Font(None, 20)
                 
        
    def get(self, pos):
        #return the value at the given position where pos = (x, y)
        x,y = pos
        return self.grid[y][x]
    
    def set(self, pos, value):
        #set the position to the given value where pos = (x, y)
        x,y = pos
        self.grid[y][x] = value        
    
    def set_all(self, value):
        #set all cells to the given value
        self.grid = [[value] * self.num_cols() for i in range(self.num_rows())]
        
    
    def num_cols(self):
        #return the number of columns in the grid
        #hint: return the len() of the first list
        return len(self.grid[0])
    
    
    def num_rows(self):
        #return the number of rows in the grid
        #return the len() of the grid 
        return len(self.grid)
    
    def size(self):
        # use get_width to return the size of the square Surface you made in the
        # __init__ function
        return self.box.get_width()
    
    def grid2pixel(self, pos):
        # given a position where pos = (x, y) is in grid coordinates
        # return the pixel coordinates of the northwest corner of pos 
        x, y = pos
        return (x * self.size(), y * self.size())
    
    def pixel2grid(self, pos):
        # given a position where pos = (x, y) is in pixel coordinates
        # return the grid coordinates of the northwest corner of pos
        (x, y) = pos
        return (x // self.size(), y // self.size())
    
    def draw(self, image):
        # draw the entire grid onto the given image
        # make a double nested loop then
        # use draw_cell to draw a single cell
        for x in range(self.num_cols()):
            for y in range(self.num_rows()):
                self.draw_cell(image,(x,y))
        return image
    
    def draw_cell(self, image, pos):
        # draw a single cell
        color = self.get(pos)
        self.box.fill(color)
        self.draw_msg(self.box, "scooby")
        pygame.draw.rect(self.box,(0,0,0),(0,0,self.size(),self.size()),1)
        image.blit(self.box, self.grid2pixel(pos))
        return image        
        
        
    def draw_msg(self, image, message):
        # use the font object to draw a message on the given image
        textImg = self.font.render( message, 1, (0,0,0))
        w = (image.get_width())
        h = (image.get_height())
        image.blit(textImg, ((w - textImg.get_width()) / 2 , h / 2) )
    
    def click(self, pos):
        # process a mouse click where pos = (x, y) in pixel coordinates
        color1 = pygame.Color("red")
        color2 = pygame.Color("blue")
        color = self.get(self.pixel2grid(pos))
        if color == color1:
            self.set(self.pixel2grid(pos), color2)
        else: 
            self.set(self.pixel2grid(pos), color1)
            
#g = Grid(3, 4, 20, "foo")
#print( g.get((3,2)))
#print( g.set((3, 2),"scooby"))
#print( g.get((3,2)))

#print( g.num_cols() )
#print( g.num_rows() )


#print(g.grid)
#g.set_all("scoby")
#print(g.grid)

#g.draw(0)




# test code goes here

# comment out all test code before integrating the grid.py into other code