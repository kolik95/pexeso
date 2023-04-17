from pygame import Rect

class ActionRect(Rect):
    def __init__(self, left, top, width, height, on_click, on_hover, on_hover_leave):
        super().__init__(left, top, width, height)
        self.on_click = on_click
        self.on_hover = on_hover
        self.on_hover_leave = on_hover_leave

    def draw(self, screen):
        pass
