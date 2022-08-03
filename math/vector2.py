import math

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
        self.magnitude = math.sqrt(self.x**2 + self.y**2)
        if self.magnitude == 0:
            self.unit = None
        elif self.magnitude == 1:
            self.unit = self
        else:
            self.unit = self / self.magnitude

    def __eq__(self, other):
        if type(other) != Vector2:
            return False
        else:
            return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x / other, self.y / other)
        elif type(other) == Vector2:
            return Vector2(self.x / other.x, self.y / other.y)
        else:
            print("Invalid type for division with a Vector2: " + str(type(other)))

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x * other, self.y * other)
        elif type(other) == Vector2:
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            print("Invalid type for division with a Vector2: " + str(type(other)))

    def __add__(self, other):
        if type(other) == Vector2:
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            print("Invalid type for addition with a Vector2: " + str(type(other)))

    def __sub__(self, other):
        if type(other) == Vector2:
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            print("Invalid type for subtraction with a Vector2: " + str(type(other)))

    def __str__(self):
        return f"V2({self.x}, {self.y})"

    def dot(self, other):
        return self.x*other.x + self.y*other.y