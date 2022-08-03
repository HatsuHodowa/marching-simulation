from gui_object import *
import pygame
pygame.init()
from cframe import *

class Frame(GUIObject):
    def __init__(self, **kwargs):
        self.size = Vector2(50, 50)
        self.position = Vector2(0, 0)
        self.background_color = (255, 255, 255)
        self.width = 0
        
        GUIObject.__init__(self, **kwargs)

    def render_ui(self):
        if not self.surface:
            return
        
        rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        pygame.draw.rect(self.surface, self.background_color, rect, self.width)