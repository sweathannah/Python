employee = [
    { 
        "Name" : "Hadizat", 
        "Details": {
            "age" : "23", 
            "position" : "HOD",
            "tasks" : ["Data collection", "Supervision"]
            },
    },
    {
        "Name" : "Zainab", 
        "Details": {
            "age" : "23", 
            "position" : "HOD",
            "tasks" : ["Data collection", "Supervision"]
            },
    },
    {
        "Name" : "Husain", 
        "Details": {
            "age" : "23", 
            "position" : "HOD",
            "tasks" : ["Data collection", "Supervision"]
            },
    },
    {
        "Name" : "Khalid", 
        "Details": {
            "age" : "23", 
            "position" : "HOD",
            "tasks" : ["Data collection", "Supervision"]
            },
    },
    {
        "Name" : "Hadizat", 
        "Details": {
            "age" : "23", 
            "position" : "HOD",
            "tasks" : ["Data collection", "Supervision"]
            },
    },
]

task1 = employee[0]["Details"]["tasks"][0]
print(f"frst task of first employee: {task1}" )

# for i in employee:
#     print(i["Name"].upper( ))

def employee_name():
    for i in employee:
        yield i["Name"].upper()

employees_name = iter(employee_name()) 
print(next(employees_name))
for i in employees_name:
    print(i)

def factors(n):
    for val in range(1, n+1):
        if n % val == 0:
            yield val
factors_of_20 = iter(factors(20))
print(next(factors_of_20))
for i in factors_of_20:
    print(i)

# istantiate a lst object
list_instance = [1, 2, 3, 4]

# convert the list to an iterator
ilterator = iter(list_instance)

# return items one at a time
print(next(ilterator))
print(next(ilterator))
print(next(ilterator))
print(next(ilterator))

#or use loop
for i in list_instance:
    print(i)

# #generator compression
# print((val for val in range(1, 20 + 1) if n % val == 0))



#list comprehension
num = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#list compressions to get the square of old numbers
squares = [x ** 2 for x in num if x > 0  and x < 20 if x % 2 == 1]
print(squares)

# prime_number = [x for x in num if x % 1 == 0 and x > 1 if x % x == 0]
prime_number = [x for x in num if all (x % i != 0 for i in range (2, x)) and x > 1]
print(f"Prime numbers btwn 0 - 20  are: {prime_number}" )

num_cube = [(i, i**3) for i in num ]
print(num_cube)


words =["duplex", "bottle", "arena", "loving", "python", "cat", "fish"]
words_to_capitals = [i.capitalize() for i in words ]
words_than_four_letters = [ i for i in words if len(i) > 4]
print(words_to_capitals)
print(words_than_four_letters)

numbers = []
def challenge():
    for i in range(21):
        if i % 3 == 0 and i % 5 == 0 and i != 0: 
            numbers.append("FizzBuzz")
        elif i % 5 == 0 and i != 0:
            numbers.append("Buzz")
        elif  i % 3 == 0 and i != 0:
            numbers.append("Fizz")  
        else:
            numbers.append(i)
    print(f" Using normal functions : {numbers}")
challenge()

fizzbuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 and i != 0 else "Buzz" if i % 5 == 0 and i != 0 else "Fizz" if i % 3 == 0 and i != 0  else i for i in range(31) ]
print(f" using list comprehension: {fizzbuzz}")
