import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
import gobj
import enemy_gen
import boss_gen
import life_gauge
import boss
from background import VertScrollBackground

canvas_width = 750
canvas_height = 1000

boss_ox = True
def enter():
    gfw.world.init(['bg', 'enemy', 'boss','bullet', 'player', 'ui', 'money'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global boss
    boss = boss.Boss()
    boss.dy = -50
    gfw.world.add(gfw.layer.boss, boss)

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/barun.ttf', 40)

    life_gauge.load()

    bg=VertScrollBackground('/map_01.png')
    bg.speed = 100
    gfw.world.add(gfw.layer.bg,bg)
    
def check_enemy(e):
    if gobj.collides_box(player, e):
        #print('Player Collision', e)
        e.remove()
        return

    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            #print('Collision', e, b)
            dead = e.decrease_life(b.power)
            if dead:
                score.score += e.level * 100
                e.remove()
            b.remove()
            return

def check_boss(boss):
    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, boss):
            boss_dead = boss.decrease_life(b.power)
            if boss_dead:
                score.score += 10000
                boss.remove()
            b.remove()
            return

def check_money(m):
    if gobj.collides_box(player, m):
        m.remove()
        return

def update():
    global boss_ox
    gfw.world.update()

    if boss_ox == True:
        enemy_gen.update()

    level = enemy_gen.enemy_level()

    if level > 5:
        boss_ox = False
        boss.update()
    
    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)
    for m in gfw.world.objects_at(gfw.layer.money):
        check_money(m)
    for e_b in gfw.world.objects_at(gfw.layer.boss):
        check_boss(e_b)
    
def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()
    font.draw(20, canvas_height - 45, 'Wave: %d' % enemy_gen.wave_index)

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
