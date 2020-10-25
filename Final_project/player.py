import random
from pico2d import *
import gfw
import gfw_image
import gfw_world
from gobj import *
from bullet import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  -1,
        (SDL_KEYDOWN, SDLK_RIGHT): 1,
        (SDL_KEYUP, SDLK_LEFT): 1,
        (SDL_KEYUP, SDLK_RIGHT):   -1,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    LASER_INTERVAL = 0.05

    #constructor
    def __init__(self):
        self.x, self.y = 250, 90
        self.dx = 0
        self.speed = 10
        self.image = gfw_image.load(RES_DIR + '/Player_01.png')
        half = self.image.w
        self.minx = 75
        self.maxx = 675
        self.fidx = 0
        
        self.player_time =0
        self.laser_time = 0
        
    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.x, self.y, 5)
        gfw_world.add(bullet)
        
    def draw(self):
        self.image.clip_draw(self.fidx*150, 0, 150, 150, self.x, self.y)
            
    def update(self):
        self.x += self.dx * self.speed
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
