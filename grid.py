
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
        # Initialize the world grid
        for i in range(len(map_data)):
            if (i % self.grid_size[0] == 0):
                self.data.append([])
        
        # Set values
        for i, tile_index in enumerate(map_data):
            j = i // self.grid_size[0]

            # 29 to 36 - Grass Tiles
            # 110 to 121 - Water Tiles

            # 'X' - invalid / water
            # ' ' - path
            # 'G' - grass
            # 'W' - next to water
            tile_type = ''
            if (tile_index == 0):
                tile_type = 'X'

            elif (tile_index >= 30 and tile_index <= 37):
                tile_type = 'G'
            
            elif (tile_index >= 111 and tile_index <= 122):
                tile_type = 'X'

            else:
                tile_type = ' '
            
            self.data[j].append(tile_type)