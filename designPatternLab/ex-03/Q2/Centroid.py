# Centroid.py
class Centroid:
    def __init__(self, *coordinates):
        self.coordinates = coordinates
    
    def centroid_distance(self, other):
        if len(self.coordinates) == len(other.coordinates):
            square = 0
            for a, b in zip(self.coordinates, other.coordinates):
                diff = a - b  # Using the __sub__ method of Vector
                square += sum(coord ** 2 for coord in diff.coordinates)
            return square ** 0.5
        else:
            raise ValueError("Centroids must have the same number of dimensions")
