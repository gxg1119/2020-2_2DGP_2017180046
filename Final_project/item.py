from pico2d import *
import gfw
from gobj import *
import random

ITEM_MOVE_PPS = 200
ITEM_SIZE = 30
class Item:

	def __init__(self, x, y, dx, dy):
		self.x, self.y = x, y
		self.dx, self.dy = dx, -random.uniform(2.0, 3.0)
		self.Dualshot_image = gfw.image.load(RES_DIR + '/dualshot.png')
		self.Powershot_image = gfw.image.load(RES_DIR + '/powershot.png')

		self.choose = random.randint(1, 5)

		self.x_direction = random.randint(1, 2)

	def draw(self):
		if self.choose == 1:
			self.Powershot_image.draw(self.x, self.y)
		else:
			self.Dualshot_image.draw(self.x, self.y)

	def update(self):
		x, y = self.x, self.y
		dx, dy = self.dx, self.dy
		x += dx * ITEM_MOVE_PPS * gfw.delta_time
		y += dy * ITEM_MOVE_PPS * gfw.delta_time

		#hw = self.image.w //2
		#x = clamp(hw, x, get_canvas_width() - hw)

		self.x, self.y = x, y

		if self.x_direction == 1: self.dx = -1
		else: self.dx = 1

	def generate(self):
		item = Item(self.x, self.y, self.dx, self.dy)
		gfw.world.add(gfw.layer.item, item)

	def remove(self):
		gfw.world.remove(self)

	def get_bb(self):
		half = ITEM_SIZE
		return self.x - half, self.y - half, self.x + half, self.y + half