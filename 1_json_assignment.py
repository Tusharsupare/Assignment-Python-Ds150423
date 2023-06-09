import json

class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Reading information from json file and storing it in a list

employee_list = []
file = open(r"assement question\json_assignment\employee.json","r")
data = json.load(file)  
for employee_data in data:
    name = employee_data["Name"]
    dob =  employee_data["DOB"]
    height = employee_data["Height"]
    city = employee_data["City"]
    state = employee_data["State"]
    employee = Employee(name, dob, height, city, state)
    employee_list.append(employee)

# Printing the list of employement object
for employee in employee_list:
    print("Name:", employee.name)
    print("D.O.B:", employee.dob)
    print(f"Height:", employee.height,"inches")
    print("City:", employee.city)
    print("State:", employee.state)
    print()


