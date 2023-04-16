from scene import Scene
from pygame import Rect
from pygame import draw
from collections.abc import Callable


class Pexeso(Scene):
    def __init__(self, gap:float, rect_size:float, width:int, height:int, scene_switch:Callable[[int], None]):
        super().__init__(scene_switch)
        left_offset = 30
        top_offset = 30
        self.screen_objects = [[[] for _ in range((width-gap-left_offset)//(rect_size+gap))] for _ in range((height-gap-top_offset)//(rect_size+gap))]
        for i in range(len(self.screen_objects)):
            for j in range(len(self.screen_objects[i])):
                self.screen_objects[i][j] = [Rect(left_offset + gap + j * (rect_size+gap), top_offset + gap + i * (rect_size+gap), rect_size, rect_size), "blue", self.change_color]
        self.screen_objects[0].append([Rect(0, 0, 50, 50), "blue", self.open_menu])

    def on_mouse_down(self, pos):
        if pos:
            for x in self.screen_objects:
                for y in x:
                    if y[0].collidepoint(pos):
                        y[2](y)
                        break
                else:
                    continue
                break

    def draw(self, screen):
        screen.fill("white")
        for x in self.screen_objects:
            for y in x:
                draw.rect(screen, y[1], y[0])

    def update(self, mouse_pos):
        pass

    def change_color(self, rect_struct):
        rect_struct[1] = "red"

    def open_menu(self, y):
        self.switch_scenes(0)