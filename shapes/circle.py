from polygon import *
from camera import *
from services import *

class Circle(Polygon):
    def __init__(self, **kwargs):
        Polygon.__init__(self, None, **kwargs)

    def calculate_points(self):
        return None
    
    def calculate_point(self, angle):
        return self.cframe * (CFrame.angle(angle).look_vector * self.size)

    def draw(self):
        size = min(self.size.x, self.size.y)
        posv2 = self.cframe.p * 10

        # camera adjustments
        tags = Tag.get_tags(self.surface)
        for tag in tags:
            if type(tag.tag) == Camera:
                posv2 = tag.tag.point_on_camera(posv2)
                size *= tag.tag.zoom

        # getting window size
        w, h = 0, 0
        if self.surface:
            w, h = self.surface.get_size()

        # creating tuple pos
        posv2 = Vector2(posv2.x + w/2, h - posv2.y - h/2)
        pos = (posv2.x, posv2.y)

        # border width
        bd_width = self.width
        tags = Tag.get_tags(self.surface)
        for tag in tags:
            if type(tag.tag) == Camera:
                cam = tag.tag
                bd_width *= cam.zoom
        
        # drawing
        pygame.draw.circle(self.surface, self.color, pos, size*10, int(bd_width + 0.5))