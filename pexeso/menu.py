from scene import Scene
from pygame import font
from collections.abc import Callable
from text_rect import TextRect

class Menu(Scene):
    def __init__(self, width:int, height:int, scene_switch:Callable[[int], None], quit:Callable):
        super().__init__(scene_switch)
        button_width = 300
        button_height = 50
        self.title_font = font.SysFont("Corbel", 100)
        self.button_font = font.SysFont("Arial", 35)
        button_x = (width - button_width)*0.5
        button_y = (height - button_height)*0.5
        self.screen_objects = [
            TextRect(button_x, button_y - 0.2*height + 40, button_width, button_height, "blue", "white", "Hra pro jednoho", self.button_font, self.on_1p_click, self.on_button_hover, self.on_button_hover_leave),
            TextRect(button_x, button_y - 0.2*height + button_height + 70, button_width, button_height, "blue", "white", "Hra pro dva", self.button_font, self.on_2p_click, self.on_button_hover, self.on_button_hover_leave),
            TextRect(button_x, button_y - 0.2*height - button_height - 60, button_width, button_height, "white", "blue", "Pexeso", self.title_font),
            TextRect(button_x, button_y - 0.2*height + 2*button_height + 100, button_width, button_height, "blue", "white", "Konec", self.button_font, self.on_quit_click, self.on_button_hover, self.on_button_hover_leave)
        ]
        self.quit = quit

    def on_button_hover(self, x):
        x.background_color = "red"
    
    def on_button_hover_leave(self, x):
        x.background_color = "blue"

    def on_1p_click(self, x):
        self.switch_scenes(1)

    def on_2p_click(self, x):
        self.switch_scenes(2)

    def on_quit_click(self, x):
        self.quit()