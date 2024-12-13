
class Grid:
    def __init__(self, screen, tilemap):
        self.screen = screen
        self.cell_size = 32
        self.grid_size = (tilemap.w, tilemap.h)
        
        self.data = []

        self.generate_grid(tilemap.data[0])

    def print_data(self):
        for col in self.data:
            print(col)

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
            tile_type = ''
            if (tile_index == 0):
                tile_type = 'X'

            elif (tile_index >= 30 and tile_index <= 37):
                tile_type = 'G'
            
            elif (tile_index >= 111 and tile_index <= 122):
                tile_type = 'W'

            else:
                tile_type = ' '
            
            self.data[j].append(tile_type)

        # Update tiles next to water
        for y in range(self.grid_size[1]):
            for x in range(self.grid_size[0]):
                if self.data[y][x] == ' ' and is_next_to_water(x, y, self.grid_size):
                    self.data[y][x] = 'N'