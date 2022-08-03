import pygame
pygame.init()

import sys
import math

sys.path.append("math")
sys.path.append("services")
sys.path.append("render")
from cframe import *
from tagservice import *
from camera import *

class Polygon:
    all_polygons = []
    next_id = 0
    def __init__(self, points, **kwargs):
        self.points = points # each point is a vector2 relative to the center point

        # physical properties
        self.cframe = CFrame()
        self.size = Vector2(5, 5)

        self.velocity = Vector2()
        self.angular_velocity = 0

        # appearance properties
        self.surface = None
        self.color = (0, 0, 0)
        self.width = 0

        # kwargs
        for kw in kwargs:
            if kwargs[kw] == None:
                continue
            setattr(self, kw, kwargs[kw])
        self.kwargs = kwargs

        # id
        self.id = Polygon.next_id
        Polygon.next_id += 1

        # inserting into list
        Polygon.all_polygons.append(self)

    def destroy(self):
        if self in Polygon.all_polygons:
            Polygon.all_polygons.remove(self)
        del self

    def __eq__(self, other):
        if type(other) != Polygon:
            return False

        if self.id == other.id:
            return True
        else:
            return False

    def calculate_points(self):
        global_points = []

        for point in self.points:
            poly_cf = (CFrame.vector2(self.cframe.p*10) * CFrame.angle(self.cframe.get_angle()))
            new_point = poly_cf * (point * self.size*10)
            tags = Tag.get_tags(self.surface)
            for tag in tags:
                if type(tag.tag) == Camera:
                    new_point = tag.tag.point_on_camera(new_point)

            global_points.append(new_point)

        return global_points

    def update_physics(self, dt):
        new_pos = CFrame.vector2(self.cframe.position + self.velocity*dt)
        new_angle = CFrame.angle(self.cframe.get_angle() + self.angular_velocity*dt)
        self.cframe = new_pos * new_angle

    def calculate_furthest_vertex(self):
        furthest = None
        for point in self.points:
            if not furthest or furthest.magnitude < point.magnitude:
                furthest = point

        return furthest

    def is_visible(self):
        # finding camera
        cam = None
        tags = Tag.get_tags(self.surface)
        for tag in tags:
            if type(tag.tag) == Camera:
                cam = tag.tag

        if not cam:
            return False

        # finding furthest distance
        furthest_point = self.calculate_furthest_vertex()
        w, h = self.surface.get_size()
        w, h = w/(10 * cam.zoom), h/(10 * cam.zoom)
        cam_diag = math.sqrt(w**2 + h**2)/2
        furthest_dist = furthest_point.magnitude*max(self.size.x, self.size.y) + cam_diag

        # checking distance from camera center
        dist = (self.cframe.p - cam.cframe.p).magnitude
        return dist <= furthest_dist

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

        pygame.draw.polygon(self.surface, self.color, tuple_points, int(bd_width + 0.5))

    def get_surface_polygons(surface):
        return_list = []

        for poly in Polygon.all_polygons:
            if poly.surface == surface:
                return_list.append(poly)

        return return_list