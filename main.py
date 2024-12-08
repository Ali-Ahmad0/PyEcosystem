import pygame
from tilemap import *
from camera import *
from Grid import *

class Main():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Ecosystem")

        # Screen and clock
        self.screen = pygame.display.set_mode((540, 400))
        self.clock = pygame.time.Clock()

        # Initialize world map
        self.world_map = Tilemap("../AI-based-Ecological-Simulation/assets/tilemap/isometric_tileset.png", "assets/tilemap/tilemap.json")

        # Initialize grid with map_data from world_map
        self.grid = Grid(self.screen, self.world_map.map_data)

    # Simulation render logic
    def render(self):
        self.screen.fill((0, 0, 0))
        self.world_map.render(self.screen)
        # self.grid.draw_grid()

        pygame.display.update()

    # Pygame events handling
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # Simulation update logic
    def update(self):
        # Move camera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Camera.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            Camera.move(1, 0)
        if keys[pygame.K_UP]:
            Camera.move(0, -1)
        if keys[pygame.K_DOWN]:
            Camera.move(0, 1)

        self.clock.tick(60)

    def main_loop(self):
        while True:
            self.render()
            self.events()
            self.update()

if __name__ == "__main__":
    simulation = Main()
    simulation.main_loop()