from scene import Scene
from pygame import Rect
from pygame import draw
from collections.abc import Callable
from pexeso_rect import PexesoRect
from random import shuffle
from os import path
from pygame.time import wait

class Pexeso(Scene):
    def __init__(self, gap:float, rect_width:float, rect_height:float, width:int, height:int, scene_switch:Callable[[int], None]):
        super().__init__(scene_switch)
        left_offset = 30
        top_offset = 30
        self.stage1 = True
        self.selected = None
        self.screen_objects = [None] * 16
        self.wrong = False
        self.to_cover = None
        pairs = list(range(1, 9)) * 2
        shuffle(pairs)
        for i in range(4):
            for j in range(4):
                self.screen_objects[i*4 + j] = PexesoRect(left_offset + gap + j * (rect_width+gap), top_offset + gap + i * (rect_height+gap), rect_width, rect_height, pairs[i*4+j], path.join(path.dirname(__file__), f"../assets/{pairs[i*4+j]}.png"), "blue")
        #self.screen_objects[0].append([Rect(0, 0, 50, 50), "blue", self.open_menu])

    def on_mouse_down(self, pos):
        if pos:
            for x in self.screen_objects:
                if x.collidepoint(pos) and (not x.solved):
                    if self.stage1:
                        x.uncover()
                        self.stage1 = False
                        self.selected = x
                        break
                    else:
                        self.stage1 = True
                        x.uncover()
                        if x.pair_id != self.selected.pair_id:
                            self.wrong = True
                            self.to_cover = x
                        else:
                            x.solved = True
                            self.selected.solved = True

    def draw(self, screen):
        screen.fill("white")
        for x in self.screen_objects:
            x.draw(screen)

    def update(self, mouse_pos):
        if self.wrong:
            wait(1000)
            self.to_cover.cover()
            self.selected.cover()
            self.wrong = False

    def open_menu(self, y):
        self.switch_scenes(0)