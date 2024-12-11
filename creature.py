import pygame
from animated_sprite import *
from camera import *

class Creature():
    def __init__(self, x, y):
        
        self.speed = 0
        self.stamina = 0
        
        self.max_hunger = 0
        self.cur_hunger = 0

        self.max_thirst = 0
        self.cur_thirst = 0

        # Sprite
        self.sprite_group = pygame.sprite.Group()
        self.anim_sprite = AnimatedSprite(self.sprite_group)
        
    def render(self, screen):
        self.anim_sprite.render(screen)