import gfw
from pico2d import *
from gobj import *
import highscore

num = 0

def enter():
    gfw.world.init(['highscore'])

    global image, sdimage_1, sdimage_2
    image = gfw.image.load(RES_DIR + '/Gameoverbg.png')
    sdimage_1 = gfw.image.load(RES_DIR + '/sd_01.png')
    sdimage_2 = gfw.image.load(RES_DIR + '/sd_02.png')

    global font
    font = gfw.font.load(RES_DIR + '/BM.ttf', 100)

    global sdnum
    sdnum = num

    highscore.load()
    gfw.world.add(gfw.layer.highscore, highscore)

def update():
    pass

def draw():
    image.draw(get_canvas_width()//2,get_canvas_height()//2)
    if sdnum == 0:
        sdimage_1.draw(550, 200)
    else : sdimage_2.draw(550, 200)

    gfw.world.draw()

    font.draw(100, 800, 'socre',(225,225,225))

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
        gfw.pop()

def exit():
    global image, sdimage_1, sdimage_2
    del image
    del sdimage_1
    del sdimage_2

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()