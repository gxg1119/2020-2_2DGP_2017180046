import gfw
from pico2d import *
from gobj import *
import Play_state

def enter():
	global boximage, chimage, chsimage, x, y, dy
	boximage = gfw.image.load_image(RES_DIR + '/box_01.png')
	chimage = gfw.image.load_image(RES_DIR + '/character_01.png')
	chsimage = gfw.image.load_image(RES_DIR + '/select_character_01.png')
	x, y = get_canvas_width() // 2, get_canvas_height() // 2
	dy = 0.5
def update():
    global y, dy
    print(y)
    y += dy
    if y < 490 or y > 510: dy *= -1

def draw():
	global x, y
	chimage.draw(x, y, 700, 700)
	boximage.draw(get_canvas_width() // 2, 150,700,150)
	chsimage.draw(get_canvas_width() // 2, 150)

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