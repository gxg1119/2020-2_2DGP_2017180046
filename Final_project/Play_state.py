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

boss_ox = 0
boss_ap = 1

def enter():
    gfw.world.init(['bg', 'enemy', 'boss', 'bullet', 'player','boss_bullet', 'ui', 'item'])
    global player
    player = Player()
    Player.player_type = 2
    gfw.world.add(gfw.layer.player, player)

    global dis_score, score
    dis_score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, dis_score)
    score = Score(canvas_width - 20, canvas_height - 100)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/BM.ttf', 40)

    life_gauge.load()

    bg=VertScrollBackground('/map_01.png')
    bg.speed = 100
    gfw.world.add(gfw.layer.bg,bg)

    global power_item
    power_item = gfw.image.load(gobj.RES_DIR + '/powershot.png')

    global music_bg, wav_item, wav_mon_die, player_voice, wav_boss_appear, wav_boss_dead, wav_siren, get_money, get_item
    music_bg = load_music(gobj.RES_DIR +'/bg_music.mp3')
    wav_mon_die = load_wav(gobj.RES_DIR +'/enemy_die.wav')
    player_voice = load_wav(gobj.RES_DIR +'/go.wav')
    wav_siren = load_wav(gobj.RES_DIR +'/siren.wav')
    wav_boss_appear = load_wav(gobj.RES_DIR +'/go.wav')
    wav_boss_dead = load_wav(gobj.RES_DIR +'/boss_dead.wav')
    get_money = load_wav(gobj.RES_DIR +'/get_coin.wav')
    get_item = load_wav(gobj.RES_DIR +'/get_item.wav')
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
                wav_boss_dead.play()
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
        score.score += 100
        if i.item_val == 1:
            get_money.play()
        if i.item_val == 2:
            get_item.play()
            if LaserBullet.powershoot_time == 0: 
                LaserBullet.Shoot_state = 1
                LaserBullet.Dualshoot_time = 20
        i.remove()

def update():
    dis_score.score += 10
    global boss_ox, boss_ap
    gfw.world.update()

    level = enemy_gen.enemy_level()
    
    boss_ox += gfw.delta_time

    if boss_ox < 12:
        enemy_gen.update()
        print(boss_ox)

    else :
        if boss_ap > 0 :
            #for i in [0,1,2,3,4]:
                #wav_siren.play(i)
            wav_boss_appear.play()
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
