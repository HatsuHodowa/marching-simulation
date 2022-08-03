import pygame
pygame.init()

from polygon import *
from camera import *

class ImageRect(Polygon):
    assets = "assets"
    def __init__(self, image="", **kwargs):
        self.image = image
        self.loaded_image = None
        self.points = []

        for i in range(4):
            self.points.append(CFrame.angle(i*(math.pi/2) + math.pi/4).look_vector)

        if self.image != "":
            self.orig_image = pygame.image.load(ImageRect.assets + "/" + self.image)
            self.loaded_image = self.orig_image

        # polygon
        Polygon.__init__(self, self.points, **kwargs)
        self.size = Vector2(self.orig_image.get_width()/20, self.orig_image.get_height()/20)

    def update_points(self):
        # generating points
        self.points = []
        if self.image == "":
            for i in range(4):
                self.points.append(CFrame.angle(i*(math.pi/2) + math.pi/4).look_vector)

        else:
            self.points.append(Vector2(-self.size.x/2, self.size.y/2)/self.size)
            self.points.append(Vector2(-self.size.x/2, -self.size.y/2)/self.size)
            self.points.append(Vector2(self.size.x/2, -self.size.y/2)/self.size)
            self.points.append(Vector2(self.size.x/2, self.size.y/2)/self.size)

    def draw(self):
        if self.image == "":
            Polygon.draw(self)
            return

        """if not self.is_visible():
            return"""

        self.update_points()

        # calculating position
        new_point = self.cframe.p*10
        tags = Tag.get_tags(self.surface)

        zoom = 1
        for tag in tags:
            if type(tag.tag) == Camera:
                new_point = tag.tag.point_on_camera(new_point)
                zoom = tag.tag.zoom

        # drawing
        if not self.orig_image:
            self.orig_image = pygame.image.load(ImageRect.assets + "/" + self.image)

        # drawing
        w, h = self.surface.get_size()
        self.loaded_image = pygame.transform.scale(self.orig_image, (self.size.x*10*zoom, self.size.y*10*zoom))
        self.loaded_image = pygame.transform.rotate(self.loaded_image, self.cframe.get_angle() * (180/math.pi))
        
        iw, ih = self.loaded_image.get_size()
        self.surface.blit(self.loaded_image, (new_point.x + w/2 - iw/2, -new_point.y + h/2 - ih/2))