import gfw
from pico2d import *
from gobj import *
import character_select_state

def enter():
    global image, game_start_box_01, game_end_box_01, game_start_box_02, game_end_box_02
    image = gfw.image.load_image(RES_DIR + '/Title.png')
    game_start_box_01 = load_image(RES_DIR + '/Gamestart.png')
    game_end_box_01 = load_image(RES_DIR + '/Gameend.png')
    game_start_box_02 = load_image(RES_DIR + '/st.png')
    game_end_box_02 = load_image(RES_DIR + '/ed.png')

    global music_bg, botton_sd
    music_bg = load_music(RES_DIR +'/Title_bg_music.mp3')
    botton_sd = load_wav(RES_DIR +'/button.wav')
    music_bg.repeat_play()

    global botton, start, end
    botton, start, end = 1, 1, 1

def update():
    pass

def draw():
    image.draw(375, 500)
    if start == 1: game_start_box_01.draw(200,150)
    else : game_start_box_02.draw(200,150)
    if end == 1: game_end_box_01.draw(550,150)
    else : game_end_box_02.draw(550,150)

def handle_event(e):
    global botton, start, end
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
        if(e.x >= 50 and e.x<=350 and e.y <= 925 and e.y >= 775):
            botton_sd.play()
            gfw.change(character_select_state)
        elif(e.x >= 400 and e.x<=700 and e.y <= 925 and e.y >= 775):
            botton_sd.play()
            gfw.quit()
    elif e.type == SDL_MOUSEMOTION:
        if(e.x >= 50 and e.x<=350 and e.y <= 925 and e.y >= 775):
            if botton > 0 : botton_sd.play()
            botton, start, end = (0, 0, 1)
        elif(e.x >= 400 and e.x<=700 and e.y <= 925 and e.y >= 775):
            if botton > 0 : botton_sd.play()
            botton, start, end = (0, 1, 0)
        else : botton, start, end = (1, 1, 1)
def exit():
    global image, game_start_box_01, game_end_box_01, game_start_box_02, game_end_box_02, music_bg, botton_sd
    del image
    del game_start_box_01
    del game_end_box_01
    del game_start_box_02
    del game_end_box_02
    del music_bg
    del botton_sd
    
def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
