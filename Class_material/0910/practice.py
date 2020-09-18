import pico2d
pico2d.open_canvas()
pico2d.close_canvas()

import pico2d as p
p.open_canvas()
p.close_canvas()

from random import randint
print(randint(1, 6))

from random import randint as ri
print(ri(1, 6))

from random import *
print(uniform(1, 2))
print(randrange(10, 20))

import os
print(os.getcwd())
print(os.listdir())


from pico2d import *

open_canvas()
os.chdir('C:/Users/User/Desktop/투디겜플/img')
print(os.listdir())
image = load_image('../img/cat.jpg')
image.draw_now(400, 300)

delay(3)

hide_lattice()
show_lattice()

open_canvas()
image = load_image('../img/character.png')
image.draw_now(300, 200)
image.draw_now(400, 300)
for x in range(100, 701, 100):
    image.draw_now(x, 500)
    
for x in range(100, 701, 30):
    image.draw_now(x, 100)

clear_canvas_now()
for y in range(100, 501, 80):
    for x in range(100, 701, 35):
        image.draw_now(x, y)

grass = load_image('../img/grass.png')
grass.draw_now(400, 90)

delay(2)

close_canvas()
