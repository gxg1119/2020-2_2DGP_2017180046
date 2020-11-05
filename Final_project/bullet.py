from pico2d import *
import gfw
import gfw_image
import gfw_world
from gobj import *

class LaserBullet:
    bullets = []
    trashcan = []
    SIZE = 50
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw_image.load(RES_DIR + '/bullet_01.png')

    def draw(self):
        self.image.draw(self.x, self.y + 75)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw_world.remove(self)

    def get_bb(self):
        hw = LaserBullet.SIZE
        hh = LaserBullet.SIZE
        return self.x - hw, self.y + 75 - hh, self.x + hw, self.y + 75 + hh    
