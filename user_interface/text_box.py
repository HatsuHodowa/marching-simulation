from gui_object import *
from cframe import *
import threading
import pygame

pygame.init()

class TextBox(GUIObject):
    all_texts = []
    def __init__(self, **kwargs):
        # text box things
        self.default_text = "Text Box"
        self.current_text = ""
        self.active = False
        self.event_loop_active = True
        
        self.font_family = None
        self.font_size = 25

        # positioning
        self.size = Vector2(50, 25)
        self.position = Vector2()

        # appearance
        self.color = (255, 0, 0)
        self.default_text_color = (150, 150, 150)
        self.background_color = (50, 50, 50)

        self.width = 0
        self.padding = 5

        # linked functions
        self.linked_functions = {
            "changed" : []
        }
        self.function_args = {}

        # super class
        GUIObject.__init__(self, **kwargs)

        # inserting into list
        TextBox.all_texts.append(self)

    def __fire_event(self, event, *args):
        for func in self.linked_functions[event]:
            arguments = args + self.function_args[func]
            thread = threading.Thread(target=func, args=arguments)
            thread.start()

    def link_function(self, event, func, *args):
        self.linked_functions[event].append(func)
        self.function_args[func] = args

    def process_event(self, event):
        rect = self.calculate_rect()

        # selecting
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        # input & backspace
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.current_text = self.current_text[:-1]
            else:
                self.current_text += event.unicode

            # running changed
            self.__fire_event("changed", self.current_text)

    def calculate_rect(self):
        return pygame.Rect(self.position.x - self.padding, self.position.y - self.padding, self.size.x + 2*self.padding, self.size.y + 2*self.padding)

    def render_ui(self):
        if not self.surface:
            return

        # creating text image
        color = self.color
        text = self.current_text
        if text == "":
            color = self.default_text_color
            text = self.default_text

        self.__font = pygame.font.SysFont(None, 25)
        self.__image = self.__font.render(text, True, color)

        # drawing rectangle
        w, h = self.__image.get_size()
        self.size = Vector2(w, h)
        rect = self.calculate_rect()
        pygame.draw.rect(self.surface, self.background_color, rect, self.width)
        
        # drawing text
        self.surface.blit(self.__image, (self.position.x, self.position.y))