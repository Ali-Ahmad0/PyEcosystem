import pygame
from camera import *

class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        
        # TO DO: implement this
        self.speed = 0
        self.stamina = 0
        
        self.max_hunger = 0
        self.cur_hunger = 0

        self.max_thirst = 0
        self.cur_thirst = 0

        # Sprite sheets for animations
        self.sprite_sheets = []

        # Size of each frame
        self.frame_size = (0, 0)
        
        # Individual animation frames
        self.animations = {
            "idle_ne": [], "idle_nw": [], "idle_se": [], "idle_sw": [],
            "walk_ne": [], "walk_nw": [], "walk_se": [], "walk_sw": [],
            "run_ne":  [], "run_nw":  [], "run_se":  [], "run_sw":  []
        }
        
        self.curr_animation = "idle_ne"
        self.curr_frame = 0

        # Current image and rect
        self.image = None
        self.rect = None

    # Load animations as individual frames
    def load_anim(self):
        directions = ["ne", "nw", "se", "sw"]
        actions = ["idle", "walk", "run"]

        for i in range(len(self.sprite_sheets)):
            # Get the name of animation
            action_index = i // 4
            direction_index = i % 4

            action = actions[action_index]
            direction = directions[direction_index]
            animation_key = f"{action}_{direction}"

            # Get sheet and frame dimensions
            sheet_width, sheet_height = self.sprite_sheets[i].get_size()
            frame_width, frame_height = self.frame_size

            # Get number of rames
            num_frames = sheet_width // frame_width

            # for x in range(num_frames):
            #     frame_rect = pygame.Rect(
            #         x * frame_width, frame_height, frame_width, frame_height
            #     )
            #     frame = self.sprite_sheets[i].subsurface(frame_rect).copy()
            #     self.animations[animation_key].append(frame)

            for x in range(0, sheet_height, frame_width):
                # Create a surface for individual frame
                frame_surface = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
                frame_surface.blit(self.sprite_sheets[i], (0, 0),                 
                    pygame.Rect(x, 0, frame_width, frame_height)
                )
                
                # Add the frame to the corresponding animation
                self.animations[animation_key].append(frame_surface)


    def render(self, screen):
        Camera.apply(self.image, self.rect, screen)
        
