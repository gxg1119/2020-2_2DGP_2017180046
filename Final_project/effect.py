from pico2d import *
import gfw
from gobj import *

class Effect :
	def __init__(self, x, y, num):
		self.x, self.y = x, y - 30
		self.effect_image = gfw.image.load(RES_DIR + '/effect.png')
		self.boss_effect_image = gfw.image.load(RES_DIR + '/boss_effect.png')
		self.effect_time = 0
		self.efdx = 0
		self.num = num

	def draw(self):
		if self.num == 0 : self.effect_image.clip_draw(self.efdx * 150 ,0, 150, 150, self.x, self.y, 120, 120)
		else: self.boss_effect_image.clip_draw(self.efdx * 256 ,0, 256, 256 , self.x, self.y, 800, 800)

	def update(self):
		self.effect_time += gfw.delta_time
		if self.num == 0:
			self.efdx = int(self.effect_time * 20) % 8
			if self.efdx > 6 :
				self.remove()
		else :
			self.efdx = int(self.effect_time * 20) % 48
			if self.efdx > 40 :
				self.remove()

	def generate(self):
		effect = Effect(self.x, self.y, self.num)
		gfw.world.add(gfw.layer.effect, effect)

	def remove(self):
		gfw.world.remove(self)