from pygame import draw
from pygame import font
from text_rect import TextRect

class PexesoRect(TextRect):
    rendered_question = None
    unified_question_offset = (21, -4)

    def __init__(self, left, top, width, height, pair_id, on_click, on_hover, on_hover_leave, background:str, text_color:str, text:str, text_font):
        super().__init__(left, top, width, height, background, text_color, text, text_font, on_click, on_hover, on_hover_leave)
        self.pair_id = pair_id
        self.covered = True
        self.background = background
        self.solved = False
        if not PexesoRect.rendered_question:
            question_font = font.SysFont("Arial", 55, bold=True)
            PexesoRect.rendered_question = question_font.render("?", True, "white")

    def draw(self, screen):
        if self.covered:
            draw.rect(screen, self.background, self)
            screen.blit(self.rendered_question, (self.x + PexesoRect.unified_question_offset[0],
                        self.y + PexesoRect.unified_question_offset[1] + 10))
        else:
            screen.blit(self.rendered_text, self.text_pos)
    
    def uncover(self):
        self.covered = False
    
    def cover(self):
        self.covered = True