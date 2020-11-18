from pico2d import *
import gfw
from gobj import *
import life_gauge
import money


class Enemy:
    enemies = []
    trashcan = []
    SIZE = 50
    def __init__(self, x, speed, level):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, get_canvas_height() + Enemy.SIZE
        self.dx, self.dy = 0, speed
        self.level = level
        self.max_life = level * 100
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/dragon_%02d.png' %level)
        self.fidx = 0
        self.src_width = self.image.w // 2
        self.src_height = self.image.h
        self.time = 0
        
    def draw(self):
        sx = self.fidx * self.src_width
        self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y)
        gy = self.y - Enemy.SIZE - 10
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, 100, rate)

    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 10) % 2
        # self.x += self.dx
        self.y += self.dy * gfw.delta_time * 200
        
        if self.y < -Enemy.SIZE:
            self.remove()
            
    def remove(self):
        gfw.world.remove(self)
        money.Money.generate(self)
        #print(self.money)
        
    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def score(self):
        return self.max_life

    def get_bb(self):
        half = Enemy.SIZE
        return self.x - half, self.y - half, self.x + half, self.y + half


