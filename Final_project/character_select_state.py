import gfw
from pico2d import *
from gobj import *
import Play_state

def enter():
    global image, x, y, chx, chy, dy, num , chimage1, chimage2, bgimage, koimage, time
    image = gfw.image.load_image(RES_DIR + '/aa.png')
    bgimage = gfw.image.load_image(RES_DIR + '/map_01.png')
    chimage1 = gfw.image.load_image(RES_DIR + '/character_01.png')
    chimage2 = gfw.image.load_image(RES_DIR + '/character_02.png')
    koimage = gfw.image.load_image(RES_DIR + '/ko2.png')
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    chx, chy = get_canvas_width() // 2, get_canvas_height() // 2
    dx = 0
    dy = 0.5
    num = 0
    Play_state.charnum = 0
    time = 0

    global botton_sd
    botton_sd = load_wav(RES_DIR +'/button.wav')

def update():
    global chy ,dx, dy, time
    time += gfw.delta_time * 3
    dx = int(time) % 2
    chy += dy
    if chy < 490 or chy > 510 : dy *= -1
    
def draw():
    global x, y, num
    bgimage.draw(x, y)
    if num == 0 :
        chimage1.draw(chx, chy+100)
    else : 
        chimage2.draw(chx + 100, chy)

    koimage.clip_draw(dx * 650,0,650,150,x, y + 400)
    image.clip_draw(0 + 750 * num, 0, 750, 1000, x, y)
    
def handle_event(e):
    global num

    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
        num = 0
        Play_state.charnum = 0
        botton_sd.play()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHT):
        num = 1
        Play_state.charnum = 1
        botton_sd.play()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
            gfw.change(Play_state)
            
def exit():
	pass

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()