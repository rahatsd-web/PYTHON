# Wriyte a program to input 2 numbers & print their sum.

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum = a + b
print ("Sum of a & b is", sum)


# Write a progrm to input of a square & print its areaS

area = int(input("Enter the side of square:"))
area = area * area
print ("Area of square is", area)


## Write a program o input 2 floating poit numbers & print their average

a = float(input("Enter 1st value:"))
b = float(input("Enter 2nd value:"))
average = (a + b)/2
print ("Average of a & b is:", average)


# Write a program to input 2 int numbers, a and b. print true if a is greater than or equal to b. if not print falseSSS

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if a>=b:
    print("True")
else:
    print("False")


    
### EXTRA ###
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number"))
if a>b and b>c:
    print("The value is big", True)
else: 
    print ("The value is small", False)    