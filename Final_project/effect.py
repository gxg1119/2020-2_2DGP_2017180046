from pico2d import *
import gfw
from gobj import *

class Effect :
	def __init__(self, x, y):
		self.x, self.y = x, y - 30
		self.effect_image = gfw.image.load(RES_DIR + '/effect.png')
		self.effect_time = 0
		self.efdx = 0

	def draw(self):
		self.effect_image.clip_draw(self.efdx * 150 ,0, 150, 150, self.x, self.y, 100, 100)

	def update(self):
		self.effect_time += gfw.delta_time
		self.efdx = int(self.effect_time * 20) % 8

		if self.efdx > 6 :
			self.remove()

	def generate(self):
		effect = Effect(self.x, self.y)
		gfw.world.add(gfw.layer.effect, effect)

	def remove(self):
		gfw.world.remove(self)