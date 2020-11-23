import random
import gfw
from pico2d import *
from enemy import Enemy

GEN_X  = [75, 225, 375, 525, 675]
next_wave = 0
wave_index = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave
    
    for x in GEN_X:
        level = enemy_level()
        speed = -(1 + wave_index/20)
        e = Enemy(x, speed, level)
        gfw.world.add(gfw.layer.enemy, e)

    #print(wave_index, level)
    wave_index += 1
    next_wave = random.uniform(3, 4)

def enemy_level():
    level = wave_index // 5
    level += 1
    return level