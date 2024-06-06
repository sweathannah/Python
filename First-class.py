# name = input("What is your name?")
# year = input("What year were you born?")
# print("Hello " + name + " nice to meet you")

# print("Hello World")

# first_name = str(input("What is your first name?"))
# last_name = str(input("What is your last name? "))
# year_of_birth = abs(int(input("Enter your year of birth: ")))

# age = 2024 - year_of_birth
 
# print(f"Hello {first_name} {last_name}, you are {age} years old" )

# fruits = ["orange", "mango", "apple", "cashew"]
# for fruit in fruits:
#     print(fruit)

# for number in range(2,10,2):
#     print(number)

# for i in range(10):
#     if i > 5:
#         print(i)
#         break

# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#     continue 

def test():
    food = ['eba', 'amala', 'indomie', 'eggs']
    for i in range(len(food)):
        if i % 2 == 0:
            print(i,food[i])    
        continue        
test()

def area(length, breadth):
    return length * breadth
print(area(4, 5))

def interest(p:int ,r,t):
    result = int((p * r * t)/100)
    return result

print(f"Interest equals to", interest(20,10,5))





