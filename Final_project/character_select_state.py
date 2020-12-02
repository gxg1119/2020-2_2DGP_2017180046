import gfw
from pico2d import *
from gobj import *
import Play_state

def enter():
    global image, x, y, dy, num , chimage1, chimage2
    image = gfw.image.load_image(RES_DIR + '/sel.png')
    chimage1 = gfw.image.load_image(RES_DIR + '/character_01.png')
    chimage2 = gfw.image.load_image(RES_DIR + '/character_02.png')
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    num = 0

def update():
    pass
def draw():
    global x, y, num
    if num == 0 :
        chimage1.draw(x, y)
    else : 
        chimage2.draw(x, y)

    image.clip_draw(0 + 750 * num, 0, 750, 1000, x, y)
    
def handle_event(e):
    global num
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
        num = 0
        Play_state.charnum = 0
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHT):
        num = 1
        Play_state.charnum = 1
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