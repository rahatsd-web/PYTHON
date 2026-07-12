# Basic print statement in Python


# String ---- In Python, a string must be enclosed in quotation marks.
print("Hi I am Rahat")
print("I am a Python learner")

print("Hi I am Rahat", "I am a Python learner")

# Number
print(5)
print(3.14)

print(5, 3.14)
print(39+31)

# Print number and string together
print("My age is", 20)


## VARIABLES --- A variable is a name given to a memory location in a program.
name = "Rahat"  # name = variable name, "Rahat" = value assigned to the variable
age = 20
print(name)
print(age)
 
age2 = age

print ("My name is", name, "and my age is", age)
print(age2)

# type() function is used to know the data type of a variable
age = 25
name = "Rahat"
old = True
a = None

print (type(name))  
print (type(age))
print (type(old))
print (type(a))

## KEYWORDS --- Keywords are reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier.
""" PYTHON is a case sensitive language. <<KEYWORDS>> For example, 
the variable name "age" and "Age" would be treated as two different variables."""  # SINGLE Line & MULTI Line comments in Python....

# OPERATORS
# Arithmetic operators {+,-,*,/,%,**,//} in Python
a = 100
b = 20
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a % b) # Remainder
print (a ** b) # Power operators
print (a // b) # Floor division

a = 15
b = 5
sum = a + b
print ("Sum of a & b is", sum)


# Comparison or Relation operators {==, !=, >, <, >=, <=} in Python
a = 50
b = 20
print (a == b) # False
print (a != b) # True
print (a > b) # True
print (a < b) # False
print (a >= b) # True
print (a <= b) # False


# Assignment operators {=, +=, -=, *=, /=, %=, **=, //=} in Python
a = 10
a = a + 10
# a += 10 & a = a + 10  Both are same 

num = 10
num = num + 10 # num = 10 + 10
print ("num :" ,num)


# Logical operators {and, or, not} in Python
a = True
b = False
print (a and b) # False
print (a or b) # True
print (not a) # False

a = 50 # with expression
b = 20
print (a > 30 and b < 30) # True
print (a > 30 or b < 30) # True


# TYPE Conversion --- Type conversion is the process of converting the data type of a value to another data type.
a = 2
b = 4.25

sum = a + b # 2.0 + 4.25 = 6.25
print (sum)

a = int("2")
b = 4.25

print (type(a))
print (a + b)


## INPUT in  Python --- The input() function is used to take input from the user. The input() function always returns a string value.

#name = str(input("Enter your name: "))
#age = int(input("Enter your age: ")) 
#print ("My name is", name, "and my age is", age)

#val = input ("enter some value:")
#print  (type(val))

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
print ("My name is:", name, "and my age is:", age, "and my marks are:", marks)