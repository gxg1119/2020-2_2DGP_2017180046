from pico2d import *
import gfw
from gobj import *
import random
import life_gauge
import item
import effect


class Enemy:
    SIZE = 50
    effect_ox = False

    def __init__(self, x, speed, level):
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

        self.effect_image = gfw.image.load(RES_DIR + '/effect.png')
        self.effect_time = 0
        self.efdx = 0

        self.item_gen = random.randint(1, 2)
        
    def draw(self):
        sx = self.fidx * self.src_width
        self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y)
        gy = self.y - Enemy.SIZE - 10
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, 100, rate)

    def update(self):
        self.time += gfw.delta_time
        self.effect_time += gfw.delta_time
        self.fidx = int(self.time * 10) % 2
        self.efdx = int(self.effect_time * 20) % 8
        self.y += self.dy * gfw.delta_time * 120
        if self.y < -Enemy.SIZE:
            self.remove()
            
    def remove(self):
        gfw.world.remove(self)
        item.Item.generate(self, self.x, self.y)
        item.Dual.generate(self)

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def score(self):
        return self.max_life

    def get_bb(self):
        half = Enemy.SIZE
        return self.x - half, self.y - half, self.x + half, self.y + half


