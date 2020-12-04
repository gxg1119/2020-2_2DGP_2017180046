import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
import gobj
from enemy import Enemy
import enemy_gen
import life_gauge
import boss
from item import Item, Dual
from background import VertScrollBackground
import effect
import random
import highscore
import Gameover_state


canvas_width = 750
canvas_height = 1000
charnum = 0

START_GAME, END_GAME = range(2)

def enter():
    gfw.world.init(['bg', 'enemy', 'boss', 'bullet', 'player','boss_bullet','effect', 'ui', 'item'])
    global player, charnum
    player = Player()
    Player.player_type = charnum
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

    global power_item, dual_item
    power_item = gfw.image.load(gobj.RES_DIR + '/powershot.png')
    dual_item = gfw.image.load(gobj.RES_DIR + '/dualshot.png')

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

    global state
    state = START_GAME
    enemy_gen.reset()

    global boss_ox, boss_ap
    boss_ox, boss_ap = 0, 1

    global time, boss_die
    time = 0
    boss_die = False
    highscore.load()

    Gameover_state.num = charnum
    
def check_enemy(e):
    global state
    if gobj.collides_box(player, e):
        e.remove()
        player.damage_ox = True
        player_dead = player.decrease_life()
        if player_dead:
            state = END_GAME       

    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            enemy_dead = e.decrease_life(b.Power)
            if enemy_dead:
                effect.Effect(e.x,e.y, 0).generate()
                score.score += e.level * 100
                wav_mon_die.play()
                e.remove()
            b.remove()

def check_boss(boss):
    global boss_die
    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, boss):
            boss_dead = boss.decrease_life(b.Power)
            if boss_dead:
                effect.Effect(boss.x, boss.y, 1).generate()
                wav_boss_dead.play()
                score.score += 50000
                boss.remove()
                boss_die = True
            b.remove()

    for bb in gfw.world.objects_at(gfw.layer.boss_bullet):
        if gobj.collides_box(bb, player):
            bb.remove()
            player_dead = player.decrease_life()
            if player_dead:
                state = END_GAME

def check_item(i):
    global player
    if gobj.collides_box(player, i):
        score.score += 100
        if i.item_val == 1:
            get_money.play()
        if i.item_val == 2:
            if player.dualshoot_cnt < 10:
                player.dualshoot_cnt += 1
            get_item.play()
        i.remove()

def endgame():
    global state
    state = END_GAME
    music_bg.stop()
    gfw.change(Gameover_state)
    highscore.add(score.score)

def update():
    global state
    if state != START_GAME:
        endgame()
        return

    global time, boss_die
    if boss_die :
        time += gfw.delta_time
    if time > 8:
        state = END_GAME

    dis_score.score += 10
    global boss_ox, boss_ap
    gfw.world.update()
    
    boss_ox += gfw.delta_time

    if boss_ox < 10:
        enemy_gen.update()

    else :
        if boss_ap > 0 :
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
    dual_item.draw(canvas_width - 100, 105, 50, 50)
    font.draw(canvas_width - 70, 50, ': %d' % player.powershoot_cnt,(255,255,255))
    font.draw(canvas_width - 70, 105, ': %d' % player.dualshoot_cnt,(255,255,255))

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
