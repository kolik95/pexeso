from scene import Scene
from collections.abc import Callable
from pexeso_rect import PexesoRect
from random import shuffle
from text_rect import TextRect
from pygame import font


class Pexeso(Scene):
    def __init__(self, gap:float, rect_width:float, rect_height:float, width:int, height:int, scene_switch:Callable[[int], None], wait, is_waiting, stop_waiting):
        super().__init__(scene_switch)
        self.wait = wait
        self.stop_waiting = stop_waiting
        self.is_waiting = is_waiting
        self.stage1 = True
        self.selected = None
        self.screen_objects = [None] * 64
        self.wrong = False
        self.to_cover = None
        self.button_font = font.SysFont("Arial", 35)
        pairs = list(range(1, 33)) * 2
        left_offset = (width - 8 * rect_width - 7 * gap)/2
        top_offset = (height - 8 * rect_height - 7 * gap)/2
        shuffle(pairs)
        for i in range(8):
            for j in range(8):
                self.screen_objects[i*8 + j] = PexesoRect(left_offset + j * (rect_width+gap), top_offset + i * (rect_height+gap), rect_width, rect_height, pairs[i*8+j], self.on_pexeso_click, lambda x: None, lambda x: None, "blue", "black", str(pairs[i*8 + j]), self.button_font)
        self.screen_objects.append(TextRect(10, 10, 95, 50, "blue", "white", "Zpět", self.button_font, self.open_menu, self.on_button_hover, self.on_button_hover_leave))
        self.screen_objects.append(TextRect(10, 70, 95, 50, "blue", "white", "Znovu", self.button_font, self.reset, self.on_button_hover, self.on_button_hover_leave))
        self.screen_objects.append(TextRect(width-left_offset+10, 10, 95,50, "white", "blue", "Hraje:", self.button_font))

    def on_pexeso_click(self, clicked_rect):
        if clicked_rect.solved:
            return
        
        if self.is_waiting():
            return
        
        if self.stage1:
            clicked_rect.uncover()
            self.stage1 = False
            self.selected = clicked_rect
        else:
            if clicked_rect == self.selected:
                return
            
            self.stage1 = True
            clicked_rect.uncover()
            if clicked_rect.pair_id != self.selected.pair_id:
                self.wrong = True
                self.to_cover = clicked_rect
            else:
                clicked_rect.solved = True
                self.selected.solved = True

    def on_button_hover(self, x):
        x.background_color = "red"

    def on_button_hover_leave(self, x):
        x.background_color = "blue"

    def draw(self, screen):
        screen.fill("white")
        for x in self.screen_objects:
            x.draw(screen)

    def update(self, mouse_pos):
        for x in self.screen_objects:
            if x.collidepoint(mouse_pos):
                x.on_hover(x)
            else:
                x.on_hover_leave(x)
            
        if self.wrong and (not self.is_waiting()):
            self.wait(2,self.resume_game)

    def resume_game(self):
        self.to_cover.cover()
        self.selected.cover()
        self.wrong = False

    def open_menu(self, y):
        self.stop_waiting(lambda:None)
        self.switch_scenes(0)

    def reset(self, x):
        self.stop_waiting(lambda:None)
        self.switch_scenes(1)
