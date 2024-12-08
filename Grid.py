import pygame
import math

class Grid:
    def __init__(self, screen, map_data):
        self.screen = screen
        self.cell_size = 32
        self.grid_size = int(math.sqrt(len(map_data)))
        self.window_size = self.grid_size * self.cell_size
        
        # Initialize grid based on map_data
        self.grid = [[-1 if map_data[row * self.grid_size + col] == -1 else 0 
                      for col in range(self.grid_size)] 
                     for row in range(self.grid_size)]
        
        
    
        
        pygame.display.flip()