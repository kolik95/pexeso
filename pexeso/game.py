import pygame
from menu import Menu
from pexeso import Pexeso
from threading import Timer
from functools import partial

class Game:
    def __init__(self, res:tuple[int,int], caption:str, scene_id:int):
        pygame.init()
        self.active_scene = None
        self.width = res[0]
        self.height = res[1]
        self.caption = caption
        self.screen = pygame.display.set_mode(res, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.running = False
        pygame.display.set_caption(caption)
        self.load_scene(scene_id)
        self.waiting = False

    def load_scene(self, id):
        if id == 0:
            self.active_scene = Menu(self.width, self.height, self.load_scene, self.stop)
        elif id == 1:
            self.active_scene = Pexeso(20, 70, 70, self.width, self.height, self.load_scene, self.non_blocking_wait, self.is_waiting, self.stop_wating)

    def run(self):
        self.running = True
        self.loop()
    
    def stop(self):
        self.running = False

    def stop_wating(self, action):
        action()
        self.waiting = False

    def is_waiting(self):
        return self.waiting

    def non_blocking_wait(self, seconds, action):
        self.waiting = True
        timer = Timer(seconds, partial(self.stop_wating, action))
        timer.start()

    def loop(self):
        while self.running:
            self.active_scene.update(pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.active_scene.on_mouse_down(event.pos)

            self.active_scene.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()