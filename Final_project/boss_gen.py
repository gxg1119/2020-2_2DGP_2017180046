import random
import gfw
from pico2d import *
from boss import Boss

def update():
    generate()

def generate():
    boss_moster = Boss()
    gfw.world.add(gfw.layer.boss, boss_moster)