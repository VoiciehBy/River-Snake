from constants import screen
from pygame import Color, Rect, Surface
from draw import drawPygameRect, drawImageOverRect


class VSprite:
    def __init__(self, color: Color, rect: Rect, texture: Surface):
        self.color = Color(color)
        self.rect = Rect(rect)
        self.texture = texture

    def draw(self, surface=screen):
        drawPygameRect(surface, self.color, self.rect)
        drawImageOverRect(surface, self.texture, self.rect)

    def set_color(self, color: Color):
        self.color = color

    def set_rect(self, rect: Rect):
        self.rect = rect

    def set_texture(self, texture: Surface):
        self.texture = texture
