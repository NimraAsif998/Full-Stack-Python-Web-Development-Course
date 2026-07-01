


# Python Complete Notes (Basics)

---

# 1. Variables

A variable is a name that refers to a value stored in memory. Python is **dynamically typed**, so you don't declare a type — it's inferred automatically.

```python
name = "Ali"
age = 25
gpa = 3.8
```

### Naming Rules
- Must start with a letter or underscore `_` (not a number)
- Can only contain letters, numbers, and underscores
- Case-sensitive (`Age` and `age` are different)
- Cannot use reserved keywords (`if`, `for`, `class`, etc.)

### Multiple Assignment

```python
a, b, c = 1, 2, 3
x = y = z = 0

# Swapping values (Python trick)
a, b = 5, 10
a, b = b, a
print(a, b)   # 10 5
```

---

# 2. Data Types

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `10`, `-5` |
| `float` | Decimal number | `3.14` |
| `complex` | Complex number | `2 + 3j` |
| `str` | Text | `"Hello"` |
| `bool` | True/False | `True` |
| `NoneType` | Represents "no value" | `None` |
| `list` | Ordered, mutable collection | `[1, 2, 3]` |
| `tuple` | Ordered, immutable collection | `(1, 2, 3)` |
| `dict` | Key-value pairs | `{"a": 1}` |
| `set` | Unordered, unique values | `{1, 2, 3}` |

### Type Checking & Type Casting

```python
x = 10
print(type(x))          # <class 'int'>

a = int("25")             # string -> int
b = float("3.14")         # string -> float
c = str(100)                # int -> string
d = list("abc")             # string -> list -> ['a','b','c']
e = bool(0)                 # False
f = bool(1)                 # True
```

---

# 3. Operators

### Arithmetic

```python
a, b = 10, 3
print(a + b)    # Addition       -> 13
print(a - b)    # Subtraction    -> 7
print(a * b)    # Multiplication -> 30
print(a / b)    # Division       -> 3.33
print(a // b)   # Floor Division -> 3
print(a % b)    # Modulus        -> 1
print(a ** b)   # Power          -> 1000
```

### Comparison

```python
print(a == b)   # equal to
print(a != b)   # not equal to
print(a > b)    # greater than
print(a < b)    # less than
print(a >= b)   # greater than or equal
print(a <= b)   # less than or equal
```

### Logical

```python
x, y = True, False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False
```

### Assignment

```python
a = 10
a += 5    # a = a + 5
a -= 3
a *= 2
a /= 2
a //= 2
a %= 3
a **= 2
```

### Membership

```python
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)        # True
print("orange" not in fruits)    # True
```

### Identity

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)    # True  - same object
print(a is b)    # False - different objects
print(a == b)    # True  - same value
```

### Bitwise

```python
a, b = 5, 3
print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift
```

---

# 4. Control Flow (All Types)

```python
# Simple if
age = 20
if age >= 18:
    print("Adult")

# if-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else
marks = 75
if marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
elif marks >= 50:
    print("C grade")
else:
    print("Fail")

# Nested if
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Bring your ID")

# Ternary operator (one-line if-else)
status = "Adult" if age >= 18 else "Minor"

# match-case (Python 3.10+, like switch)
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
```

---

# 5. Loops (All Types)

```python
# For loop
for i in range(5):              # 0 to 4
    print(i)

for i in range(2, 10, 2):        # start, stop, step
    print(i)                     # 2,4,6,8

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Nested loop
for i in range(3):
    for j in range(3):
        print(i, j)

# break - stops loop entirely
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - skips current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass - placeholder, does nothing
for i in range(5):
    if i == 2:
        pass
    print(i)

# else with loop - runs if loop completes without break
for i in range(5):
    print(i)
else:
    print("Loop completed without break")

