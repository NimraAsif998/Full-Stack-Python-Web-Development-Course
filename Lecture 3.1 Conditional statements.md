# Lecture 3.1 — Python Conditional Statements

**Instructor:** Nimra Asif
**Role:** Software Engineer & Data Analyst

**Date:** July 7, 2026

---

# 🐍 Think of Python Like a Smart Robot

Imagine Python is a very obedient robot.

You give it instructions, and it follows them exactly. But sometimes the robot needs to make decisions based on different situations.

That's where **Conditional Statements** come in.

---

# 📌 What is a Conditional?

A **conditional statement** allows Python to make decisions by checking whether a condition is **True** or **False**.

For example:

* Is the student passed?
* Is the password correct?
* Is the user 18 or older?
* Is the account active?

Python mainly uses the **`if`** keyword to make these decisions.

---

# 1️⃣ if Statement

Use an **if statement** when you want Python to perform an action **only if a condition is True**.

## Syntax

```python
if condition:
    statement
```

## Example

```python
age = 20

if age >= 18:
    print("You can vote.")
```

### Output

```text
You can vote.
```

### Explanation

Python checks:

```python
20 >= 18
```

Since the condition is **True**, the message is displayed.

---

## When the Condition is False

```python
age = 15

if age >= 18:
    print("You can vote.")
```

### Output

```text
Nothing
```

Because the condition is **False**, Python skips the code inside the `if` block.

---

# 2️⃣ if-else Statement

Use **else** when you want Python to perform another action if the condition is **False**.

## Syntax

```python
if condition:
    statement
else:
    statement
```

## Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Output

```text
Minor
```

---

# 3️⃣ if-elif-else Statement

Use **elif** when there are multiple conditions to check.

## Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
```

### Output

```text
Grade C
```

### Explanation

Python checks conditions **from top to bottom** and stops as soon as it finds the first **True** condition.

---

# 📊 Comparison Operators

Comparison operators compare two values and return either **True** or **False**.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

## Example

```python
a = 10
b = 20

print(a == b)
```

### Output

```text
False
```

---

# 🔗 Logical Operators

Logical operators combine multiple conditions.

## 1. and

Both conditions must be **True**.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

### Output

```text
Eligible
```

---

## 2. or

At least one condition must be **True**.

```python
marks = 40
sports = True

if marks >= 50 or sports:
    print("Selected")
```

### Output

```text
Selected
```

---

## 3. not

Reverses the result of a condition.

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

### Output

```text
Please Login
```

---

# 📂 Nested if

A **Nested if** means placing one `if` statement inside another.

## Example

```python
age = 20
license = True

if age >= 18:
    if license:
        print("You can drive.")
```

### Output

```text
You can drive.
```

---

# ⚡ Short-hand if

```python
age = 20

if age >= 18: print("Adult")
```

---

# ⚡ Short-hand if-else

```python
age = 17

print("Adult") if age >= 18 else print("Minor")
```

---

# 💡 Truthy and Falsy Values

Python automatically treats certain values as **False**.

## Falsy Values

* `0`
* `False`
* `None`
* `""`
* `[]`
* `{}`
* `()`

Everything else is generally considered **Truthy**.

## Example

```python
name = ""

if name:
    print("Name entered")
else:
    print("No name")
```

### Output

```text
No name
```

---

# 📝 Today's Lecture Covers

* ✅ if Statement
* ✅ if-else Statement
* ✅ if-elif-else Statement
* ✅ Comparison Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
* ✅ Logical Operators (`and`, `or`, `not`)
* ✅ Nested if
* ✅ Short-hand if
* ✅ Short-hand if-else
* ✅ Truthy & Falsy Values

---

# 🎯 Practice Questions

### Question 1

Write a program to check whether a person is eligible to vote.

---

### Question 2

Take marks as input and print:

* A (90+)
* B (80–89)
* C (70–79)
* Fail (Below 70)

---

### Question 3

Take two numbers and print the greater number.

---

### Question 4

Check whether a number is even or odd.

---

### Question 5

Check whether a user can log in only if the username and password are correct.

---

# 📚 Next Lecture

In the next lecture, we'll explore **Python Functions** and learn how to write reusable, organized, and efficient code.
