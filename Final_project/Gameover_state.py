import gfw
from pico2d import *
from gobj import *
import highscore

def enter():
    gfw.world.init(['highscore'])

    global image
    image = gfw.image.load(RES_DIR + '/map_02.png')

    global font
    font = gfw.font.load(RES_DIR + '/BM.ttf', 30)

    highscore.load()
    gfw.world.add(gfw.layer.highscore, highscore)

def update():
    pass

def draw():
    image.draw(get_canvas_width()//2,get_canvas_height()//2)
    gfw.world.draw()

    font.draw(150, 700, 'socre',(255,255,255))

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
        gfw.pop()

def exit():
	pass
def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()