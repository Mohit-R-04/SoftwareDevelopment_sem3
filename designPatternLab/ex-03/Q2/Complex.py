
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def complex_distance(self, other):
        return (((self.real - other.real) ** 2 + (self.imaginary - other.imaginary) ** 2) ** 0.5)
