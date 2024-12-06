import pygame
from tilemap import *


def main():
    pygame.init()
    pygame.display.set_caption("Test")
    
    # Create screen
    screen = pygame.display.set_mode((480, 360))
    
    # grid = Grid(screen, grid_size, cell_size)

    # Load tilemap
    tilemap_object = Tilemap("assets/tilemap/isometric_tileset.png", "assets/tilemap/tilemap.json")
    
    while True:
        # Test tileset loading
        # for i in range(11):
        #     for j in range(11):
        #         index = i + 11 * j
        #         if index < len(tilemap_object.tiles):
        #             screen.blit(tilemap_object.tiles[index].convert(), (i * 32, j * 32))

        tilemap_object.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            #grid.move_player()
        pygame.display.flip()

if __name__ == "__main__":
    main()
    