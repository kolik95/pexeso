from pygame import Rect
from pygame import image
from pygame import draw
from pygame import transform
from pygame import Surface

class PexesoRect(Rect):
    def __init__(self, left, top, width, height, pair_id, image_path, color):
        super().__init__(left, top, width, height)
        self.pair_id = pair_id
        self.image = transform.scale(image.load(image_path), self.size)
        self.image_pos = self.x + (self.width - self.image.get_rect().width)/2, self.y + (self.height - self.image.get_rect().height)/2
        self.covered = False
        self.color = color
        self.solved = False

    def draw(self, screen):
        if self.covered:
            screen.blit(self.image, self.image_pos)
        else:
            draw.rect(screen, self.color, self)
    
    def uncover(self):
        self.covered = True
    
    def cover(self):
        self.covered = False