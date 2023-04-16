import pygame
from menu import Menu
from pexeso import Pexeso

class Game:
    def __init__(self, res:tuple[int,int], caption:str, scene_id:int):
        pygame.init()
        self.active_scene = None
        self.width = res[0]
        self.height = res[1]
        self.caption = caption
        self.screen = pygame.display.set_mode(res)
        self.clock = pygame.time.Clock()
        self.running = False
        pygame.display.set_caption(caption)
        self.load_scene(scene_id)

    def load_scene(self, id):
        if id == 0:
            self.active_scene = Menu(self.width, self.height, self.load_scene, self.stop)
        elif id == 1:
            self.active_scene = Pexeso(20, 200, 100, self.width, self.height, self.load_scene)

    def run(self):
        self.running = True
        self.loop()
    
    def stop(self):
        self.running = False

    def loop(self):
        while self.running:
            pos = None
            self.active_scene.update(pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.active_scene.on_mouse_down(event.pos)

            self.active_scene.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()