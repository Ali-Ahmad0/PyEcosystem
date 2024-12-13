
import pygame
import json
from camera import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, surface, *groups):
        super().__init__(*groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=position)

class Tileset():
    def __init__(self, tileset_path):
        self.tileset_path = tileset_path

        self.image = pygame.image.load(tileset_path)
        self.tiles = []

        self.load_tiles()

    # Load individual tiles
    def load_tiles(self):
        # Tileset dimensions
        w, h = self.image.get_width(), self.image.get_height()

        # Tile size
        dx = 32
        dy = 32

        # Iterate over the tileset to extract each tile
        for y in range(0, h, dy):
            for x in range(0, w, dx):
                # Split an individual tile surface from the tileset
                tile_surface = pygame.Surface((dx, dy), pygame.SRCALPHA)  
                tile_surface.blit(self.image, (0, 0), pygame.Rect(x, y, dx, dy))

                # Add the tile to the list
                self.tiles.append(tile_surface)

class Tilemap():
    def __init__(self, tileset_path, tilemap_path, dimensions=(16, 16)):
        self.tileset = Tileset(tileset_path)

        self.tilemap_path = tilemap_path
        self.sprite_group = pygame.sprite.Group()

        self.tilemap = None
        self.w = dimensions[0]
        self.h = dimensions[1]

        self.data = []
        self.load_tilemap()

    # Draw the tilemap based on tilemap data
    def load_tilemap(self):
        with open(self.tilemap_path, "r") as file:
            map_data = json.load(file)

        # Get tilemap data for each layer
        layers = map_data['layers']

        for _ in range(len(layers)):
            self.data.append(list)
        
        # Get height and width (in no. of tiles)
        self.w = map_data['width']
        self.h = map_data['height']

        for i, layer in enumerate(layers):
            for row in range(self.h):
                self.data[i] = layer['data']

                for col in range(self.w):
                    # Calculate the tile index
                    tile_index = self.data[i][col + self.w * row] - 1

                    # Skip if (empty tile)
                    if tile_index >= 0:  
                        # Get the surface of the tile
                        tile_surface = self.tileset.tiles[tile_index]

                        # Calculate x, y coordinates
                        x = (col - row) * 16
                        y = (col + row) * 8

                        tile = Tile((x, y), tile_surface, self.sprite_group)

    def render(self, screen):
        for tile in self.sprite_group:
            Camera.apply(tile.image, tile.rect, screen)
