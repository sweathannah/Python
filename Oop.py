# Object oriented programmng

class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def change_salary(self,amount):
        self.salary += amount

    def __str__(self):
        return f"{self.name}'s salary is: {self.salary}"

# #create employee instances
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

# #change the salaries by 10k
# employee1.change_salary(10000)
# employee2.change_salary(10000)

employees = [
     Employee("Alice", 50000),
     Employee("Bob", 60000),
     Employee("Charlie", 60000),
     Employee("Avast", 2000)
]

for employee in employees:
    if employee.name != "Avast":
        employee.change_salary(10000)

for employee in employees:
    print(f"{employee.name}'s new salary: {employee.salary}")

p3 = Employee("Dane", 50000)
print(p3)
# p3.change_salary(10000)
# print(f"{p3.name}'s new salary: {p3.salary}")




# class Animal:
#     def __init__(self,name,specie):
#         self.name = name
#         self.specie = specie
#     def speak(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, "Dog")
#         self.breed = breed
#     def speak(self):
#         return f"{self.name} says Woof!"
    


# class Dog:
#     number = 0
#     # __number = 0   #private attribute
#     #_protected = "i am a protected variable"
#     def __init__(self,  name):
#         self.name = name
#         self.Number = Dog.__number
#         self.Number += 1
#         self.__dognumber = Dog.number

#     def get_dognumber(self):
#         return self.__dognumber 

#     def bark(self):
#         print(f"{self.name} says woof!")


# jack = Dog("jack")
# # print(f"{jack.name} position is No.{get_dognumber(self)}")



class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary:.2f}"

    def update_position(self, new_position):
        self.position = new_position

    def update_salary(self, new_salary):
        self.salary = new_salary


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully")
        print(f"list of employee : {self.employees}")

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return True
        return False

    def update_employee(self, name, position=None, salary=None):
        for employee in self.employees:
            if employee.name == name:
                if position:
                    employee.update_position(position)
                if salary:
                    employee.update_salary(salary)
                return True
        return False

    def view_all_employees(self):
        for employee in self.employees:
            print(employee)

    def find_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

user = Company()
user.add_employee("sultanat")

def user_interface():
    company = Company()

    while True:
        print("\nEmployee Management System")
        print("1. Add a new employee")
        print("2. Remove an employee")
        print("3. Update an employee's details")
        print("4. View all employees")
        print("5. Find an employee by name")
        print("Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter employee's name: ")
            age = int(input("Enter employee's age: "))
            position = input("Enter employee's position: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, age, position, salary)
            company.add_employee(employee)
            print(f"Employee {name} added successfully.")


        

