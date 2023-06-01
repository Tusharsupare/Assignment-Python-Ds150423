class Student:
    def __init__(self):
        self.__name = None   # i use self.__ to private name and roll number 
        self.__rollNumber = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll_number(self):
        return self.__rollNumber

    def set_roll_number(self, roll_number):
        self.__rollNumber = roll_number

# Creating an instance of the Student class
student = Student()

# Accessing the methods of the Student class
student.set_name("Tushar Supare")
name = student.get_name()
student.set_roll_number(14369)
rollNumber = student.get_roll_number()

# Printing values
print(name)
print(rollNumber)

