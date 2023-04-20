from pygame import draw
from pygame import font
from text_rect import TextRect

class PexesoRect(TextRect):
    rendered_question = None
    unified_question_offset = (21, -4) # Umístí otazník zhruba doprostřed obdélníku (dynamické počítání zlobilo)

    def __init__(self, left, top, width, height, pair_id, on_click, on_hover, on_hover_leave, background:str, text_color:str, text:str, text_font, rect_id):
        super().__init__(left, top, width, height, background, text_color, text, text_font, on_click, on_hover, on_hover_leave)
        self.pair_id = pair_id # Toto id má společné s jinou kartičkou
        self.rect_id = rect_id # Unikátní id pro tuto jednu kartu
        self.covered = True # True pokud se má zobrazovat jako zakrytá
        self.background = background
        self.solved = False # True pokud byl nalezen pár
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