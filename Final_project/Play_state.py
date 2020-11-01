import random
import gfw
import gfw_world
from pico2d import *
from player import Player
from bullet import LaserBullet
import enemy_gen
import gobj

canvas_width = 750
canvas_height = 1000

def enter():
    gfw_world.init(['bg', 'enemy', 'bullet', 'player'])
    global player
    player = Player()
    gfw_world.add(gfw.layer.player, player)

def update():
    gfw_world.update()
    enemy_gen.update()
    #print(gfw.delta_time)
    
def draw():
    gfw_world.draw()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
