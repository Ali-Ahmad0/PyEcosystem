from creature import *

class Stag(Creature):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, *groups)

        # Idle animations
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NE_idle.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NW_idle.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SE_idle.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SW_idle.png"))
        
        # Walk animations
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NE_walk.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NW_walk.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SE_walk.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SW_walk.png"))

        # Run animations
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NE_run.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_NW_run.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SE_run.png"))
        self.sprite_sheets.append(pygame.image.load("assets/sprites/stag/critter_stag_SW_run.png")) 

        self.frame_size = (32, 41)

        super.load_anim()
