from pico2d import *
import gfw
from gobj import *

class Boss_Bullet:

    SIZE = 50
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/boss_bullet.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.dy * gfw.delta_time

        if self.y > get_canvas_height() + Boss_Bullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = Boss_Bullet.SIZE
        hh = Boss_Bullet.SIZE
        return self.x - hw, self.y + 75 - hh, self.x + hw, self.y + 75 + hh    