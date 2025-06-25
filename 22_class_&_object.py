# Define a class
class Student:
    # Constructor to initialize the object
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Method to display student details
    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)

# Create objects of the class
student1 = Student("Arjun", 101)
student2 = Student("Priya", 102)

# Call the method using objects
student1.display_info()
print("----------")
student2.display_info()

