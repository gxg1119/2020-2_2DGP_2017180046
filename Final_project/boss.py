from pico2d import *
import gfw
from gobj import *
import life_gauge

class Boss:
	SIZE = 100
	def __init__(self):
		self.x, self.y = 375, get_canvas_height()
		self.dy = 0
		self.image = gfw.image.load(RES_DIR + '/boss.png')
		self.src_width = self.image.w // 2
		self.src_height = self.image.h
		self.life = 10000
		self.fidx = 0
		self.boss_time = 0

	def draw(self):
		sx = self.fidx * self.src_width
		self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y,600,400)
		life_gauge.draw(self.x-10, self.y-10,10,10)

	def update(self):
		global dy
		self.boss_time += gfw.delta_time
		self.fidx = int(self.boss_time * 5) % 2
		self.y += self.dy * gfw.delta_time
		if self.y < 700 : self.dy = 0

	def decrease_life(self, amount):
		self.life -= amount
		print(self.life)
		return self.life <= 0

	def score(self):
		return self.life

	def remove(self):
		gfw.world.remove(self)

	def get_bb(self):
		half = Boss.SIZE
		return self.x - half, self.y - half, self.x + half, self.y + half