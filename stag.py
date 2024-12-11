from creature import *

class Stag(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Idle animations
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NE_idle.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NW_idle.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SE_idle.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SW_idle.png"))
        
        # Walk animations
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NE_walk.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NW_walk.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SE_walk.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SW_walk.png"))

        # Run animations
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NE_run.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NW_run.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SE_run.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SW_run.png")) 

        # Load the animations
        self.anim_sprite.load_anim((32, 41))
        self.anim_sprite.image = self.anim_sprite.animations[self.anim_sprite.cur_animation][0]
        self.anim_sprite.rect = self.anim_sprite.image.get_rect()
        self.anim_sprite.rect.topleft = [x, y]

        self.anim_sprite.frame_time = 0.15

