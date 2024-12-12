import pygame
from camera import *

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # Sprite sheets for animations
        self.sprite_sheets = []

        # Individual animation frames
        self.animations = {
            "idle_ne": [], "idle_nw": [], "idle_se": [], "idle_sw": [],
            "walk_ne": [], "walk_nw": [], "walk_se": [], "walk_sw": [],
            "run_ne":  [], "run_nw":  [], "run_se":  [], "run_sw":  []
        }
        
        self.cur_animation = "idle_ne"

        # Current image and rect
        self.image = None
        self.rect = None

        # Animation properties
        self.anim_timer = 0
        self.frame_time = 0.15
        self.frame_index = 0

    # Load animations as individual frames
    def load_anim(self, frame_size):
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
            sheet_width = self.sprite_sheets[i].get_size()[0]
            frame_width, frame_height = frame_size

            for x in range(0, sheet_width, frame_width):
                # Create a surface for individual frame
                frame_surface = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
                frame_surface.blit(self.sprite_sheets[i], (0, 0),                 
                    pygame.Rect(x, 0, frame_width, frame_height)
                )
                
                # Add the frame to the corresponding animation
                self.animations[animation_key].append(frame_surface)


    # Render the creatures
    def render(self, screen):
        # Update timer by delta time
        self.anim_timer += 1 / 60

        # Update frames after every frame time
        if self.anim_timer >= self.frame_time:
            anim = self.animations[self.cur_animation]

            # Go to the next frame
            self.anim_timer = 0
            self.frame_index = (self.frame_index + 1) % len(anim)
            self.image = anim[self.frame_index]

        Camera.apply(self.image, self.rect, screen)