import pygame
from tilemap import *


def main():
    pygame.init()
    pygame.display.set_caption("Test")
    
    # Create screen
    screen = pygame.display.set_mode((480, 360))
    
    # Load tilemap
    tilemap_object = Tilemap("assets/tilemap/isometric_tileset.png", "assets/tilemap/tilemap.json", (220, 40))
    
    while True:
        tilemap_object.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
    