import pygame

class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        
        # TO DO: implement this
        self.speed
        self.stamina
        
        self.max_hunger
        self.cur_hunger

        self.max_thirst
        self.cur_thirst

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

            for x in range(num_frames):
                frame_rect = pygame.Rect(
                    x * frame_width, frame_height, frame_width, frame_height
                )
                frame = self.sprite_sheets[i].subsurface(frame_rect).copy()
                self.animations[animation_key].append(frame)


    def animate(self, speed):
        pass
