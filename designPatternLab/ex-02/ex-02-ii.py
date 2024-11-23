import math

# 1. Point Class 
class Point: 
    def __init__(self, x, y): 
        self.xcod = x 
        self.ycod = y 
 
    def getpoint(self): 
        return self.xcod, self.ycod 
 
    def showpoint(self): 
        print(f'{self.xcod},{self.ycod}') 

# 2a. Circle Class 
class Circle: 
    def __init__(self, r=0): 
        self.radius = r 
        self.center = None 
        self.point = None 
        self.area = None 
 
    def getcircle(self): 
        while True:
            try:
                # Taking input and splitting based on comma
                a = input('Enter center co-ordinates(x,y): ').strip().split(',')
                b = input('Enter point co-ordinates(x,y): ').strip().split(',')

                # Ensure that both inputs are in the correct format
                if len(a) != 2 or len(b) != 2:
                    raise ValueError("Please enter two comma-separated values.")

                # Converting string values to float
                self.center = Point(float(a[0]), float(a[1])) 
                self.point = Point(float(b[0]), float(b[1])) 

                # Calculate radius and area
                self.radius = ((self.center.xcod - self.point.xcod) ** 2 + 
                               (self.center.ycod - self.point.ycod) ** 2) ** 0.5 
                self.area = 3.1415 * (self.radius) ** 2 
                print(f"Radius: {self.radius}")
                break  # Exit the loop after successful input and calculation

            except ValueError as e:
                print(f"Error: {e}. Please try again.")  # Show error and retry input
 
    def getradius(self): 
        return self.radius 
 
    def getarea(self): 
        return self.area 

# 2b. Cone Class (Inherits from Circle) 
class Cone(Circle): 
    def __init__(self): 
        super().__init__() 
        self.apex = None 
        self.volume = None 
 
    def getcone(self): 
        self.getcircle() 
        while True:
            try:
                # Taking apex input and splitting it
                apex_x, apex_y = map(float, input("Enter the apex of the cone (x, y): ").strip().split(','))  
                self.apex = Point(apex_x, apex_y) 
                
                # Calculate height
                height = math.sqrt((self.apex.xcod - self.center.xcod) ** 2 + 
                                   (self.apex.ycod - self.center.ycod) ** 2) 
                
                # Calculate volume
                self.volume = (1/3) * 3.1415 * (self.radius ** 2) * height
                break  # Exit the loop after successful input and calculation
            except ValueError:
                print("Error: Please enter valid numbers for the apex coordinates.")
 
    def getvolume(self): 
        return self.volume 

# 3a. Regular_Polygon Class 
class Regular_Polygon: 
    def __init__(self): 
        self.lop = [] 
        self.num_sides = 0 
 
    def getdetails(self): 
        self.num_sides = int(input("Enter the number of sides: ")) 
        for i in range(self.num_sides): 
            while True:
                try:
                    x, y = map(float, input(f"Enter point {i+1} co-ordinates (x, y): ").strip().split(','))
                    self.lop.append(Point(x, y))
                    break
                except ValueError:
                    print("Error: Please enter valid coordinates (x, y) in numeric form.")

# 3b. Square Class (Inherits from Regular_Polygon) 
class Square(Regular_Polygon): 
    def __init__(self): 
        super().__init__() 
 
    def calculate_area(self): 
        side_length = math.sqrt((self.lop[0].xcod - self.lop[1].xcod) ** 2 + 
                                 (self.lop[0].ycod - self.lop[1].ycod) ** 2) 
        return side_length ** 2 
 
    def calculate_perimeter(self): 
        side_length = math.sqrt((self.lop[0].xcod - self.lop[1].xcod) ** 2 + 
                                 (self.lop[0].ycod - self.lop[1].ycod) ** 2) 
        return 4 * side_length 
 
    def calculate_volume(self): 
        return 0 

# Testing the classes 
cone = Cone() 
cone.getcone() 
print("Volume of the cone: ", cone.getvolume()) 
print() 

square = Square() 
square.getdetails() 
print("Area of the square: ", square.calculate_area()) 
print("Perimeter of the square: ", square.calculate_perimeter()) 
print("Volume of the square: ", square.calculate_volume())
