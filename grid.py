
class Grid:
    def __init__(self, screen, tilemap):
        self.screen = screen
        self.cell_size = 32
        self.grid_size = tilemap.map_w * tilemap.map_h
        
