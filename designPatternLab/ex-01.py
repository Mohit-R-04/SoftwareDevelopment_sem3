class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None

    def set_num1(self):
        try:
            self.num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Please provide a valid number.")

    def set_num2(self):
        try:
            self.num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please provide a valid number.")

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

# Sample usage
calculator = Calculator()

# Getting input from user
calculator.set_num1()
calculator.set_num2()

# Performing operations
print("Addition result:", calculator.add())
print("Subtraction result:", calculator.sub())
print("Multiplication result:", calculator.mul())
