from rect import *
import time
import math

import pygame
pygame.init()
clock = pygame.time.Clock()

class BandMember(Rect):
    next_id = 0
    def __init__(self, metronome, **kwargs):
        points = [Vector2(-1, -1), Vector2(-1, 1), Vector2(1, 1), Vector2(2.5, 0), Vector2(1, -1)]
        Polygon.__init__(self, points, color=(0, 0, 150), size=Vector2(2, 2), cframe=CFrame.angle(math.pi/2), **kwargs)

        # properties
        self.metronome = metronome
        self.goal = None
        self.last_count = None
        self.id = BandMember.next_id; BandMember.next_id += 1

    def __eq__(self, other):
        if type(other) != BandMember:
            return False
        elif self.id == other.id:
            return True
        else:
            return False

    def forward_march(self, count):
        seconds = self.metronome.calculate_seconds(count)
        distance = count * 5

        self.goal = self.cframe * CFrame(distance, 0)
        self.velocity = (self.cframe.look_vector*5) * (self.metronome.tempo / 60)
        time.sleep(seconds)

        self.velocity = Vector2()
        self.cframe = self.goal
        self.goal = None
        self.last_count = count

    def right_face(self):
        self.cframe *= CFrame.angle(-math.pi/2)

    def left_face(self):
        self.cframe *= CFrame.angle(math.pi/2)

    def turn_left(self, turn, count):
        seconds = self.metronome.calculate_seconds(count)

        self.goal = self.cframe * CFrame.angle(math.radians(turn))
        self.angular_velocity = (math.radians(turn) / count) * (self.metronome.tempo / 60)
        time.sleep(seconds)

        self.angular_velocity = 0
        self.cframe = self.goal
        self.goal = None
        self.last_count = count

    def turn_right(self, turn, count):
        seconds = self.metronome.calculate_seconds(count)

        self.goal = self.cframe * CFrame.angle(-math.radians(turn))
        self.angular_velocity = (math.radians(-turn) / count) * (self.metronome.tempo / 60)
        time.sleep(seconds)

        self.angular_velocity = 0
        self.cframe = self.goal
        self.goal = None
        self.last_count = count

    def mark_time(self, count):
        self.goal = self.cframe
        time.sleep(self.metronome.calculate_seconds(count))
        self.goal = None
        self.last_count = count

    def left_pinwheel(self, count, pivot):
        seconds = self.metronome.calculate_seconds(count)

        angle = (count / 8) * math.pi/2
        start_angle = self.cframe.get_angle()
        self.goal = CFrame(pivot) * CFrame.angle(angle) * CFrame(self.cframe.p - pivot) * CFrame.angle(start_angle)
        
        # smooth rotating
        last_time = time.time()
        start_time = last_time
        while time.time() - start_time < seconds:
            curr_time = time.time()
            dt = (curr_time - last_time) * (self.metronome.tempo / 60)
            last_time = curr_time
            
            add_angle = angle * (dt / count)
            start_angle = self.cframe.get_angle()
            self.cframe = CFrame(pivot) * CFrame.angle(add_angle) * CFrame(self.cframe.p - pivot) * CFrame.angle(start_angle)

            # ticking
            clock.tick(60)

        self.cframe = self.goal
        self.goal = None
        self.last_count = count

    def right_pinwheel(self, count, pivot):
        seconds = self.metronome.calculate_seconds(count)

        angle = (-count / 8) * math.pi/2
        start_angle = self.cframe.get_angle()
        self.goal = CFrame(pivot) * CFrame.angle(angle) * CFrame(self.cframe.p - pivot) * CFrame.angle(start_angle)
        
        # smooth rotating
        last_time = time.time()
        start_time = last_time
        while time.time() - start_time < seconds:
            curr_time = time.time()
            dt = (curr_time - last_time) * (self.metronome.tempo / 60)
            last_time = curr_time
            
            add_angle = angle * (dt / count)
            start_angle = self.cframe.get_angle()
            self.cframe = CFrame(pivot) * CFrame.angle(add_angle) * CFrame(self.cframe.p - pivot) * CFrame.angle(start_angle)

            # ticking
            clock.tick(60)

        self.cframe = self.goal
        self.goal = None
        self.last_count = count