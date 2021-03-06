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
        speed = -(1 + wave_index//25)
        e = Enemy(x, speed, level)
        gfw.world.add(gfw.layer.enemy, e)

    wave_index += 1
    next_wave = 3

LEVEL_ADJUST_PERCENTS = [ 10, 20 ,30 ,40, 50 ]

def enemy_level():
    level = (wave_index - 5) // 5
    percent = random.randrange(100)
    for p in LEVEL_ADJUST_PERCENTS:
        if percent < p:break
        percent -= p
        level += 1
    if level < 1 : level = 1
    if level > 5 : level = 5
    return level

def reset():
    global wave_index, next_wave
    wave_index, next_wave = 0, 0