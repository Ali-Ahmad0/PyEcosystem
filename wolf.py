from creature import *

class Wolf(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Idle animations
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-idle-NE.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-idle-NW.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-idle-SE.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-idle-SW.png"))

        # Run animations
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-run-NE.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-run-NW.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-run-SE.png"))
        self.anim_sprite.sprite_sheets.append(pygame.image.load("PyEcosystem/assets/sprites/wolf/wolf-run-SW.png"))

        # Load the animations
        self.anim_sprite.load_anim((64, 64))
        self.anim_sprite.image = self.anim_sprite.animations[self.anim_sprite.cur_animation][0]
        self.anim_sprite.rect = self.anim_sprite.image.get_rect()
        self.anim_sprite.rect.topleft = [x, y]