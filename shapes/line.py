from polygon import *

class Line(Polygon):
    def __init__(self, points, **kwargs):
        self.closed = False
        Polygon.__init__(self, points, **kwargs)
        
        # defaults
        self.width = 5

        # kwargs
        for kw in kwargs:
            if kw == "width":
                self.width = kwargs[kw]

    def draw(self):
        if not self.is_visible():
           return

        # calculating points
        points = self.calculate_points()
        tuple_points = []
        for point in points:
            w, h = 0, 0
            if self.surface:
                w, h = self.surface.get_size()
            tuple_points.append((point.x + w/2, h - point.y - h/2))

        # border width
        bd_width = self.width
        tags = Tag.get_tags(self.surface)
        for tag in tags:
            if type(tag.tag) == Camera:
                cam = tag.tag
                bd_width *= cam.zoom

        # drawing
        pygame.draw.lines(self.surface, self.color, self.closed, tuple_points, int(bd_width + 0.5))