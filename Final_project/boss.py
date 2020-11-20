from pico2d import *
import gfw
from gobj import *

class Boss:
	SIZE = 100

	def __init__(self):
		self.x, self.y = 375, get_canvas_height()-100
		self.dy = 0
		self.image = gfw.image.load(RES_DIR + '/boss.png')
		self.src_width = self.image.w // 2
		self.src_height = self.image.h
		self.life = 3000
		self.fidx = 0
		self.boss_time = 0

	def draw(self):
		sx = self.fidx * self.src_width
		self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y)

	def update(self):
		global dy
		self.boss_time += gfw.delta_time
		self.fidx = int(self.boss_time * 10) % 2
		self.y += self.dy * gfw.delta_time
		if self.y < 700 : self.dy = 0

	def remove(self):
		gfw.world.remove(self)

	def get_bb(self):
		pass