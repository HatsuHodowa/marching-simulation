from polygon import *

class Rect(Polygon):
    def __init__(self, **kwargs):
        # kwargs
        self.__width = 8
        self.__height = 5

        if "rect_width" in kwargs:
            self.__width = kwargs['rect_width']
        if "rect_height" in kwargs:
            self.__height = kwargs['rect_height']

        # calculating points
        self.points = []
        for i in range(4):
            angle = math.pi/4 + (math.pi/2)*i
            point = CFrame.angle(angle).right_vector * Vector2(self.__width, self.__height)
            
            self.points.append(point.unit)

        Polygon.__init__(self, self.points, **kwargs)

        # adjusting size
        self.size = Vector2(self.__width, self.__height)