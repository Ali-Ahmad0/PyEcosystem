
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
        w, h = self.tileset.get_width(), self.tileset.get_height()

        # Tile size
        dx = 32
        tile_height = 32

        # Iterate over the tileset to extract each tile
        for y in range(0, h, tile_height):
            for x in range(0, w, dx):
                # Create a tile
                tile = pygame.Surface((dx, tile_height), pygame.SRCALPHA)  
                tile.blit(self.tileset, (0, 0), pygame.Rect(x, y, dx, tile_height))

                # Add the tile surface to the list
                self.tiles.append(tile)