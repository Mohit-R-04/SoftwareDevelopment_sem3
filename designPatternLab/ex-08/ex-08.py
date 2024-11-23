import pickle

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

class Faculty(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

class Staff(Person):
    def __init__(self, name, position, salary):
        super().__init__(name)
        self.position = position
        self.salary = salary

# Global list to store people
PplAsn = []

def add_person(person):
    PplAsn.append(person)

def filter_people(category, department=None):
    if category == 'Student':
        return [p for p in PplAsn if isinstance(p, Student) and (department is None or p.department == department)]
    elif category == 'Faculty':
        return [p for p in PplAsn if isinstance(p, Faculty) and (department is None or p.department == department)]
    elif category == 'Staff':
        return [p for p in PplAsn if isinstance(p, Staff)]
    return []

def add_security_bonus():
    for person in PplAsn:
        if isinstance(person, Staff) and person.position == 'Security':
            person.salary += 2000

def save_to_file(filename):
    with open(filename, 'wb') as f:
        pickle.dump(PplAsn, f)

def load_from_file(filename):
    global PplAsn
    with open(filename, 'rb') as f:
        PplAsn = pickle.load(f)

# Sample usage
if __name__ == "__main__":
    while True:
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Add Staff")
        print("4. Filter People")
        print("5. Add Security Bonus")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Unique list of faculty")
        print("9. EXIT")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            department = input("Enter department: ")
            add_person(Student(name, department))

        elif choice == '2':
            name = input("Enter faculty name: ")
            department = input("Enter department: ")
            add_person(Faculty(name, department))

        elif choice == '3':
            name = input("Enter staff name: ")
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            add_person(Staff(name, position, salary))

        elif choice == '4':
            category = input("Enter category (Student/Faculty/Staff): ")
            department = input("Enter department (leave empty for all): ")
            results = filter_people(category, department if department else None)
            for person in results:
                print(f"{person.name} - {person.__class__.__name__} - {getattr(person, 'department', 'N/A')}")

        elif choice == '5':
            add_security_bonus()
            print("Security bonus added.")

        elif choice == '6':
            filename = input("Enter filename to save: ")
            save_to_file(filename)
            print("Data saved.")

        elif choice == '7':
            filename = input("Enter filename to load: ")
            load_from_file(filename)
            print("Data loaded.")

        elif choice == '8':
            uniq_fac = set()
            uniq_fac_dep = set()
            print('Unique members of faculty:')
            for person in PplAsn:
                if isinstance(person, Faculty):
                    uniq_fac.add(person.name)
            print(uniq_fac)

            print('Unique members of faculty in a specific department:')
            dep = input('Enter a department: ')
            for person in PplAsn:
                if person.department == dep and isinstance(person, Faculty):
                    uniq_fac_dep.add(person.name)
            print(uniq_fac_dep)

        elif choice == '9':
            break

        else:
            print("Invalid option. Please try again.")
