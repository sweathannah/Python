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
    


class Dog:
    number = 0
    # __number = 0   #private attribute
    #_protected = "i am a protected variable"
    def __init__(self,  name):
        self.name = name
        self.Number = Dog.__number
        self.Number += 1
        self.__dognumber = Dog.number

    def get_dognumber(self):
        return self.__dognumber 

    def bark(self):
        print(f"{self.name} says woof!")


jack = Dog("jack")
print(f"{jack.name} position is No.{get_dognumber(self)}")