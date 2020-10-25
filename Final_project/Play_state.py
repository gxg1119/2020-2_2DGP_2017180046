import random
import gfw
import gfw_world
from pico2d import *
from player import Player
from bullet import LaserBullet
from enemy import Enemy
import gobj

canvas_width = 750
canvas_height = 1000

def enter():
    global player
    player = Player()
    gfw_world.add(player)

    set_next_enemy_gen_time()

def set_next_enemy_gen_time():
    global enemy_gen_time
    enemy_gen_time = random.uniform(1, 2)
    
def generate_enemy_if_timed_out():
    global enemy_gen_time
    enemy_gen_time -= gfw.delta_time
    if enemy_gen_time > 0: return

    x = random.randint(0, get_canvas_width())
    e = Enemy(x, -1)
    
    gfw_world.add(e)
    set_next_enemy_gen_time()

def update():
    gfw_world.update()
    
    generate_enemy_if_timed_out()
    
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
