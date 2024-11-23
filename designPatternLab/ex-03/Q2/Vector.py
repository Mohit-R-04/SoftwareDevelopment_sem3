# Vector.py
class Vector:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __sub__(self, other):
        if len(self.coordinates) == len(other.coordinates):
            return Vector(*(a - b for a, b in zip(self.coordinates, other.coordinates)))
        else:
            raise ValueError("Vectors must have the same number of dimensions")

    def __str__(self):
        return str(self.coordinates)

    def vector_distance(self, other):
        if len(self.coordinates) == len(other.coordinates):
            square = sum((a - b) ** 2 for a, b in zip(self.coordinates, other.coordinates))
            return square ** 0.5
        else:
            raise ValueError("Vectors must have the same number of dimensions")
