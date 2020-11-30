import random
from pico2d import *
import gfw
from gobj import *
from bullet import *

MAX_LIFE = 3

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  -1,
        (SDL_KEYDOWN, SDLK_RIGHT): 1,
        (SDL_KEYUP, SDLK_LEFT): 1,
        (SDL_KEYUP, SDLK_RIGHT):   -1,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    LASER_INTERVAL = 0.1

    #constructor
    def __init__(self):
        self.x, self.y = 375, 150
        self.dx = 0
        self.speed = 750
        self.image = gfw.image.load(RES_DIR + '/Player_01.png')
        half = self.image.w
        self.minx = 75
        self.maxx = 675
        self.fidx = 0
        
        self.player_time =0
        self.laser_time = 0

        self.life = MAX_LIFE
        self.hp_1 = gfw.image.load(RES_DIR + '/hp_heart_01.png')
        self.hp_2 = gfw.image.load(RES_DIR + '/hp_heart_02.png')

        self.damage_time = 0
        self.damage = gfw.image.load(RES_DIR + '/damage.png')
        
    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.x, self.y, 1000)
        gfw.world.add(gfw.layer.bullet, bullet)

    def decrease_life(self):
        self.life -= 1
        print(self.life)
        return self.life <= 0
        
    def draw(self):
        self.image.clip_draw(self.fidx*150, 0, 150, 150, self.x, self.y)
        
        global MAX_LIFE
        self.hx, self.hy = get_canvas_width() // 2 + 45, 50
        for i in range(MAX_LIFE):
            self.hp = self.hp_1 if i < self.life else self.hp_2
            self.hp.draw(self.hx, self.hy, 40, 40)
            self.hx -= self.hp.w + 10

    def update(self):
        self.x += self.dx * self.speed * gfw.delta_time
       # self.fidx = (self.fidx+1)%8
        self.player_time += gfw.delta_time
        self.laser_time += gfw.delta_time
        frame = self.player_time * 10
        self.fidx=int(frame) % 8
        
        if self.x < self.minx: self.x = self.minx
        elif self.x > self.maxx: self.x = self.maxx

        if self.laser_time >= Player.LASER_INTERVAL:
            self.fire()
            
    def handle_event(self, e):
        pair = (e.type, e.key)
        if(pair in Player.KEY_MAP):
            self.dx += Player.KEY_MAP[pair]
        if pair == (SDL_KEYDOWN, SDLK_SPACE):
            print("space")

    def get_bb(self):
        hw = 30
        hh = 40
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh
