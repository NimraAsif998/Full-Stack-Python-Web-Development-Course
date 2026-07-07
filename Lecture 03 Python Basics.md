# 🐍 Python Basics variables,datatypes, comments input and output , typecasting

---

# 📘 What is Python?

Python is a **high-level, easy-to-read, and beginner-friendly programming language**. It is widely used in:

* 🌐 Web Development
* 🤖 Artificial Intelligence (AI)
* 📊 Data Science
* 🔐 Cyber Security
* 🎮 Game Development
* ⚙️ Automation

### Why Learn Python?

* Easy Syntax
* Less Code
* Beginner Friendly
* Huge Community
* Cross Platform (Windows, Linux, Mac)

---

#  Variables

A **variable** is a container used to store data.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Ali"
age = 20
cgpa = 3.8

print(name)
print(age)
print(cgpa)
```

### Output

```
Ali
20
3.8
```

---

## Variable Naming Rules

✅ Can contain letters, numbers and underscore (_)

```python
student_name
age1
total_marks
```

❌ Cannot start with a number

```python
1name
```

❌ No spaces

```python
student name
```

❌ Cannot use Python keywords

```python
class
if
for
```

---

# 📘 Data Types

A data type tells Python what kind of data is stored.

| Data Type | Example      |
| --------- | ------------ |
| int       | 10           |
| float     | 3.14         |
| str       | "Hello"      |
| bool      | True / False |

---

## Integer (int)

Whole numbers

```python
age = 21
marks = 500

print(age)
```

---

## Float

Decimal numbers

```python
price = 99.99
cgpa = 3.75

print(price)
```

---

## String

Text written inside quotes.

```python
name = "Nimra"

print(name)
```

---

## Boolean

Only two values.

```python
is_student = True
is_logged_in = False

print(is_student)
```

---

# Finding Data Type

```python
age = 20
print(type(age))

name = "Ali"
print(type(name))
```

Output

```
<class 'int'>
<class 'str'>
```

---

# 🖥️ Input & Output

## Output

Use **print()** to display information.

```python
print("Hello Students!")
```

Output

```
Hello Students!
```

---

## Input

Use **input()** to take input from the user.

```python
name = input("Enter your name: ")

print(name)
```

Output

```
Enter your name: Ali
Ali
```

---

## Example 2

```python
city = input("Enter your city: ")

print("Your city is", city)
```

Output

```
Enter your city: Lahore
Your city is Lahore
```

---

# 💬 Comments

Comments are notes written for humans. Python ignores them during execution.

---

## Single Line Comment

```python
# This is a comment

print("Hello")
```

---

## Multi-line Comment

```python
"""
This is
a multi-line
comment
"""

print("Python")
```

---

# 🔄 Type Casting

Type casting means converting one data type into another.

---

## Integer to Float

```python
num = 10

result = float(num)

print(result)
```

Output

```
10.0
```

---

## Float to Integer

```python
num = 7.9

print(int(num))
```

Output

```
7
```

---

## Integer to String

```python
age = 20

print(str(age))
```

Output

```
20
```

---

## String to Integer

```python
num = "50"

print(int(num))
```

Output

```
50
```

---

# ⭐ Why Type Casting is Important?

Suppose the user enters two numbers.

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
```

Input

```
10
20
```

Output

```
1020
```

Because **input() always returns a string**.

Correct way:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Output

```
30
```

---

# 📌 Mini Practice Examples

### Example 1

```python
name = input("Enter your name: ")
print("Welcome", name)
```

---

### Example 2

```python
age = int(input("Enter your age: "))

print("Your age is", age)
```

---

### Example 3

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)
```

---

# 📝 Practice Questions

## Easy Level 

### Q1

Create a variable called **name** and print it.

---

### Q2

Create variables:

* Name
* Age
* City

Print all three.

---

### Q3

Store your CGPA in a variable and print its data type.

---

### Q4

Take your name as input and display:

```
Hello, Nimra!
```

---

### Q5

Take your favourite subject as input and print it.

---

## Medium Level 

### Q6

Take two numbers from the user and print their sum.

**Example**

Input

```
10
20
```

Output

```
30
```

---

### Q7

Take length and width from the user and calculate the area of a rectangle.

Formula:

```
Area = Length × Width
```

---

### Q8

Take your birth year as input and calculate your age.

*(Hint: Use the current year.)*

---

### Q9

Convert:

```
45
```

into:

* float
* string

and print both.

---

### Q10

Write a program that prints:

```
Name: Ali
Age: 20
City: Lahore
```

using variables.

---

# 🎯 Challenge Questions

### Q11

Take three numbers from the user and print their average.

---

### Q12

Take a student's name and marks as input and display:

```
Student: Ali
Marks: 89
```

---

### Q13

Ask the user for their first name and last name, then print their full name.

**Example**

```
Enter First Name: Ali
Enter Last Name: Khan

Full Name: Ali Khan
```

---

### Q14

Ask the user to enter a temperature in Celsius and convert it to Fahrenheit.

**Formula:**

```
F = (C × 9/5) + 32
```

---



