from polygon import *

class Triangle(Polygon):
    def __init__(self, **kwargs):
        # calculating points
        self.points = []
        for i in range(3):
            angle = (math.pi/1.5)*i
            self.points.append(CFrame.angle(angle).right_vector)

        # regular polygon
        Polygon.__init__(self, self.points, **kwargs)

class Square(Polygon):
    def __init__(self, **kwargs):
        # calculating points
        self.points = []
        for i in range(4):
            angle = math.pi/4 + (math.pi/2)*i
            self.points.append(CFrame.angle(angle).right_vector)

        # regular polygon
        Polygon.__init__(self, self.points, **kwargs)

class Pentagon(Polygon):
    def __init__(self, **kwargs):
        # calculating points
        self.points = []
        for i in range(5):
            angle = (math.pi/2.5)*i
            self.points.append(CFrame.angle(angle).right_vector)

        # regular polygon
        Polygon.__init__(self, self.points, **kwargs)

class Hexagon(Polygon):
    def __init__(self, **kwargs):
        # calculating points
        self.points = []
        for i in range(6):
            angle = (math.pi/3)*i
            self.points.append(CFrame.angle(angle).right_vector)

        # regular polygon
        Polygon.__init__(self, self.points, **kwargs)

class RegularPolygon(Polygon):
    def __init__(self, sides=3, **kwargs):
        # calculating points
        self.points = []
        for i in range(sides):
            angle = (math.pi/(sides/2))*i
            self.points.append(CFrame.angle(angle).right_vector)

        # regular polygon
        Polygon.__init__(self, self.points, **kwargs)