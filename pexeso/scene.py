from collections.abc import Callable

class Scene:
    def __init__(self, scene_switch:Callable[[int], None]):
        self.screen_objects = []
        self.switch_scenes = scene_switch

    def on_mouse_down(self, pos):
        pass

    def draw(self, screen):
        pass

    def update(self, mouse_pos):
        pass