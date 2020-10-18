import gfw
import gfw_image
from pico2d import *
from gobj import *
import Play_state

def enter():
    global image, game_start_box, game_end_box
    image = gfw_image.load_image(RES_DIR + '/Title.png')
    game_start_box = load_image(RES_DIR + '/Gamestart.png')
    game_end_box = load_image(RES_DIR + '/Gameend.png')

def update():
    pass

def draw():
    image.draw(375, 500)
    game_start_box.draw(200,150)
    game_end_box.draw(550,150)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
        if(e.x >= 50 and e.x<=350 and e.y <= 925 and e.y >= 775):
            gfw.push(Play_state)
        elif(e.x >= 400 and e.x<=700 and e.y <= 925 and e.y >= 775):
            gfw.quit()
            
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
