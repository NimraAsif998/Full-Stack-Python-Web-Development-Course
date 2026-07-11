# Random Password Generator

import random
import string

# Available characters
val = string.ascii_letters + string.digits + string.punctuation

# User se password ki length lena
num = int(input("Enter a number which you want password length: "))

# Password banana
password = ""
for i in range(num):
    password += random.choice(val)

print(password)
