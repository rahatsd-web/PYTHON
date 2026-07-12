# STRING

#An escape sequence character in Python is a special character combination that starts with a backslash (\). It is used to represent characters that are difficult or impossible to type directly inside a string.

str1 = "Hello\nWorld" # \n is used to print in new line
print(str1)

str1 = "Hello\tWorld" # \t is used to add a tab space in the string
print(str1)


# Different operation s on string in Python 1. Concatenation of string 2. Lenth of str 3. Repetition of string 4. Slicing of string 5. String formatting 

# 1. Concatenation of string
str1 = "CSE"
str2 = "Course"
str3 = str1 + " " + str2
print(str3)
                        
str1 = "My name is "
str2 = "MRA"
print(str1 + str2)

#2. Length of string
str1 = "Hello World"
print(len(str1))

str2 = " My name is MRA"
len1 = (len(str2))
print(len1) 

#Concatenation + Length
final_str = str1 + " " +str2
print(final_str)
print(len(final_str))

## INDEXING

str = "Hello World"
ch = str[2] # Indexing starts from 0
print(ch)

str = "Hello World" # Direct indexing
print(str[6])


# SLICING
str = "Hello World"
print(str[2:5]) # Slicing from index 2 to 4
print(str[:5])  # Slicing from beginning to index 4
print(str[2:])  # Slicing from index 2 to the ends
# Slicing with negative indexing     {{ W O R L D}}
#                                   {{-5 -4 -3 -2 -1}}

print(str[-5:-2])  # Slicing from index -5 to -3
print(str[-5:])    # Slicing from index -5 to the end
print(str[:-2])    # Slicing from beginning to index -2


## String Functions::
str ="I am learning python from Home"
print(str.endswith("me")) # Check if the string ends with "me"

str ="i am learning python from Home"
print(str.capitalize()) # Capitalize the first letter of the string. It capitaise only ones not in main string
print (str)

str ="I am learning python from Home"
print(str.replace("learning", "teaching")) # Replace "learning" with "teaching" in the string

str ="I am learning python from Home"
print(str.find("o")) # Find the index of "o" in the string -- actual valu is o 1st INDEX

str ="I am learning python from Home"
print(str.count("o")) # Count the number of occurrences of "o" in the string


## CONDITIONAL STATEMENTS << IF, ELIF, ELSE >> syntax
## 4____space gap before print is called INDENTATION.
age  = 17
if age>= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")    

# if checks the first condition. & if the first condition is false then it checks the second condition else. & if both conditions are false then it executes the else statement. The 'else' statement can be written only once.
Traffic_Light = "black"
if (Traffic_Light == "Green"):
    print("You can go")
elif (Traffic_Light == "Yellow"):
    print("You should wait")
elif (Traffic_Light == "Red"):   
    print("You should Stop") 
else:
    print("traffic light er khamba nai")    

# Example
marks = int(input("Enter the mark :"))
if (marks >= 95):
    print("Grade A+")
elif (marks >= 85):
    print("Grade A")
elif (marks >= 75):
    print("Grade B")    
elif (marks >= 65):
    print("Grade C")
elif (marks >= 55 and marks < 65):
    print("Grade D")  
else :
    print ("U R Fail in life")        


## NESTING -----Nesting means placing one statement or structure inside another. For example, an if statement can be placed inside another if statement. This is called a nested if statement.
age = 60
if (age >= 18):
    if (age >= 80):
        print("Can't Drive")
    print("Can Drive")
else:
    print("Can't Drive")    

