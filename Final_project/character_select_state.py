import gfw
from pico2d import *
from gobj import *
import Play_state

def enter():
	pass

def update():
    pass

def draw():
	pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
            gfw.push(Play_state)
            
def exit():
	pass

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()