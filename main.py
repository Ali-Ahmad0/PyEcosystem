import pygame
from tilemap import *
from camera import *
from grid import *
from stag import *
from wolf import *

# Camera handling
last_zoom_time = 0
ZOOM_COOLDOWN = 150

def update_camera():
        global last_zoom_time
        keys = pygame.key.get_pressed()
        
        # Move camera
        camera_dx = 0
        camera_dy = 0

        if keys[pygame.K_LEFT]:
            camera_dx = -1.5
        if keys[pygame.K_RIGHT]:
            camera_dx = 1.5
        if keys[pygame.K_UP]:
            camera_dy = -1.5
        if keys[pygame.K_DOWN]:
            camera_dy = 1.5
        
        Camera.move(camera_dx, camera_dy)

        # Zoom
        current_time = pygame.time.get_ticks()
        if (current_time - last_zoom_time >= ZOOM_COOLDOWN):
            if keys[pygame.K_PAGEUP]:
                Camera.zoom += 1 if Camera.zoom < 4 else 0
                last_zoom_time = current_time

            if keys[pygame.K_PAGEDOWN]:
                Camera.zoom -= 1 if Camera.zoom > 1 else 0
                last_zoom_time = current_time

class Main():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Ecosystem")

        # Screen and clock
        self.screen = pygame.display.set_mode((540, 400))
        self.clock = pygame.time.Clock()

        # Initialize world map
        self.world_map = Tilemap("PyEcosystem/assets/tilemap/isometric_tileset.png", "PyEcosystem/assets/tilemap/tilemap.json")

        # Initialize grid with world_map
        self.grid = Grid(self.screen, self.world_map)
        self.stag = Stag(0, 0)
        self.wolf = Wolf(-16, 196)
        self.wolf.anim_sprite.cur_animation = "idle_se"

        self.grid.print_data()

    # Simulation render logic
    def render(self):
        self.screen.fill((0, 0, 0))
        self.world_map.render(self.screen)
        self.stag.render(self.screen)
        self.wolf.render(self.screen)

        pygame.display.update()

    # Pygame events handling
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # Simulation update logic
    def update(self):
        
        update_camera()
        
        self.clock.tick(60)

    def main_loop(self):
        while True:
            self.render()
            self.events()
            self.update()

if __name__ == "__main__":
    simulation = Main()
    simulation.main_loop()