from scene import Scene
from collections.abc import Callable
from pexeso_rect import PexesoRect
from random import shuffle
from text_rect import TextRect
from pygame import font
from random import sample
from functools import partial


class Pexeso(Scene):
    def __init__(self, gap:float, rect_width:float, rect_height:float, width:int, height:int, scene_switch:Callable[[int], None], wait, is_waiting, stop_waiting, multiplayer):
        super().__init__(scene_switch)
        self.wait = wait
        self.stop_waiting = stop_waiting
        self.is_waiting = is_waiting
        self.ai_active = False
        self.multiplayer = multiplayer
        self.player1_score = 0
        self.player2_score = 0
        self.player1 = True
        self.stage1 = True
        self.selected = None
        self.screen_objects = [None] * 64
        self.wrong = False
        self.to_cover = None
        self.button_font = font.SysFont("Arial", 35)
        self.available_rects = list(range(0,64))
        pairs = list(range(1, 33)) * 2
        left_offset = (width - 8 * rect_width - 7 * gap)/2
        top_offset = (height - 8 * rect_height - 7 * gap)/2
        shuffle(pairs)
        for i in range(8):
            for j in range(8):
                self.screen_objects[i*8 + j] = PexesoRect(left_offset + j * (rect_width+gap), top_offset + i * (rect_height+gap), rect_width, rect_height, pairs[i*8+j], self.on_pexeso_click, lambda x: None, lambda x: None, "blue", "black", str(pairs[i*8 + j]), self.button_font, i*8+j)
        self.screen_objects.append(TextRect(10, 10, 100, 50, "blue", "white", "Zpět", self.button_font, self.open_menu, self.on_button_hover, self.on_button_hover_leave))
        self.screen_objects.append(TextRect(10, 70, 100, 50, "blue", "white", "Znovu", self.button_font, self.reset, self.on_button_hover, self.on_button_hover_leave))
        self.screen_objects.append(TextRect(width-left_offset+20, 10, 95, 50, "white", "blue", "Hraje:", self.button_font))
        self.screen_objects.append(TextRect(width-left_offset+20, 70, 95, 50, "white", "blue", "Hráč 1", self.button_font))
        self.screen_objects.append(TextRect(width-left_offset+20, height-160, 95, 50, "white", "blue", "Hráč 1:", self.button_font))
        self.screen_objects.append(TextRect(width-left_offset+20, height-90, 95, 50, "white", "blue", "Hráč 2:", self.button_font))
        self.screen_objects.append(TextRect(width-left_offset+155, height-160, 95, 50, "white", "blue", "0", self.button_font))
        self.screen_objects.append(TextRect(width-left_offset+155, height-90, 95, 50, "white", "blue", "0", self.button_font))

        #cheat

        #for i in range(8):
        #    for j in range(8):
        #        self.screen_objects[i*8 + j].uncover()

    def on_pexeso_click(self, clicked_rect):
        if clicked_rect.solved:
            return
        
        if self.is_waiting() or self.ai_active:
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
                if self.player1:
                    self.player1_score += 1
                    self.screen_objects[-2].update_text(self.player1_score)
                else:
                    self.player2_score += 1
                    self.screen_objects[-1].update_text(self.player2_score)

                clicked_rect.solved = True
                self.selected.solved = True

                self.available_rects.remove(clicked_rect.rect_id)
                self.available_rects.remove(self.selected.rect_id)

    def update_current_player(self):
        if self.player1:
            self.screen_objects[-5].update_text("Hráč 1")
        else:
            self.screen_objects[-5].update_text("Hráč 2")

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
        self.player1 = not self.player1
        self.update_current_player()
        if not self.player1 and not self.multiplayer:
            self.ai_active = True
            self.wait(0.5, self.ai_turn)

    def open_menu(self, y):
        self.stop_waiting(lambda:None)
        self.switch_scenes(0)

    def reset(self, x):
        self.stop_waiting(lambda:None)
        self.switch_scenes(1)

    def ai_turn(self):
        pick1, pick2 = sample(self.available_rects, 2)
        #pick1 = self.available_rects[0]
        #pick2 = list(filter(lambda x: x.pair_id == self.screen_objects[pick1].pair_id and x.rect_id != self.screen_objects[pick1].rect_id, self.screen_objects[:64]))[0].rect_id
        self.screen_objects[pick1].uncover()
        self.screen_objects[pick2].uncover()
        self.wait(2, partial(self.ai_turn_end, pick1, pick2))

    def ai_turn_end(self, pick1, pick2):
        if self.screen_objects[pick1].pair_id == self.screen_objects[pick2].pair_id:
            self.available_rects.remove(pick1)
            self.available_rects.remove(pick2)

            self.player2_score += 1
            self.screen_objects[-1].update_text(self.player2_score)

            self.screen_objects[pick1].solved = True
            self.screen_objects[pick2].solved = True

            if len(self.available_rects) > 0:
                self.wait(0.5, self.ai_turn)
        else:
            self.screen_objects[pick1].cover()
            self.screen_objects[pick2].cover()
            self.ai_active = False
            self.player1 = True
            self.update_current_player()
        
