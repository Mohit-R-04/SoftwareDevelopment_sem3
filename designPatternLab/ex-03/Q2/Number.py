
class Number:
    def __init__(self, value):
        self.value = value

    def number_distance(self, other):
        return abs(self.value - other.value)
