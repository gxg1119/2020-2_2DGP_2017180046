from pico2d import *
import gfw
from gobj import *

class LaserBullet:

    SIZE = 50
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/bullet_01.png')
        self.power = 50

    def draw(self):
        self.image.draw(self.x, self.y + 75)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = LaserBullet.SIZE
        hh = LaserBullet.SIZE
        return self.x - hw, self.y + 75 - hh, self.x + hw, self.y + 75 + hh    
