from abc import ABC, abstractmethod

# Base Pet Class
class Pet(ABC):
    def __init__(self, name, color, pet_type, cost):
        self.name = name
        self.color = color
        self.type = pet_type
        self.cost = cost

    def display_name(self):
        return self.name

    def display_color(self):
        return self.color

    def display_type(self):
        return self.type

    def display_cost(self):
        return self.cost

# Derived Dog Class
class Dog(Pet):
    def __init__(self, name, color, breed, cost):
        super().__init__(name, color, "dog", cost)
        self.breed = breed

    def display_breed(self):
        return self.breed

# Derived Cat Class
class Cat(Pet):
    def __init__(self, name, color, breed, cost):
        super().__init__(name, color, "cat", cost)
        self.breed = breed

    def display_breed(self):
        return self.breed

# Function to create a Dog
def create_dog():
    name = input("Enter dog's name: ")
    color = input("Enter dog's color: ")
    breed = input("Enter dog's breed: ")
    cost = int(input("Enter dog's cost: "))
    return Dog(name, color, breed, cost)

# Function to create a Cat
def create_cat():
    name = input("Enter cat's name: ")
    color = input("Enter cat's color: ")
    breed = input("Enter cat's breed: ")
    cost = int(input("Enter cat's cost: "))
    return Cat(name, color, breed, cost)

# Main function to get input and display pet details
def main():
    pet_type = input("Do you want to add a Dog or a Cat? ").lower()

    if pet_type == 'dog':
        dog = create_dog()
        print(f"\nDog Details:")
        print(f"Name: {dog.display_name()}")
        print(f"Color: {dog.display_color()}")
        print(f"Breed: {dog.display_breed()}")
        print(f"Cost: {dog.display_cost()}")
    elif pet_type == 'cat':
        cat = create_cat()
        print(f"\nCat Details:")
        print(f"Name: {cat.display_name()}")
        print(f"Color: {cat.display_color()}")
        print(f"Breed: {cat.display_breed()}")
        print(f"Cost: {cat.display_cost()}")
    else:
        print("Invalid pet type. Please enter either 'Dog' or 'Cat'.")

# Call the main function
if __name__ == "__main__":
    main()
