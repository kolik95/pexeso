from pygame import draw
from text_rect import TextRect

class PexesoRect(TextRect):
    def __init__(self, left, top, width, height, pair_id, on_click, on_hover, on_hover_leave, background:str, text_color:str, text:str, font):
        super().__init__(left, top, width, height, background, text_color, text, font, on_click, on_hover, on_hover_leave)
        self.pair_id = pair_id
        self.covered = True
        self.background = background
        self.solved = False

    def draw(self, screen):
        if self.covered:
            draw.rect(screen, self.background, self)
        else:
            screen.blit(self.rendered_text, self.text_pos)
    
    def uncover(self):
        self.covered = False
    
    def cover(self):
        self.covered = True