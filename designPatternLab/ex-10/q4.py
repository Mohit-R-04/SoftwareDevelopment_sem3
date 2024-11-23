class Student:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.hobbies = []
        self.prof_bodies = []

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

    def add_prof_body(self, prof_body):
        self.prof_bodies.append(prof_body)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print("Hobbies:", self.hobbies if self.hobbies else "None")
        print("Professional Bodies:", self.prof_bodies if self.prof_bodies else "None")


class StudentRegistrationFacade:
    def __init__(self):
        self.student = None

    def register_student(self, name, age, phone):
        self.student = Student(name, age, phone)
        print("Student registered successfully!")

    def add_hobby(self, hobby):
        if self.student:
            self.student.add_hobby(hobby)
            print(f"Hobby '{hobby}' added successfully!")
        else:
            print("No student registered yet.")

    def add_prof_body(self, prof_body):
        if self.student:
            self.student.add_prof_body(prof_body)
            print(f"Professional body '{prof_body}' added successfully!")
        else:
            print("No student registered yet.")

    def store_in_file(self, filename):
        if self.student:
            with open(filename, 'w') as file:
                file.write(f"Name: {self.student.name}\n")
                file.write(f"Age: {self.student.age}\n")
                file.write(f"Phone: {self.student.phone}\n")
                file.write(f"Hobbies: {self.student.hobbies if self.student.hobbies else 'None'}\n")
                file.write(f"Professional Bodies: {self.student.prof_bodies if self.student.prof_bodies else 'None'}\n")
            print(f"Details stored in '{filename}' successfully!")
        else:
            print("No student registered to store details.")

    def display_student_details(self):
        if self.student:
            self.student.display()
        else:
            print("No student registered yet.")


# Usage Example
facade = StudentRegistrationFacade()
facade.register_student("John Doe", 22, "123-456-7890")
facade.add_hobby("Reading")
facade.add_hobby("Cycling")
facade.add_prof_body("IEEE")
facade.add_prof_body("ACM")
facade.display_student_details()
facade.store_in_file("student_details.txt")
