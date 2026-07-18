# operators => operation perform karna 
"""
types => arith,logical,comp,identity,membership so on....

"""
# airithmatic
"""num1=3
num2=5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
# 2 ^ 4 ans => ?
print(num1**2) # 3^2
print(num2**2)
print(num1**num2) # num1^num2 => 3^5

# floor => // => only bara value lye aiya ga matlab agr float mai ans ha to us ka decimal ky baad wala number ni aiye ga
print(num1//7)  # 3//7 # 0
print(num1/7) # 0.kuch bhi

"""

# comparison => compare two values
# 3==5 => ni han => False
"""

print(3==5)
print(3 !=5)
print(3>5)
print(3<5)
print(5>=5)
print(5<=5)
"""

# logical operators
# and , or => two input par kam karty han
# ! => ak input par kam karta a 
# and=> agr ak bhi input false han to result false aiye ga
# or=> agr ak bhi input True ha to result bhi True aoye ga
# !=> ulta kar do => agr input ha => True to result hoga False, agr input han False to result aiya ga True
"""

a=4
b=3
print(a>b and a<b)
print(a>b or a<b)
print(not a>b)
"""

# identity operators => kiya two variables ak hi cheez ko point karty han 
# is => han karty han
# is not => ni karty han
"""

a=2
b=3
print(a is b)
print(a is not b)
"""

# membership operators => kiya value wo str,list,tuple,set,dict mai ha ya nai
# in => han ha
# not in => ni ha
"""

name="liza"
print("l" in name)
print("n"in name)
print("n" not in name)
"""

# bitwise operator
"""


x=3 #011
y=5 # 101
print(x & y) # 1
print(bin(x & y))  # 001
"""

"""

x=3 #011
y=5 # 101
print(x | y) # 1
print(bin(x | y))
"""


"""
x=3 # 011 -> 100
print(~ 3)
print(bin(~ 3))
"""

# question
"""

a=15
print(a)
b=4
print(a%b)
print(a//b)
print(a**b)
a +=10 #=> a=a+10=> 15+10=>25
print(a)
"""


"""

# assignment=> value assign karna ha 
x=3
# ky 3 ky andr 3 add ho
x +=3
print(x) #=> x=x+3 => 3+3=>6
x -=3
print(x)
x *=3
print(x)
x /=3
print(x)
x //=3
print(x)
x %=3
print(x)

"""

# mini task => build calculator
"""

num1=int(input("enter a first number:"))
num2=int(input("enter a 2nd number:"))

print("sum is ",num1+num2)
print("sub is ",num1-num2)
print("mul is ",num1*num2)
print("div is ",num1/num2)
print("floor is ",num1//num2)
print("mod is ",num1%num2)
"""

