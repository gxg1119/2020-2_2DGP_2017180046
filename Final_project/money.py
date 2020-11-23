from pico2d import *
import gfw
from gobj import *
import random

MONEY_MOVE_PPS =200
MONEY_SIZE = 20

class Money:
	def __init__(self, x, y, dx, dy):
		self.x, self.y = x, y
		self.dx, self.dy = dx*0.5, -random.uniform(2.0, 3.0)
		self.image = gfw.image.load(RES_DIR + '/money.png')

		self.side = random.randint(1, 2)

	def update(self):
		x, y = self.x, self.y
		dx, dy = self.dx, self.dy
		x += dx * MONEY_MOVE_PPS * gfw.delta_time
		y += dy * MONEY_MOVE_PPS * gfw.delta_time

		hw = self.image.w //2
		x = clamp(hw, x, get_canvas_width() - hw)

		self.x, self.y = x, y

		if self.side == 1: self.dx = -1
		else: self.dx = 1

	def draw(self):
		self.image.draw(self.x, self.y)

	def remove(self):
		gfw.world.remove(self)

	def generate(self):
		money = Money(self.x, self.y, self.dx, self.dy)
		gfw.world.add(gfw.layer.money, money)

	def get_bb(self):
		half = MONEY_SIZE
		return self.x - half, self.y - half, self.x + half, self.y + half