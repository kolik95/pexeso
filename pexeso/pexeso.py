from scene import Scene
from collections.abc import Callable
from pexeso_rect import PexesoRect
from random import shuffle
from os import path
from pygame.time import wait
from text_rect import TextRect
from pygame import font


class Pexeso(Scene):
    def __init__(self, gap:float, rect_width:float, rect_height:float, width:int, height:int, scene_switch:Callable[[int], None], block_input):
        super().__init__(scene_switch)
        self.block_input = block_input
        self.stage1 = True
        self.selected = None
        self.screen_objects = [None] * 64
        self.wrong = False
        self.to_cover = None
        self.button_font = font.SysFont("Corbel", 35)
        pairs = list(range(1, 33)) * 2
        left_offset = (width - 8 * rect_width - 7 * gap)/2
        top_offset = (height - 8 * rect_height - 7 * gap)/2
        shuffle(pairs)
        for i in range(8):
            for j in range(8):
                self.screen_objects[i*8 + j] = PexesoRect(left_offset + j * (rect_width+gap), top_offset + i * (rect_height+gap), rect_width, rect_height, pairs[i*8+j], self.on_pexeso_click, lambda x: None, lambda x: None, "blue", "black", str(pairs[i*8 + j]+ 1), self.button_font)
        self.screen_objects.append(TextRect(10, 10, 95, 50, "blue", "white", "Zpět", self.button_font, self.open_menu, self.on_button_hover, self.on_button_hover_leave))
        self.screen_objects.append(TextRect(10, 70, 95, 50, "blue", "white", "Znovu", self.button_font, self.reset, self.on_button_hover, self.on_button_hover_leave))

    def on_pexeso_click(self, clicked_rect):
        if clicked_rect.solved:
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
            
        if self.wrong:
            wait(3000)
            self.block_input()
            self.to_cover.cover()
            self.selected.cover()
            self.wrong = False

    def open_menu(self, y):
        self.switch_scenes(0)

    def reset(self, x):
        self.switch_scenes(1)
