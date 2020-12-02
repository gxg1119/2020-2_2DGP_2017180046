from pico2d import *
import gfw
from gobj import *
from boss_bullet import *
import life_gauge

appear_boss_time = 5

class Boss:
	SIZE = 100
	LASER_INTERVAL = 0.5

	def __init__(self):
		self.x, self.y = 375, get_canvas_height()+300
		self.dx, self.dy = 50, -50
		self.image = gfw.image.load(RES_DIR + '/boss.png')
		self.src_width = self.image.w // 2
		self.src_height = self.image.h
		self.max_life = 10000
		self.life = self.max_life
		self.fidx = 0
		self.boss_time = 0
		self.boss_laser_time = 0

	def draw(self):
		sx = self.fidx * self.src_width
		self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y,600,400)
		gy = self.y - Boss.SIZE - 50
		rate = self.life / self.max_life
		life_gauge.draw(self.x, gy, 300, rate)

	def update(self):
		global appear_boss_time
		appear_boss_time -= gfw.delta_time
		self.boss_laser_time += gfw.delta_time
		if appear_boss_time <0:
			self.boss_time += gfw.delta_time
			self.fidx = int(self.boss_time) % 2

			self.y += self.dy * gfw.delta_time
			if self.y < 700 :
				self.dy = 0
				self.x += self.dx * gfw.delta_time

				if self.x < 250 or self.x> 500:
					self.dx*=-1

			if self.boss_laser_time >= Boss.LASER_INTERVAL:
				self.fire()

	def fire(self):
		self.boss_laser_time = 0
		boss_bullet = Boss_Bullet(self.x, self.y, 100, 500)
		gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

	def generate(self):
		boss = Boss()
		gfw.world.add(gfw.layer.boss, boss)

	def decrease_life(self, amount):
		self.life -= amount
		return self.life <= 0

	def score(self):
		return self.max_life

	def remove(self):
		gfw.world.remove(self)

	def get_bb(self):
		hw = 200
		hh = 100
		return self.x - hw, self.y - hh, self.x + hw, self.y + hh