import random
import pygame
from stag import *
from wolf import *

class Grid:
    def __init__(self, screen, tilemap):
        self.screen = screen
        self.cell_size = 32
        self.grid_size = (tilemap.w, tilemap.h)

        self.data = []
        
        self.stag_list = []
        self.wolf_list = []

        self.generate_grid(tilemap.data[0])
        self.spawn_creatures()

    def print_data(self):
        for row in self.data:
            print(row)

    def generate_grid(self, map_data):
        
        # Check if a tile is next to water
        def is_next_to_water(x, y, grid_size):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Left, Right, Up, Down
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size[0] and 0 <= ny < grid_size[1]:
                    if self.data[ny][nx] == 'W':
                        return True
                    
            return False

        # Initialize the world grid
        for i in range(len(map_data)):
            if (i % self.grid_size[0] == 0):
                self.data.append([])
        
        # Set values
        for i, tile_index in enumerate(map_data):
            j = i // self.grid_size[0]

            # 29 to 36 - Grass Tiles
            # 110 to 121 - Water Tiles

            # 'X' - invalid
            # 'W' - water
            # ' ' - path
            # 'G' - grass
            # 'N' - next to water
            cell_type = ''
            if (tile_index == 0):
                cell_type = 'X'

            elif (tile_index >= 30 and tile_index <= 37):
                cell_type = 'G'
            
            elif (tile_index >= 111 and tile_index <= 122):
                cell_type = 'W'

            else:
                cell_type = ' '
            
            self.data[j].append(cell_type)

        # Update tiles next to water
        for y in range(self.grid_size[1]):
            for x in range(self.grid_size[0]):
                if self.data[y][x] == ' ' and is_next_to_water(x, y, self.grid_size):
                    self.data[y][x] = 'N'

    def spawn_creatures(self):
        for i, data_row in enumerate(self.data):
            for j, cell_type in enumerate(data_row):
                if cell_type == ' ':
                    # Calculate the tile pixel coordinates
                    x = (j - i) * 16
                    y = (j + i) * 8 
                    
                    # Ensure the coordinates are within valid bounds
                    if 0 <= x < len(self.data[0]) * 16 and 0 <= y < len(self.data) * 8:
                        # Spawn a stag with a 2.5% chance
                        if random.random() < 0.025:
                            self.stag_list.append(Stag(x + 3, y - 20))

                        # Spawn a wolf with a 2.5% chance
                        elif random.random() > 0.975:
                            self.wolf_list.append(Wolf(x - 16, y - 24))