from constants import screen
from pygame import Color, Rect, Surface
from draw import drawPygameRect


class VSprite:
    def __init__(self, color: Color, rect: Rect, texture: Surface):
        self.color = Color(color)
        self.rect = Rect(rect)
        self.texture = texture

    def draw(self, surface=screen):
        drawPygameRect(surface, self.color, self.rect)
