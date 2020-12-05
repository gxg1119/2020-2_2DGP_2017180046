import random
from pico2d import *
import gfw
from gobj import *
from bullet import LaserBullet

MAX_LIFE = 3

class Player:
    player_type = 0

    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  -1.25,
        (SDL_KEYDOWN, SDLK_RIGHT): 1.25,
        (SDL_KEYUP, SDLK_LEFT): 1.25,
        (SDL_KEYUP, SDLK_RIGHT):   -1.25,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    LASER_INTERVAL = 0.08

    #constructor
    def __init__(self):
        self.x, self.y = 375, 150
        self.dx = 0
        self.speed = 750
        self.p1image = gfw.image.load(RES_DIR + '/Player_01.png')
        self.p2image = gfw.image.load(RES_DIR + '/Player_02.png')
        self.minx = 75
        self.maxx = 675
        self.fidx = 0
        
        self.player_time =0
        self.laser_time = 0

        self.life = MAX_LIFE
        self.hp_1 = gfw.image.load(RES_DIR + '/hp_heart_01.png')
        self.hp_2 = gfw.image.load(RES_DIR + '/hp_heart_02.png')

        self.damage_time = 0
        self.dfidx = 0
        self.damage_ox = False
        self.damage = gfw.image.load(RES_DIR + '/damage.png')

        self.dualshoot_cnt = 0
        self.powershoot_cnt = 9
        self.powershoot_wav = load_wav(RES_DIR +'/power_shot.wav')

    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.x, self.y, 1000)
        if Player.player_type == 0 : LaserBullet.bullet_type = 0
        else : LaserBullet.bullet_type = 1
        gfw.world.add(gfw.layer.bullet, bullet)

    def decrease_life(self):
        self.life -= 1
        return self.life <= 0
        
    def draw(self):
        if Player.player_type == 0 :
            self.p1image.clip_draw(self.fidx*150, 0, 150, 150, self.x, self.y)
        else : self.p2image.clip_draw(self.fidx*150, 0, 150, 150, self.x, self.y)

        global MAX_LIFE
        self.hx, self.hy = get_canvas_width() // 2 + 45, 50
        for i in range(MAX_LIFE):
            self.hp = self.hp_1 if i < self.life else self.hp_2
            self.hp.draw(self.hx, self.hy, 40, 40)
            self.hx -= self.hp.w + 10
        if self.damage_ox == True:
            if self.damage_time <= 3:
                self.damage.clip_draw(self.dfidx * 64, 0, 64, 64, self.x+40, self.y+50)
            else : self.damage_ox = False
        else : self.damage_time = 0

    def update(self):
        self.x += self.dx * self.speed * gfw.delta_time
        self.player_time += gfw.delta_time
        self.laser_time += gfw.delta_time
        self.damage_time += gfw.delta_time
        frame = self.player_time * 10
        self.fidx=int(frame) % 8
        
        if self.x < self.minx: self.x = self.minx
        elif self.x > self.maxx: self.x = self.maxx

        if self.laser_time >= Player.LASER_INTERVAL:
            self.fire()
        if self.damage_ox == True:
            self.damage_time += gfw.delta_time
            self.dfidx = int(self.damage_time * 2) % 2
            
    def handle_event(self, e):
        pair = (e.type, e.key)
        if(pair in Player.KEY_MAP):
            self.dx += Player.KEY_MAP[pair]
        if pair == (SDL_KEYDOWN, SDLK_SPACE):
            if self.powershoot_cnt > 0:
                self.powershoot_cnt -= 1
                LaserBullet.Shoot_state = 2
                LaserBullet.Power = 500
                self.powershoot_wav.play()
        if pair == (SDL_KEYDOWN, SDLK_LSHIFT):
            #print(self.dualshoot_cnt)
            if self.dualshoot_cnt > 0 :
                if LaserBullet.powershoot_time == 0 and self.dualshoot_cnt > 0: 
                    LaserBullet.Shoot_state = 1
                    LaserBullet.Dualshoot_time = 20

                self.dualshoot_cnt -= 1

    def get_bb(self):
        hw = 30
        hh = 40
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh
