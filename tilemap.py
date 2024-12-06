
import pygame

class Tilemap():
    def __init__(self, tileset_path, tilemap_path):
        self.tileset_path = tileset_path
        self.tilemap_path = tilemap_path

        self.tileset = pygame.image.load(tileset_path)
        self.tiles = []

        self.load_tiles()

        self.tilemap = None

    # Load individual tiles
    def load_tiles(self):
        # Tileset dimensions
        w, h = self.tileset.get_rect().size

        # Tilesize
        dx = 32 
        dy = 32

        for i in range(0, w, dx):
            for j in range(0, h, dy):
                # Create new tile
                tile = pygame.Surface((32, 32)).blit(self.tileset, (0, 0), (i, j, *(32, 32)))
                
                # Add to list of tiles
                self.tiles.append(tile)