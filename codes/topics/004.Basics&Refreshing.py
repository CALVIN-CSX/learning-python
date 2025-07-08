"""
  Python Basics Refresher

This program is a personal revision of core Python concepts to refresh my memory.
It includes examples of:

🔹 Variable declarations and printing (including f-strings)
🔹 Conditional statements (if, elif, else)
🔹 Taking input and using typecasting (int, float, str, bool)
🔹 Boolean logic and input validation
🔹 Using string methods like .lower()
🔹 Loops: for loops, while loops, and user-driven loop exits
🔹 Basic user interaction and input-based flow control
🔹 Truthy/falsy check using type conversion
🔹 Slicing

Note: This script also includes personal notes and exploratory comments
for better conceptual clarity during learning.
"""
# Declaring and initializing variables
a = 5
b = "String"
boolean = True

# Printing statements or variables
print("hello world")
print(a)
print(f"b is a {type(b)} and its contents are {b}")  # f-string: a clean way to display variables
print("3 + 2 is equal to", a)                         # Another way to display variables

# Conditional statements
if a > 0:
    print("a is greater than 0")
elif a < 5:
    print("a is less than 5")
elif a == 5:
    print("a is equal to 5")
elif a < 0:
    print("a is less than 0")
else:
    print("a is greater than 5")

# Taking input
name = input("Enter your name: ")
age = int(input("Enter age (in numbers): "))

# Boolean input (basic version)
likes_coding = input("Do you like coding? (yes/no): ") == "yes"
print(name)
print(age)
print(likes_coding)

# Boolean input with string method refinement
likes_coding = input("Do you like coding? (yes/no): ").lower() == "yes"

# Conditional statement based on boolean
if likes_coding:
    print("You like coding.")
else:
    print("You don't like coding.")

# Typecasting (something new I'm learning in Python)
age = float(age)
age += 0.5
print(age)

age = str(age)
age += ".5"
print(age)

age = bool(age)
print(age)  # Outputs True if age is not empty or zero

# Note to self:
# In Python, memory addresses aren’t shown unless explicitly requested using the id() function.
#loops
for i in range(1,10):
    print(i)
while i>0:
    print(i)
    i = i-1
num=int(input("Enter a positive number: "))
while num<0:
    print("You Entered a negative number.")
else:
    print(f"You Entered a positive number.{num}")
food=input("Enter food you like(press q to quit): ")
while food!="q":#or while not can be used
    print(f"You like {food}.")
    food=input("Enter another food you like(press q to quit): ")
print("you exited the program.")
#slicing
food=input("Enter food you like:")
print(food[::-1])#reverses the string
print(food[2:3])#starts after the second letter eg. "shawarma" will give "a"