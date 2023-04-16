from scene import Scene
from pygame import Rect
from pygame import draw
from collections.abc import Callable


class Pexeso(Scene):
    def __init__(self, gap:float, rect_size:float, width:int, height:int, scene_switch:Callable[[int], None]):
        super().__init__(scene_switch)

        self.screen_objects = [[[] for _ in range((width-gap)//(rect_size+gap))] for _ in range((height-gap)//(rect_size+gap))]
        for i in range(len(self.screen_objects)):
            for j in range(len(self.screen_objects[i])):
                self.screen_objects[i][j] = [Rect(gap + j * (rect_size+gap), gap + i * (rect_size+gap), rect_size, rect_size), "blue"]
        self.pos = None

    def on_mouse_down(self, pos):
        self.pos = pos

    def draw(self, screen):
        screen.fill("white")
        for x in self.screen_objects:
            for y in x:
                draw.rect(screen, y[1], y[0])

    def update(self, mouse_pos):
        if self.pos:
            for x in self.screen_objects:
                for y in x:
                    if y[0].collidepoint(self.pos):
                        y[1] = "red"
                        self.pos = None
                        break
                else:
                    continue
                break