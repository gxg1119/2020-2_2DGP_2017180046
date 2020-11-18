from pico2d import *
import gfw
from gobj import *
import random

MONEY_MOVE_PPS =200
MONEY_SIZE = 40

class Money:
	def __init__(self, x, y, dy):
		global money
		self.x, self.y = x, y
		self.dy = random.uniform(2,4)
		self.image = gfw.image.load(RES_DIR + '/money.png')

	def update(self):
		global money_cout
		y = self.y
		dy = self.dy
		y -= dy * MONEY_MOVE_PPS * gfw.delta_time
		self.y = y

	def draw(self):
		self.image.draw(self.x, self.y)

	def remove(self):
		gfw.world.remove(self)

	def generate(self):
		money=Money(self.x, self.y, self.dy)
		gfw.world.add(gfw.layer.money, money)

	def get_bb(self):
		half = MONEY_SIZE
		return self.x - half, self.y - half, self.x + half, self.y + half