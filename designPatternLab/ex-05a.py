# 1. Using *args
def Average(*args):
    if len(args) == 0:
        return "Length should be more than one."
    total = sum(args)
    leng = len(args)
    return total / leng

# Example usage for Average
print(Average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Output: 5.5

# 2. Using **kwargs
def ShowOff(**kwargs):
    # Check if 'mark' is present in the keyword arguments
    if 'mark' in kwargs:
        # Get the value of 'mark'
        mark = kwargs['mark']
        # Check if 'mark' is greater than 60
        if mark > 60:
            # Get the value of 'name' if it exists
            name = kwargs.get('name', 'Unknown')
            # Return the name and marks
            return f"Name: {name}, Marks: {mark}"
        else:
            name = kwargs.get('name', 'Unknown')
            sub_name = kwargs.get('sub_name')
            teacher_name = kwargs.get('teacher_name')
            return f'''
Name: {name}
Subject Name: {sub_name}
Teacher Name: {teacher_name}
Marks are 60 or below'''
    else:
        return "Marks are not provided"

# Example usage for ShowOff
print(ShowOff(name="Alice", mark=75))  # Output: Name: Alice, Marks: 75
print(ShowOff(name="Bob", mark=50, sub_name='Maths', teacher_name='Bob'))  # Output: Marks are 60 or below
print(ShowOff(name="Charlie"))  # Output: Marks are not provided
