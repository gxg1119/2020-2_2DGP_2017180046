from pico2d import *
import gfw
from gobj import *
from item import Item

class LaserBullet:
    Dualshoot_time = 3

    SIZE = 50
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/bullet_01.png')
        self.power = 50
        self.Shoot_state = 0

    def draw(self):
        if self.Shoot_state and LaserBullet.Dualshoot_time > 0:
            self.image.draw(self.x-50, self.y + 75)
            self.image.draw(self.x+50, self.y + 75)
        else:
            self.image.draw(self.x, self.y + 75)

    def update(self):
        self.y += self.dy * gfw.delta_time
        print(LaserBullet.Dualshoot_time)
        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

        if self.Shoot_state == 5:
            LaserBullet.Dualshoot_time -= gfw.delta_time
            # LaserBullet.Dualshoot_time = 3
            if LaserBullet.Dualshoot_time < 0 :
                LaserBullet.Dualshoot_time = 3
                self.Shoot_state = 0

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = LaserBullet.SIZE
        hh = LaserBullet.SIZE
        return self.x - hw, self.y + 75 - hh, self.x + hw, self.y + 75 + hh    
