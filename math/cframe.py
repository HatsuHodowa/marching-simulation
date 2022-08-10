from vector2 import *

class CFrame: # m<row><column>
    def __init__(self, x=0, y=0):
        if type(x) == Vector2:
            self.position = x
        else:
            self.position = Vector2(x, y)
        self.p = self.position
        self.x = self.p.x
        self.y = self.p.y

        m11, m12, m13 = 1, 0, self.position.x
        m21, m22, m23 = 0, 1, self.position.y
        m31, m32, m33 = 0, 0, 1

        self.components = [m11, m12, m13, m21, m22, m23, m31, m32, m33]
        self.look_vector = Vector2(m11, m21)
        self.left_vector = Vector2(m12, m22)

        if self.position.magnitude != 0:
            self.rotation = CFrame.from_components(m11, m12, 0, m21, m22, 0, m31, m32, m33)
        else:
            self.rotation = self

    def __str__(self):
        comp_strings = []
        for comp in self.components:
            comp_string = str(math.floor(comp*1000)/1000)
            comp_strings.append(comp_string)

        max_length = 0
        for comp_string in comp_strings:
            if len(comp_string) > max_length:
                max_length = len(comp_string)

        # adjusting string spacing
        for i, comp_string in enumerate(comp_strings):
            if len(comp_string) < max_length:
                for i2 in range(max_length - len(comp_string)):
                    comp_strings[i] = comp_strings[i] + " "

        title_add = " " * (max_length - 1)
        return "CF(\n  {} {} {}\n  {} {} {}\n  {} {} {}\n  lv{}rv{}po\n)\n".format(*comp_strings, title_add, title_add)

    def __mul__(self, other):
        if type(other) == CFrame:
            s11, s12, s13, s21, s22, s23, s31, s32, s33 = self.get_components()
            o11, o12, o13, o21, o22, o23, o31, o32, o33 = other.get_components()

            m11 = s11*o11 + s12*o21 + s13*o31
            m12 = s11*o12 + s12*o22 + s13*o32
            m13 = s11*o13 + s12*o23 + s13*o33

            m21 = s21*o11 + s22*o21 + s23*o31
            m22 = s21*o12 + s22*o22 + s23*o32
            m23 = s21*o13 + s22*o23 + s23*o33

            m31 = s31*o11 + s32*o21 + s33*o31
            m32 = s31*o12 + s32*o22 + s33*o32
            m33 = s31*o13 + s32*o23 + s33*o33
            
            self = CFrame.from_components(m11, m12, m13, m21, m22, m23, m31, m32, m33)
            return self

        elif type(other) == Vector2:
            x, y = other.x, other.y
            m11, m12, m13, m21, m22, m23, m31, m32, m33 = self.get_components()

            # calculating multiplication
            new_x = m11*x + m12*y + m13*1
            new_y = m21*x + m22*y + m23*1

            # returning
            return Vector2(new_x, new_y)

        else:
            print("Invalid type for multiplication with a CFrame: " + str(type(other)))

    def get_components(self):
        m11 = self.components[0]
        m12 = self.components[1]
        m13 = self.components[2]
        m21 = self.components[3]
        m22 = self.components[4]
        m23 = self.components[5]
        m31 = self.components[6]
        m32 = self.components[7]
        m33 = self.components[8]
        return m11, m12, m13, m21, m22, m23, m31, m32, m33

    def get_angle(self):
        angle = math.acos(self.look_vector.x)
        if self.look_vector.y < 0:
            angle = 2*math.pi - math.acos(self.look_vector.x)

        return angle

    def from_components(m11, m12, m13, m21, m22, m23, m31, m32, m33):
        self = CFrame(m13, m23)
        self.components = [m11, m12, m13, m21, m22, m23, m31, m32, m33]
        self.look_vector = Vector2(m11, m21)
        self.left_vector = Vector2(m12, m22)
        return self

    def angle(angle):
        self = CFrame(0, 0)
        m11, m12, m13 = math.cos(angle), math.cos(angle + math.pi/2), self.position.x
        m21, m22, m23 = math.sin(angle), math.sin(angle + math.pi/2), self.position.y
        m31, m32, m33 = 0, 0, 1

        self.components = [m11, m12, m13, m21, m22, m23, m31, m32, m33]
        self.look_vector = Vector2(m11, m21)
        self.left_vector = Vector2(m12, m22)
        return self

    def look_at(at, look_at):
        # finding angle
        look = (look_at - at).unit
        if not look:
            print("The distance between the 'at' and 'look' cannot be 0")
            return

        angle = math.acos(look.x)
        if look.y < 0:
            angle = 2*math.pi - math.acos(look.x)

        # creating cframe
        self = CFrame.vector2(at) * CFrame.angle(angle)
        return self

    def vector2(v):
        return CFrame(v.x, v.y)