from scene import Scene
from pygame import Rect
from pygame import draw
from pygame import font
from collections.abc import Callable
from text_rect import Text_Rect

class Menu(Scene):
    def __init__(self, width:int, height:int, scene_switch:Callable[[int], None], quit:Callable):
        super().__init__(scene_switch)
        self.button_width = 200
        self.button_height = 50
        self.title_font = font.SysFont("Corbel", 100)
        self.button_font = font.SysFont("Corbel", 35)
        button_x = (width - self.button_width)/2
        button_y = (height - self.button_height)/2
        self.screen_objects = [
            Text_Rect(button_x, button_y - 0.2*height + 40, self.button_width, self.button_height, "blue", "white", "Start", self.button_font),
            Text_Rect(button_x, button_y - 0.2*height - self.button_height - 60, self.button_width, self.button_height, "white", "blue", "Mega pexeso", self.title_font),
            Text_Rect(button_x, button_y - 0.2*height + self.button_height + 70, self.button_width, self.button_height, "blue", "white", "Konec", self.button_font)
        ]
        self.quit = quit
        

    def draw(self, screen):
        screen.fill("white")
        for x in self.screen_objects:
            draw.rect(screen, x.background_color, x)
            screen.blit(x.rendered_text, x.text_pos)
        
    def update(self, mouse_pos):
        if self.screen_objects[0].collidepoint(mouse_pos):
            self.screen_objects[0].background_color = "red"
        else:
            self.screen_objects[0].background_color = "blue"
        
        if self.screen_objects[2].collidepoint(mouse_pos):
            self.screen_objects[2].background_color = "red"
        else:
            self.screen_objects[2].background_color = "blue"
    
    def on_mouse_down(self, pos):
        if self.screen_objects[0].collidepoint(pos):
            self.switch_scenes(1)
        elif self.screen_objects[2].collidepoint(pos):
            self.quit()