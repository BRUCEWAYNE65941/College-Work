# ================================================
#  PYTHON BASICS - ALL IN ONE FILE (10 Lessons)
#  Run this single file to learn all Python fundamentals
# ================================================

print("="*60)
print("     WELCOME TO PYTHON BASICS - ALL IN ONE!")
print("="*60)

# 1. Variables & Data Types
print("\n1. Variables & Data Types")
name = "Alice"
age = 25
height = 1.68
is_student = True
hobbies = ["coding", "music", "gaming"]  # list

print(f"Name: {name}, Age: {age}, Height: {height}m")
print(f"Is student? {is_student}")
print(f"Hobbies: {hobbies}")
print(f"Age is of type: {type(age)}")

# 2. Input + If-Elif-Else
print("\n2. Input + Conditional Statements")
age_input = int(input("Enter your age: "))

if age_input >= 18:
    print("You are an adult!")
elif age_input >= 13:
    print("You are a teenager!")
else:
    print("You are a kid!")

# 3. For Loop + Range
print("\n3. For Loops")
print("Counting 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

print("Even numbers from 0 to 20:")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# 4. While Loop + Simple Game
print("\n4. While Loop - Number Guessing Game")
import random
secret = random.randint(1, 10)
guess = 0
attempts = 0

print("Guess the number between 1 and 10!")
while guess != secret:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")

# 5. Lists
print("\n5. Lists (like arrays)")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

fruits.append("orange")
fruits.insert(1, "mango")
fruits[0] = "kiwi"

print("After modifications:", fruits)
print("Second fruit:", fruits[1])
print("Last two fruits:", fruits[-2:])

print("Looping through list:")
for fruit in fruits:
    print("→", fruit.upper())

# 6. Functions
print("\n6. Functions")
def greet(name="World"):
    return f"Hello {name}!"

def calculator(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "Error"

print(greet("Python"))
print(greet())

sum_result, sub, mul, div = calculator(10, 3)
print(f"10 + 3 = {sum_result}")
print(f"10 * 3 = {mul}")
print(f"10 / 3 = {div:.2f}")

# 7. Dictionaries
print("\n7. Dictionaries (key-value pairs)")
student = {
    "name": "Emma",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Python"]
}

print("Student info:", student)
print("Name:", student["name"])
print("Subjects:", student["subjects"])

student["age"] += 1
student["school"] = "Tech University"

print("Updated student:", student)

print("Looping through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 8. String Manipulation
print("\n8. Strings")
message = "   Python is Awesome!   "
print("Original:", message)
print("Lower:", message.lower())
print("Upper:", message.upper())
print("Stripped:", message.strip())
print("Replaced:", message.strip().replace("Awesome", "SUPER COOL"))

words = message.split()
print("Words list:", words)
print("Joined:", " | ".join(words))

# Check if word exists
if "python" in message.lower():
    print("'python' found in message!")

# 9. File Handling (Write & Read)
print("\n9. File Handling")
# Writing to file
with open("my_notes.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("Today I learned all Python basics.\n")
    file.write("Keep practicing!\n")

print("File 'my_notes.txt' created!")

# Reading from file
print("Reading the file back:")
with open("my_notes.txt", "r") as file:
    content = file.read()
    print(content)

# 10. Basic Error Handling
print("\n10. Error Handling (try-except)")
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 divided by {number} = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
else:
    print("Division successful!")
finally:
    print("Thank you for learning Python basics!")

print("\n" + "="*60)
print("CONGRATULATIONS! You just learned all Python basics!")
print("Keep coding every day!")
print("="*60)