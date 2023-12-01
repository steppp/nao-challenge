''' Class which describes a move that can be performed by NAO '''

class NAOmove():
    def __init__(self, name, duration, preconditions=None, postconditions=None):
        self.name = name
        self.duration = duration
        self.preconditions = preconditions if preconditions != None else {}
        self.postconditions = postconditions if postconditions != None else {}

    def __str__(self):
        return f'NAOmove: {self.name}'

    def __repr__(self):
        return f'NAOmove: {self.name}'

    def __gt__(self, other):
        return self.duration > other.duration

    def __lt__(self, other):
        return self.duration < other.duration

