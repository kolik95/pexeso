from pygame import Rect
from pygame import draw

class Text_Rect(Rect):
    def __init__(self, left, top, width, height, background:str, text_color:str, text:str, font):
        super().__init__(left, top, width, height)
        self.rendered_text = font.render(text, True, text_color)
        self.background_color = background
        self.text_pos = self.x + (self.width - self.rendered_text.get_rect().width)/2, self.y + (self.height - self.rendered_text.get_rect().height)/2

    def draw(self, screen):
        draw.rect(screen, self.background_color, self)
        screen.blit(self.rendered_text, self.text_pos)