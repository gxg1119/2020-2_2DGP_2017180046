from pico2d import *
import random

class Boy:
    def __init__(self):
        #self.x, self.y = get_canvas_width() //2, 85
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 700)
        self.img = load_image('../img/run_animation.png')
        self.dx = random.random()
        self.fidx = random.randint(0, 7)        
    def draw(self):
        self.img.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.fidx = (self.fidx + 1) % 8
        self.x += self.dx*5

class Grass:
    def __init__(self):
        self.img = load_image('../img/grass.png')
        self.x, self.y = 400, 30
    def draw(self):
        self.img.draw(self.x, self.y)
# print("Hello")

if(__name__ == '__name__'):
    print("Not imported")
