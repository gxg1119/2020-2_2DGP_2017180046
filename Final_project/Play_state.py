import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
import gobj
import enemy_gen
import life_gauge
import boss
from item import Item, Dual
from background import VertScrollBackground
import random

canvas_width = 750
canvas_height = 1000

boss_ox = True
boss_ap = 1

def enter():
    gfw.world.init(['bg', 'enemy', 'boss', 'bullet', 'player','boss_bullet', 'ui', 'item'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/BM.ttf', 40)

    life_gauge.load()

    bg=VertScrollBackground('/map_01.png')
    bg.speed = 100
    gfw.world.add(gfw.layer.bg,bg)

    global power_item
    power_item = gfw.image.load(gobj.RES_DIR + '/powershot.png')

    global music_bg, wav_item, wav_mon_die, player_voice
    music_bg = load_music(gobj.RES_DIR +'/bg_music.mp3')
    wav_mon_die = load_wav(gobj.RES_DIR +'/enemy_die.wav')
    player_voice = load_wav(gobj.RES_DIR +'/go.wav')
    music_bg.repeat_play()
    player_voice.play()

def check_enemy(e):
    if gobj.collides_box(player, e):
        e.remove()
        player_dead = player.decrease_life()
        if player_dead:
            print('Dead')
        

    for b in gfw.world.objects_at(gfw.layer.bullet):     
        if gobj.collides_box(b, e):
            enemy_dead = e.decrease_life(b.Power)
            if enemy_dead:
                score.score += e.level * 100
                wav_mon_die.play()
                e.remove()
            b.remove()

def check_boss(boss):
    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, boss):
            boss_dead = boss.decrease_life(b.Power)
            if boss_dead:
                score.score += 1000000
                boss.remove()
            b.remove()

    for bb in gfw.world.objects_at(gfw.layer.boss_bullet):
        if gobj.collides_box(bb, player):
            bb.remove()
            player_dead = player.decrease_life()
            if player_dead:
                print("Dead")

def check_item(i):
    if gobj.collides_box(player, i):
        #if i.item_val == 1:
        score.score += 100
        if i.item_val == 2:
            if LaserBullet.powershoot_time == 0: 
                LaserBullet.Shoot_state = 1
                LaserBullet.Dualshoot_time = 20
        i.remove()

def update():
    global boss_ox, boss_ap
    gfw.world.update()

    if boss_ox == True:
        enemy_gen.update()
       
    level = enemy_gen.enemy_level()

    if level > 1:
        boss_ox = False
    if boss_ap > 0 :
        boss.Boss().generate()
        boss_ap -= 1
    
    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)
    for i in gfw.world.objects_at(gfw.layer.item):
        check_item(i)
    for e_b in gfw.world.objects_at(gfw.layer.boss):
        check_boss(e_b)
    
def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    font.draw(20, canvas_height - 45, 'Wave: %d' % enemy_gen.wave_index)
    power_item.draw(canvas_width - 100, 50, 50, 50)
    font.draw(canvas_width - 70, 50, ': %d' % player.powershoot_cnt,(255,255,255))
def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    #elif e.type == SDL_KEYDOWN:
    #    if e.key == SDLK_ESCAPE:
    #        gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
