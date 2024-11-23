class Vector(list):
    def __init__(self, *args):
        # Ensure that only integers are allowed
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"Only integers are allowed. '{arg}' is not an integer.")
        super().__init__(args)

    # Override append method to allow only integers
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Only integers are allowed. Invalid value: {value}")
        super().append(value)

    # Override insert method to allow only integers
    def insert(self, index, value):
        if not isinstance(value, int):
            raise TypeError(f"Only integers are allowed. Invalid value: {value}")
        super().insert(index, value)

    # Override set item method to allow only integers
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError(f"Only integers are allowed. Invalid value: {value}")
        super().__setitem__(index, value)

    # Overloading + for element-wise addition
    def __add__(self, other):
        if isinstance(other, Vector):
            # Merge and remove duplicates
            merged_vector = sorted(set(list(self) + list(other)))
            return Vector(*merged_vector)
        else:
            raise TypeError("Addition is supported only between Vector objects.")

    # Overload the '-' operator to return the symmetric difference of two lists
    def __sub__(self, other):
        if isinstance(other, Vector):
            # Compute symmetric difference
            difference_vector = sorted(list(set(self).symmetric_difference(set(other))))
            return Vector(*difference_vector)
        else:
            raise TypeError("Subtraction is supported only between Vector objects.")

class EmptyVectorError(Exception):
    """Custom exception for empty vectors."""
    pass

def GetRatios(Vec1, Vec2):
    # Check if both vectors are empty
    if len(Vec1) == 0 and len(Vec2) == 0:
        raise EmptyVectorError("Both vectors are empty.")

    # Check if the vectors have different sizes
    if len(Vec1) != len(Vec2):
        raise ValueError("Vectors must be of the same size.")

    Ratio = []
    for i in range(len(Vec1)):
        try:
            if Vec2[i] == 0:
                Ratio.append('NaN')  # Handle division by zero
            else:
                Ratio.append(Vec1[i] / Vec2[i])
        except ZeroDivisionError:
            Ratio.append('NaN')  # Just a safeguard for zero division
        except Exception as e:
            raise e
    return Ratio

# Example Usage:
V1 = Vector(2, 3, 4)
V2 = Vector(1, 2)

# Add two vectors
V3 = V1 + V2
print(f"V1 + V2 = {V3}")

# Subtract two vectors
V4 = V1 - V2
print(f"V1 - V2 = {V4}")

# Get ratios
V5 = Vector(10, 20, 30)
V6 = Vector(2, 0, 5)
ratios = GetRatios(V5, V6)
print(f"Ratios: {ratios}")
