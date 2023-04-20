from collections.abc import Callable

class Scene:
    def __init__(self, scene_switch:Callable[[int], None]):
        self.screen_objects = [] # Všechny UI elementy
        self.switch_scenes = scene_switch # Přepne aktivní scénu

    # Reakce na kliknutí myši
    def on_mouse_down(self, pos):
        for x in self.screen_objects:
            if x.collidepoint(pos):
                x.on_click(x)
                break

    # Vykreslí prvky scény
    def draw(self, screen):
        screen.fill("white")
        for x in self.screen_objects:
            x.draw(screen)

    # Aktualizuje stav scény
    def update(self, mouse_pos):
        for x in self.screen_objects:
            if x.collidepoint(mouse_pos):
                x.on_hover(x)
            else:
                x.on_hover_leave(x)