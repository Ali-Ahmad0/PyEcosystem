import pygame
from tilemap import *
from grid import *

def main():
    pygame.init()
    pygame.display.set_caption("Test")
    
    # Set grid size and cell size
    grid_size = 32
    cell_size = 16  
    
    # Calculate window size
    window_size = grid_size * cell_size
    
    # Create screen
    screen = pygame.display.set_mode((window_size, window_size))
    
    # grid = Grid(screen, grid_size, cell_size)

    # Load tilemap
    tilemap_object = Tilemap("assets/tilemap/spritesheet.png", "assets/tilemap/tilemap.json")
    
    while True:
        screen.blit(tilemap_object.tileset.convert(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            #grid.move_player()
        pygame.display.flip()

if __name__ == "__main__":
    main()
    