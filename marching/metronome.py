import threading

class Metronome:
    def __init__(self, tempo=60):
        self.tempo = tempo
        
    def set_tempo(self, to_set):
        self.tempo = 60

    def calculate_seconds(self, count):
        return count * (60 / self.tempo)