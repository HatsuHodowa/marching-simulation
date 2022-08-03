import sys
sys.path.append("math")

from cframe import *

# main class
class Camera:
    next_id = 0
    def __init__(self, **kwargs):
        self.cframe = CFrame()
        self.zoom = 1
        self.movement_enabled = True

        self.zoom_min = 0.1
        self.zoom_max = 2

        self.surface = None
        self.movespeed = 15
        self.rotatespeed = math.pi/6
        self.zoomspeed = 0.25

        self.target = None

        # kwargs
        for key in kwargs:
            if key == "surface":
                self.surface = kwargs["surface"]
            elif key == "movespeed":
                self.movespeed = kwargs["movespeed"]
            elif key == "rotatespeed":
                self.rotatespeed = kwargs["rotatespeed"]
            elif key == "zoomspeed":
                self.zoomspeed = kwargs["zoomspeed"]

        # adding id
        self.id = Camera.next_id
        Camera.next_id += 1

    def __eq__(self, other):
        if type(other) == Camera:
            if self.id == other.id:
                return True

        return False

    def point_on_camera(self, point):
        cam_pos = CFrame.vector2(self.cframe.p*-10)
        cam_angles = CFrame.angle(-self.cframe.get_angle())
        cam_point = cam_angles * (cam_pos * point)
        cam_point *= self.zoom

        return cam_point

    def lock_on_target(self):
        if self.target == None:
            return

        self.cframe = CFrame(self.target.cframe.p)