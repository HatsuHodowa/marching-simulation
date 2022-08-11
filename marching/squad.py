from telnetlib import theNULL
from band_member import *
import threading
import math

class Squad:
    def __init__(self, surface, metronome, left_cf=CFrame(), member_count=4, spacing=2):
        self.surface = surface
        self.member_count = member_count
        self.spacing = spacing
        self.members = []

        self.metronome = metronome
        for i in range(self.member_count):
            member = BandMember(self.metronome, surface=self.surface)
            member.cframe = left_cf * CFrame(0, -i*self.spacing*5)
            self.members.append(member)

    def left_member(self):
        left_dir = self.members[0].cframe.left_vector
        left_member = None

        for member in self.members:
            left_dist = member.cframe.p.dot(left_dir)
            if left_member == None:
                left_member = member
            elif left_member.cframe.p.dot(left_dir) < left_dist:
                left_member = member

        # returning
        return left_member

    def right_member(self):
        left_member = self.left_member()
        if left_member == self.members[0]:
            return self.members[3]
        elif left_member == self.members[3]:
            return self.members[0]

    def thread_command(self, command, *args):
        def run_command():
            getattr(self, command)(*args)

        thread = threading.Thread(target=run_command)
        thread.start()

    def forward_march(self, count):
        members_complete = []
        def forward(member):
            member.forward_march(count)
            members_complete.append(member)

        for member in self.members:
            thread = threading.Thread(target=forward, args=[member])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def right_face(self):
        for member in self.members:
            member.right_face()

    def left_face(self):
        for member in self.members:
            member.left_face()

    def turn_left(self, turn, count):
        members_complete = []
        def left(member):
            member.turn_left(turn, count)
            members_complete.append(member)

        for member in self.members:
            thread = threading.Thread(target=left, args=[member])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def turn_right(self, turn, count):
        members_complete = []
        def right(member):
            member.turn_right(turn, count)
            members_complete.append(member)

        for member in self.members:
            thread = threading.Thread(target=right, args=[member])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def mark_time(self, count):
        seconds = self.metronome.calculate_seconds(count)
        time.sleep(seconds)

    def left_pinwheel(self, count, pivot=None):
        # finding pivot point
        if not pivot:
            pivot = self.left_member().cframe.p + self.left_member().cframe.left_vector*5

        # running command
        members_complete = []
        def pinwheel(member):
            member.left_pinwheel(count, pivot)
            members_complete.append(member)

        for member in self.members:
            thread = threading.Thread(target=pinwheel, args=[member])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def right_pinwheel(self, count, pivot=None):
        # finding pivot point
        if not pivot:
            pivot = self.right_member().cframe.p + -self.right_member().cframe.left_vector*5

        # running command
        members_complete = []
        def pinwheel(member):
            member.right_pinwheel(count, pivot)
            members_complete.append(member)

        for member in self.members:
            thread = threading.Thread(target=pinwheel, args=[member])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def left_slant(self):
        members_complete = []
        def forward(member, forward):
            member.forward_march(forward)
            member.mark_time(8 - forward)
            members_complete.append(member)

        for i, member in enumerate(self.members):
            counts = (3 - i)*2 + 1
            if self.left_member() == self.members[3]:
                counts = i*2 + 1

            thread = threading.Thread(target=forward, args=[member, counts])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def right_slant(self):
        members_complete = []
        def forward(member, forward):
            member.forward_march(forward)
            member.mark_time(8 - forward)
            members_complete.append(member)

        for i, member in enumerate(self.members):
            counts = i*2 + 1
            if self.left_member() == self.members[3]:
                counts = (3 - i)*2 + 1

            thread = threading.Thread(target=forward, args=[member, counts])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)

    def collapse(self):
        # finding member in front
        front_member = None
        front_dir = self.members[0].cframe.look_vector

        for member in self.members:
            if front_member == None:
                front_member = member
            else:
                forward_dist = member.cframe.p.dot(front_dir)
                if forward_dist > front_member.cframe.p.dot(front_dir):
                    front_member = member

        # collapsing
        members_complete = []
        goal_pos = front_member.cframe.p + front_dir*5 # one step
        def coll(member):
            dist = goal_pos.dot(front_dir) - member.cframe.p.dot(front_dir)
            count = dist / 5
            member.forward_march(count)
            members_complete.append(member)

        # running threads
        for member in self.members:
            thread = threading.Thread(target=coll, args=[member])
            thread.start()

        while len(members_complete) != self.member_count:
            time.sleep(0.1)