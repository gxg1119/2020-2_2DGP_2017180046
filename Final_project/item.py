from pico2d import *
import gfw
from gobj import *
import random

ITEM_MOVE_PPS = 200
ITEM_SIZE = 30
class Item:
	item_val = 1
	def __init__(self, x, y, dx, dy):
		self.init(x, y, dx, dy, '/money.png')

	def init(self, x, y, dx, dy, imageName):
		self.x, self.y = x, y
		self.dx, self.dy = dx, -random.uniform(1.5, 2.0)
		self.image = gfw.image.load(RES_DIR + imageName)
		self.x_direction = random.randrange(12)
		

	def draw(self):
		self.image.draw(self.x, self.y)

	def update(self):
		x, y = self.x, self.y
		dx, dy = self.dx, self.dy
		x += dx * ITEM_MOVE_PPS * gfw.delta_time
		y += dy * ITEM_MOVE_PPS * gfw.delta_time

		hw = self.image.w //2
		x = clamp(hw, x, get_canvas_width() - hw)

		self.x, self.y = x, y

		if self.x_direction == 0 or self.x_direction == 1 : self.dx = 0.5
		elif self.x_direction == 2 or self.x_direction == 3 : self.dx = -0.5
		elif self.x_direction == 4 or self.x_direction == 5 : self.dx = 1
		elif self.x_direction == 6 or self.x_direction == 7 : self.dx = -1
		elif self.x_direction == 8 or self.x_direction == 9 : self.dx = 1.5
		else: self.dx = -1.5

	def generate(self):
		item = Item(self.x, self.y, self.dx, self.dy)
		gfw.world.add(gfw.layer.item, item)

	def remove(self):
		gfw.world.remove(self)

	def get_bb(self):
		half = ITEM_SIZE
		return self.x - half, self.y - half, self.x + half, self.y + half

class Dual(Item):
	item_val =2
	def __init__(self, x, y, dx, dy):
		self.init(x, y, dx, dy, '/dualshot.png')

	def generate(self):
		if random.randrange(2) == 0:
			item = Dual(self.x, self.y, self.dx, self.dy)
			gfw.world.add(gfw.layer.item, item)