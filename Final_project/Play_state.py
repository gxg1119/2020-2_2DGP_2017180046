import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
import gobj

canvas_width = 750
canvas_height = 1000

def enter():
    global player
    player = Player()

def update():
    player.update()
    for b in LaserBullet.bullets: b.update()
    
def draw():
    for b in LaserBullet.bullets: b.draw()
    player.draw()

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
