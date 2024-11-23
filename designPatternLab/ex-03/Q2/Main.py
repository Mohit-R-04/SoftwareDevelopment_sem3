
import Centroid
import Complex
import Number
import String
import Vector

def distance(obj1, obj2):
    if isinstance(obj1, Centroid.Centroid) and isinstance(obj2, Centroid.Centroid):
        return obj1.centroid_distance(obj2)
    elif isinstance(obj1, Complex.Complex) and isinstance(obj2, Complex.Complex):
        return obj1.complex_distance(obj2)
    elif isinstance(obj1, Number.Number) and isinstance(obj2, Number.Number):
        return obj1.number_distance(obj2)
    elif isinstance(obj1, Vector.Vector) and isinstance(obj2, Vector.Vector):
        return obj1.vector_distance(obj2)
    elif isinstance(obj1, String.String) and isinstance(obj2, String.String):
        return obj1.string_distance(obj2)
    else:
        raise TypeError("Incompatible types for distance calculation")

# Example usage:
com1 = Complex.Complex(4, 3)
com2 = Complex.Complex(1, 0)
com_diff = distance(com1, com2)
print("Complex Difference:", com_diff)

n1 = Number.Number(5)
n2 = Number.Number(12)
n_diff = distance(n1, n2)
print("Number Difference:", n_diff)

v1 = Vector.Vector(1, 7, 5, 2)
v2 = Vector.Vector(3, 1, 4, 7)
v_diff = distance(v1, v2)
print("Vector Difference:", v_diff)

c1 = Centroid.Centroid(v1, v2)
c2 = Centroid.Centroid(v2, v1)
c_diff = distance(c1, c2)
print("Centroid Difference:", c_diff)

s1 = String.String("Hello")
s2 = String.String("Hi")
s_diff = distance(s1, s2)
print("String Difference:", s_diff)
