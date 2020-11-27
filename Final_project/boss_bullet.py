from pico2d import *
import gfw
from gobj import *

class Boss_Bullet:

    SIZE = 10
    def __init__(self, x, y, direction, speed):
        self.x, self.y = x, y
        self.dx, self.dy = direction, speed
        self.image = gfw.image.load(RES_DIR + '/boss_bullet.png')
        self.side = random.randint(1, 5)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        x, y = self.x, self.y
        dx, dy = self.dx, self.dy
        x += dx * gfw.delta_time
        y -= dy * gfw.delta_time

        self.x, self.y = x, y

        if self.side == 1: self.dx = -100
        elif self.side == 2: self.dx = 100
        elif self.side == 3: self.dx = 200
        elif self.side == 4: self.dx = -200
        else : self.dx = 0

        if self.y > get_canvas_height() + Boss_Bullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = Boss_Bullet.SIZE
        hh = Boss_Bullet.SIZE
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh    