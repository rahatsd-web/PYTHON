# WAP to input user,s first name & print its length
name = str(input("Enter the name :"))
print("Length of te name is :" , len(name))


# WAP to fid the occurrence of '$' in a string
example = str (input ("Enter a string with '$': " ) )
print ("The occurrence of '$' in the string is: ", example.find('$'))

print ("The occurrence of '$' in the string is: ", example.count('$'))


# WAP to check if a number entered by the user is odd or even.
number = int(input("Enter the number: "))
if (number % 2 == 0):
    print("Number is Even")
else:
    print("Number os Odd")   
           # OR
number = int(input("Enter the number: "))
rem = num % 2
if (rem == 0):
     print("Number is Even")
else:
    print("Number os Odd")      


# WAP to find the greatest of 3 numbers entered by the user
a = int (input("Enter the first number :"))
b = int (input("Enter the second number :"))
c = int (input("Enter the third number :"))
if (a>b and a>c):
    print("Greatest number is a")
elif (b>c):
    print("Greatest number is b")    
else:
    print("Greatest number is c") 


# WAP to check if a number is a multiple of 7 or not
value = int (input("Enter the number :"))
if (value % 7 == 0):
    print("multiple of 7")
else:
    print("not multiple of 7")    