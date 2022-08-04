from band_member import *
import threading

class Squad:
    def __init__(self, surface, member_count=4, spacing=2, right_cf=CFrame()):
        self.surface = surface
        self.member_count = member_count
        self.spacing = spacing
        self.members = []

        for i in range(self.member_count):
            member = BandMember(surface=self.surface)
            member.cframe = right_cf * CFrame(0, -i*self.spacing*5)
            self.members.append(member)

    def forward_march(self, count):
        def forward(member):
            member.forward_march(count)

        for member in self.members:
            thread = threading.Thread(target=forward, args=[member])
            thread.start()

        time.sleep(count)

    def turn_left(self, turn, count):
        def left(member):
            member.turn_left(turn, count)

        for member in self.members:
            thread = threading.Thread(target=left, args=[member])
            thread.start()

        time.sleep(count)

    def turn_right(self, turn, count):
        def right(member):
            member.turn_left(turn, count)

        for member in self.members:
            thread = threading.Thread(target=right, args=[member])
            thread.start()

        time.sleep(count)

    def mark_time(self, count):
        def mark(member):
            member.mark_time(count)

        for member in self.members:
            thread = threading.Thread(target=mark, args=[member])
            thread.start()

        time.sleep(count)