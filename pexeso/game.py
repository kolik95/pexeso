import pygame
from menu import Menu
from pexeso import Pexeso
from threading import Timer
from functools import partial

class Game:
    def __init__(self, res:tuple[int,int], caption:str, scene_id:int):
        pygame.init()
        self.active_scene = None # Scéna která se právě zobrazuje
        self.width = res[0] # šiřka okna
        self.height = res[1] # výška okna
        self.caption = caption # titulek okna
        self.screen = pygame.display.set_mode(res, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.running = False # True pokud hra běží
        pygame.display.set_caption(caption)
        self.load_scene(scene_id)
        self.waiting = False

    # Načte novou scénu
    def load_scene(self, id):
        # Hlavní menu
        if id == 0:
            self.active_scene = Menu(self.width, self.height, self.load_scene, self.stop)
        # Hra pro jednoho hráče
        elif id == 1:
            self.active_scene = Pexeso(20, 70, 70, self.width, self.height, self.load_scene, self.non_blocking_wait, self.is_waiting, self.stop_wating, False)
        # Hra pro dva hráče
        elif id == 2:
            self.active_scene = Pexeso(20, 70, 70, self.width, self.height, self.load_scene, self.non_blocking_wait, self.is_waiting, self.stop_wating, True)


    def run(self):
        self.running = True
        self.loop()
    
    def stop(self):
        self.running = False

    # Zakončí čekání
    def stop_wating(self, action):
        action()
        self.waiting = False

    def is_waiting(self):
        return self.waiting

    # Čekání které neblokuje běh programu
    def non_blocking_wait(self, seconds, action):
        self.waiting = True
        timer = Timer(seconds, partial(self.stop_wating, action))
        timer.start()

    # Zde probíhá celá hra
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