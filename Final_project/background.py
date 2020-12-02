import gfw
from pico2d import *
from gobj import *

class Background:
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(RES_DIR + imageName)
        self.target = None
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.win_rect = 0, 0, self.cw, self.ch
        self.center = self.image.w // 2, self.image.h // 2
        hw, hh = self.cw // 2, self.    ch // 2
        self.boundary = hw, hh, self.image.w - hw, self.image.h - hh
    def set_target(self, target):
        self.target = target
        self.update()
    def draw(self):
        self.image.clip_draw_to_origin(*self.win_rect, 0, 0)
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos
        sl = round(tx - self.cw / 2)
        sb = round(ty - self.ch / 2)
        self.win_rect = sl, sb, self.cw, self.ch
    def get_boundary(self):
        return self.boundary
    def translate(self, point):
        x, y = point
        l, b, r, t = self.win_rect
        return l + x, b + y
    def to_screen(self, point):
        # return self.cw // 2, self.ch // 2
        x, y = point
        l, b, r, t = self.win_rect
        return x - l, y - b

class VertScrollBackground(Background):
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(RES_DIR + imageName)
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 0

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        left, bottom = 0, 0
        page = self.image.h * self.cw // self.image.w
        curr = int(-self.scroll) % page
        if curr > 0:
            h = int(1 + self.image.w * curr / self.cw)
            b = self.image.h - h
            src = 0, b, self.image.w, h
            dh = int(h * self.cw / self.image.w)
            dst = 0, curr- dh, self.cw, dh
            self.image.clip_draw_to_origin(*src, *dst)
        dst_height = round(self.image.h * self.cw / self.image.w)
        while curr + dst_height < self.ch:
            dst = 0, curr, self.cw, dst_height
            self.image.draw_to_origin(*dst)
            curr += dst_height
        if curr < self.ch:
            dh = self.ch - curr
            h = int(1 + self.image.w * dh / self.cw)
            src = 0, 0, self.image.w, h
            dh = int(h * self.cw / self.image.w)
            dst = 0, curr, self.cw, dh
            self.image.clip_draw_to_origin(*src, *dst)

    def to_screen(self, point):
        x, y = point
        return x - self.scroll, y

    def translate(self, point):
        x, y = point
        return x + self.scroll, y

    def get_boundary(self):
        return (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)
