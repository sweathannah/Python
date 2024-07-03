

class Employee:
    def __init__(self, name:str, age:int, positiion:str, salary:float):
        self.name = name
        self.age = age
        self.position = positiion
        self.salary = salary

    def update_position(self, new_position):
        self.position = new_position

    def update_salary(self, new_salary):
        self.salary = new_salary

    def __str__(self):
        return f"Employee's name: {self.name}, {self.name}'s age: {self.age}, {self.name}'s position: {self.position}, {self.name}'s salary: {self.salary} "
    

user = Employee("sultanat", 17, "CEO", 1000)
print(user)
    

class Company:
    def __init__(self,):
        self.employees = []


    def add_employee(self, name:str):
        self.employees.append(name)
        print(f"Employee {name} added successfully")

    def remove_employee(self, name):
        self.employees.remove(name)
        print(f"Employee {name} removed successfully")

    def update_employee(self, name, position=None, salary=None):
        for employee in self.employees:
            if employee == name:
                if position:
                    employee.update_position(position)
                if salary:
                    employee.update_salary(salary)
                return True
            print(f"Employee {name} position updated to {position} successfully")
        return False
    def view_all_employees(self):
        for employee in self.employees:
            print(employee)




user1 = Company()
user1.add_employee("Sultanat")
user1.add_employee("Hadizat")
# user1.remove_employee("Sultanat")
# user1.update_employee("Sultanat", "manager", "15000")
user1.view_all_employees()