# Comprehensions
squares = [x**2 for x in range(5)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
squares_dict = {x: x**2 for x in range(5)}
squares_set = {x**2 for x in range(5)}
```

---

# 6. Data Structures

## List (mutable, ordered, duplicates allowed)

```python
fruits = ["apple", "banana", "mango"]

fruits.append("orange")        # add to end
fruits.insert(1, "grape")       # add at specific position
fruits.remove("banana")          # remove by value
fruits.pop()                      # remove last item
fruits.pop(0)                     # remove by index
fruits.sort()                     # sort the list
fruits.reverse()                  # reverse the list
print(len(fruits))                # length
print(fruits[0])                  # indexing
print(fruits[0:2])                # slicing
print(fruits.count("apple"))      # count occurrences
fruits.clear()                     # empty the list
```

## Tuple (immutable, ordered, duplicates allowed)

```python
coords = (10, 20, 30)

print(coords[0])           # access element
print(coords.count(10))    # count
print(coords.index(20))    # find index

# coords[0] = 100   # ERROR - tuples cannot be changed

# Tuple unpacking
x, y, z = coords
```

## Dictionary (key-value pairs, ordered since Python 3.7+)

```python
student = {"name": "Ali", "age": 20, "city": "Lahore"}

print(student["name"])              # get value
student["age"] = 21                  # update value
student["grade"] = "A"               # add new key
del student["city"]                  # remove key

print(student.keys())                 # all keys
print(student.values())               # all values
print(student.items())                # key-value pairs

for key, value in student.items():
    print(key, ":", value)

student.get("name")                   # safe way to get value
student.update({"age": 22})           # update multiple values
```

## Set (unique values, unordered)

```python
numbers = {1, 2, 3, 3, 2}   # duplicates removed automatically
print(numbers)                # {1, 2, 3}

numbers.add(4)
numbers.remove(1)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))          # {1,2,3,4}
print(set1.intersection(set2))    # {2,3}
print(set1.difference(set2))       # {1}
```

## String (immutable text)

```python
text = "Hello Pakistan"

print(text.upper())            # HELLO PAKISTAN
print(text.lower())            # hello pakistan
print(text.replace("Hello", "Hi"))
print(text.split(" "))          # ['Hello', 'Pakistan']
print(text.strip())              # removes extra spaces
print(len(text))                  # length
print(text[0:5])                  # slicing -> "Hello"
print(text[::-1])                 # reverse the string
print(text.find("Pak"))           # find index
print("Pak" in text)               # membership check

# f-strings (best way to format)
name, age = "Ali", 20
print(f"My name is {name} and I am {age} years old")
```

---

# 7. Input & Output

### Output — `print()`

```python
print("Hello Pakistan")
print("My name is", "Ali")               # multiple values
print("Ali", "Sara", sep=" - ")           # sep = separator
print("Hello", end=" ")                    # end = what to print at the end
print("World")                             # output: Hello World

name, age = "Ahmed", 22
print(f"Name: {name}, Age: {age}")         # f-string (recommended)
print("Name: {}, Age: {}".format(name, age))  # .format() method
print("Name: %s, Age: %d" % (name, age))    # % operator (old style)
```

### Input — `input()`

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

**Important:** `input()` always returns a **string**. Convert it if you need a number.

```python
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# Multiple inputs in one line
name, age = input("Enter name and age (space separated): ").split()

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)
```

---

# 8. Comments

```python
# This is a single-line comment
name = "Ali"   # comments can go after code too

# Multi-line comment (Python has no true multi-line comment,
# so multiple # lines are used)

"""
This looks like a multi-line comment
but is technically a string
"""

def add(a, b):
    """
    This function adds two numbers
    and returns the result
    """
    return a + b

print(add.__doc__)   # prints the docstring
```

**Good practice:** Comments should explain **why**, not just **what** — the code already shows what it does.

---

# 9. Functions (All Types)

```python
# Simple function
def greet():
    print("Hello!")
greet()

# Function with parameters
def greet(name):
    print(f"Hello, {name}")
greet("Ahmed")

# Function with return value
def add(a, b):
    return a + b
result = add(5, 10)

# Default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
greet("Ali")
greet("Ali", "Hi")

# Keyword arguments
def student_info(name, age):
    print(f"{name} is {age} years old")
student_info(age=20, name="Sara")   # order doesn't matter

# *args - variable number of positional arguments
def total(*numbers):
    return sum(numbers)
