from rect import *
import time
import math

import pygame
pygame.init()
clock = pygame.time.Clock()

class BandMember(Rect):
    def __init__(self, **kwargs):
        points = [Vector2(-1, -1), Vector2(-1, 1), Vector2(1, 1), Vector2(2.5, 0), Vector2(1, -1)]
        Polygon.__init__(self, points, color=(0, 0, 150), size=Vector2(2, 2), cframe=CFrame.angle(math.pi/2), **kwargs)

        self.goal = None

    def forward_march(self, count):
        self.goal = self.cframe * CFrame(5*count, 0)
        self.velocity = self.cframe.look_vector*5
        time.sleep(count)
        self.velocity = Vector2()
        self.cframe = self.goal
        self.goal = None

    def turn_left(self, turn, count):
        self.goal = self.cframe * CFrame.angle(math.radians(turn))
        self.angular_velocity = math.radians(turn) / count
        time.sleep(count)
        self.angular_velocity = 0
        self.cframe = self.goal
        self.goal = None

    def turn_right(self, turn, count):
        self.goal = self.cframe * CFrame.angle(-math.radians(turn))
        self.angular_velocity = -math.radians(turn) / count
        time.sleep(count)
        self.angular_velocity = 0
        self.cframe = self.goal
        self.goal = None

    def mark_time(self, count):
        self.goal = self.cframe
        time.sleep(count)
        self.goal = None