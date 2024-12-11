from creature import *

class Wolf(Creature):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, *groups)

        