print(total(1, 2, 3, 4))

# **kwargs - variable number of keyword arguments
def student_details(**info):
    for key, value in info.items():
        print(key, ":", value)
student_details(name="Ali", age=20, city="Lahore")

# Lambda function (anonymous, one-line)
square = lambda x: x ** 2
add = lambda a, b: a + b

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Nested function
def outer():
    def inner():
        print("Inner function")
    inner()

# Generator function (uses yield, saves memory)
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(5):
    print(num)

# Variable scope
x = 10   # global
def test():
    x = 5   # local
    print(x)
test()
print(x)   # still 10

def change_global():
    global x
    x = 100
change_global()
print(x)   # 100
```

---

# 10. Modules

A module is a `.py` file containing functions, classes, or variables that you can **import** into your program to reuse code.

```python
import math
print(math.sqrt(16))       # 4.0
print(math.pi)               # 3.14159...

from math import sqrt, pi    # import specific things
print(sqrt(25))

from math import *            # import everything (not recommended)

import numpy as np           # import with alias
import pandas as pd
```

### Common Built-in Modules

| Module | Purpose |
|---|---|
| `math` | Mathematical functions |
| `random` | Random number generation |
| `datetime` | Working with dates and times |
| `os` | Interacting with the operating system |
| `sys` | System-specific functions |
| `time` | Delays, timestamps |
| `json` | Reading/writing JSON data |
| `re` | Regular expressions |
| `statistics` | Statistical functions (mean, median) |
| `collections` | Special container data types |

```python
import random
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))

import datetime
print(datetime.datetime.now())
```

### Creating Your Own Module

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"
```

```python
# main.py
import mymodule
print(mymodule.greet("Ali"))
```

### Installing External Packages — pip

```
pip install numpy
pip install pandas
pip install requests
```

### 🔗 Links to Explore ALL Python Modules

- **Official Python Docs (complete list of every built-in module):** https://docs.python.org/3/library/index.html
- **PyPI — Python Package Index (300,000+ third-party packages):** https://pypi.org/
- **Real Python — Module & Package tutorials:** https://realpython.com/tutorials/modules/
- **W3Schools — Python Modules (beginner-friendly guide):** https://www.w3schools.com/python/python_modules.asp
- **Awesome Python — curated list of popular libraries by category:** https://github.com/vinta/awesome-python

---

# 11. Error Handling

### Common Error Types

```python
print(10 / 0)                # ZeroDivisionError
int("hello")                  # ValueError
"5" + 5                        # TypeError
print(undefined_var)           # NameError
[1, 2, 3][10]                   # IndexError
{"a": 1}["b"]                    # KeyError
```

### Basic try-except

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except:
    print("Something went wrong!")
```

### Handling Specific Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
```

### Multiple Exceptions Together

```python
try:
    x = int(input("Number: "))
    print(10 / x)
except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred: {e}")
```

### try-except-else

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered {number}, no errors occurred")  # runs only if no exception
```

### try-except-finally

`finally` always runs, whether an error occurs or not — useful for cleanup (closing files, connections).

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs")
```

### Custom Exceptions

```python
class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")
    print(f"Valid age: {age}")

try:
    check_age(-5)
except AgeError as e:
    print(f"Custom Error: {e}")
```

### `raise` — manually triggering an error

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)
```

---

# 📌 Practice Exercises

1. Create 5 variables with different data types and print each type.
2. Write a program to check if a number is odd or even using if-else.
3. Use a `for` loop to find the sum of all even numbers from 1 to 100.
4. Create a list of 5 fruits, remove one, and add a new one.
5. Create a dictionary with 3 students' names and their marks.
6. Write a function using `*args` that calculates the average of any number of values.
7. Write a recursive function that prints the Fibonacci series up to a given number.
8. Use set operations to find the union and intersection of two sets.
9. Take user input for two numbers and use `try-except` to handle division safely.
10. Create your own module with two functions (`add()` and `subtract()`) and import it in another file.
11. Create a custom exception that checks if marks are between 0-100.

---

*Written by : Nimra Asif*
