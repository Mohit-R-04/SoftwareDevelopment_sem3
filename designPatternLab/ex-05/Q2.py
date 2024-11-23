class Employee:
    # Constructor to initialize first and last names (Instance members)
    def __init__(self, first_name, last_name):
        self.first_name = first_name  # Instance member
        self.last_name = last_name      # Instance member

    # Class method to create an Employee object from a single string
    @classmethod
    def from_string(cls, name_string):
        first_name, last_name = name_string.split(' ')
        return cls(first_name, last_name)  # Return a new Employee object

# Creating an Employee object by passing two strings
emp1 = Employee('John', 'Doe')
print(f"Employee 1: First Name: {emp1.first_name}, Last Name: {emp1.last_name}")
# Output: Employee 1: First Name: John, Last Name: Doe

# Creating an Employee object by passing one string to from_string()
emp2 = Employee.from_string('Seetha Raman')
print(f"Employee 2: First Name: {emp2.first_name}, Last Name: {emp2.last_name}")
# Output: Employee 2: First Name: Seetha, Last Name: Raman
