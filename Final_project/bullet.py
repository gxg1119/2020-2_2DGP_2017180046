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
        self.Shoot_state = 1
        self.Dualshoot_time = 3

    def draw(self):
        if self.Shoot_state == 1 and self.Dualshoot_time > 0:
            self.image.draw(self.x-50, self.y + 75)
            self.image.draw(self.x+50, self.y + 75)
        else:
            self.image.draw(self.x, self.y + 75)

    def update(self):
        self.y += self.dy * gfw.delta_time
        self.Dualshoot_time -= gfw.delta_time
        print(self.Dualshoot_time)
        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

        if self.Shoot_state == 1:
            pass
    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = LaserBullet.SIZE
        hh = LaserBullet.SIZE
        return self.x - hw, self.y + 75 - hh, self.x + hw, self.y + 75 + hh    
