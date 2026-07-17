"""variables:
name memory location



datatypes:

int->integer
float->decimal number
str->string (collection of characters)
bool





"""

                                     #-----------#  variables

"""# string
name="david"
# int 
age=19
# float
cgpa=3.91
# boolen datatype
is_student=False
print(type(name))
print(type(age))
print(type(is_student))
print(type(cgpa))"""

# task
# print -> name,age,marks,passed , check -> type -> manulay

"""name="david"
age=26
cgpa=3.80
is_passed=True
# print information of student
print("my name is :",name)
print("my age is :",age)
print("my cgpa is :",cgpa)
print("i am passed :",is_passed)

# check types
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_passed))"""


# best practice -> clean code 

# task user input -> store student information
name = input("enter your name:")
age=int(input("enter your age:"))
cgpa=float(input("enter your cgpa:"))
is_passed=bool(input("enter your passed status:"))

print("my name is :",name)
print("my age is :",age)
print("my cgpa is :",cgpa)
print(" passed  status:",is_passed)


print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_passed))









