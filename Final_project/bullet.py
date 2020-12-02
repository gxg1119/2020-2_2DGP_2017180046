from pico2d import *
import gfw
from gobj import *
from item import Item, Dual

class LaserBullet:
    Dualshoot_time = 5
    powershoot_time = 0
    Shoot_state = 0
    Power = 50
    SIZE = 50
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/bullet_01.png')
        self.pwimage = gfw.image.load(RES_DIR + '/bullet_powershot.png')
        #self.power = 50

    def draw(self):
        if LaserBullet.Shoot_state == 1:
            self.image.draw(self.x-50, self.y + 75)
            self.image.draw(self.x+50, self.y + 75)
        elif LaserBullet.Shoot_state == 2:
            self.pwimage.draw(self.x, self.y + 150, 510, 744)
        else:
            self.image.draw(self.x, self.y + 75)

    def update(self):
        self.y += self.dy * gfw.delta_time
        print(LaserBullet.powershoot_time)
        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

        if LaserBullet.Shoot_state == 2:
            LaserBullet.SIZE = 200
            LaserBullet.powershoot_time += gfw.delta_time
            if LaserBullet.powershoot_time > 20 :
                LaserBullet.powershoot_time = 0
                LaserBullet.Shoot_state = 0
                LaserBullet.Power = 50
                LaserBullet.SIZE = 50

        if LaserBullet.Shoot_state == 1:
            LaserBullet.Dualshoot_time -= gfw.delta_time
            if LaserBullet.Dualshoot_time < 0 :
                LaserBullet.Dualshoot_time = 20
                LaserBullet.Shoot_state = 0


    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = LaserBullet.SIZE
        hh = LaserBullet.SIZE
        return self.x - hw, self.y + 75 - hh, self.x + hw, self.y + 75 + hh    
