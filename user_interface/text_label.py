from gui_object import *
from cframe import *
import pygame
pygame.init()

class TextLabel(GUIObject):
    def __init__(self, **kwargs):
        self.font_family = None
        self.font_size = 25
        self.text = "Text Label"
        self.position = Vector2()

        self.color = (255, 0, 0)

        GUIObject.__init__(self, **kwargs)

    def render_ui(self):
        if not self.surface:
            return

        self.__font = pygame.font.SysFont(None, 25)
        self.__image = self.__font.render(self.text, True, self.color)
        
        self.surface.blit(self.__image, (self.position.x, self.position.y))