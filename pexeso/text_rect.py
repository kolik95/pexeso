from pygame import draw
from action_rect import ActionRect

class TextRect(ActionRect):
    def __init__(self, left, top, width, height, background:str, text_color:str, text:str, font, on_click = lambda x: None, on_hover = lambda x: None, on_hover_leave = lambda x: None):
        super().__init__(left, top, width, height, on_click, on_hover, on_hover_leave)
        self.rendered_text = font.render(text, True, text_color)
        self.background_color = background
        self.text_pos = self.x + (self.width - self.rendered_text.get_rect().width)/2, self.y + (self.height - self.rendered_text.get_rect().height)/2

    def draw(self, screen):
        draw.rect(screen, self.background_color, self)
        screen.blit(self.rendered_text, self.text_pos)