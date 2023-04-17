from collections.abc import Callable

class Scene:
    def __init__(self, scene_switch:Callable[[int], None]):
        self.screen_objects = []
        self.switch_scenes = scene_switch

    def on_mouse_down(self, pos):
        for x in self.screen_objects:
            if x.collidepoint(pos):
                x.on_click(x)
                break

    def draw(self, screen):
        pass

    def update(self, mouse_pos):
        pass