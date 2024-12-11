import pygame
from tilemap import *
from camera import *
from grid import *
from stag import *

class Main():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Ecosystem")

        # Screen and clock
        self.screen = pygame.display.set_mode((540, 400))
        self.clock = pygame.time.Clock()

        # Initialize world map
        self.world_map = Tilemap("assets/tilemap/isometric_tileset.png", "assets/tilemap/tilemap.json")

        # Initialize grid with map_data from world_map
        self.grid = Grid(self.screen, self.world_map)
        self.stag = Stag(0, 0)

        Camera.zoom = 2

    # Simulation render logic
    def render(self):
        self.screen.fill((0, 0, 0))
        self.world_map.render(self.screen)
        self.stag.render(self.screen)

        pygame.display.update()

    # Pygame events handling
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # Simulation update logic
    def update(self):
        
        keys = pygame.key.get_pressed()
        
        # Move camera
        camera_dx = 0
        camera_dy = 0

        if keys[pygame.K_LEFT]:
            camera_dx = -1
        if keys[pygame.K_RIGHT]:
            camera_dx = 1
        if keys[pygame.K_UP]:
            camera_dy = -1
        if keys[pygame.K_DOWN]:
            camera_dy = 1
        
        Camera.move(camera_dx, camera_dy)
        
        self.clock.tick(60)

    def main_loop(self):
        while True:
            self.render()
            self.events()
            self.update()

if __name__ == "__main__":
    simulation = Main()
    simulation.main_loop()