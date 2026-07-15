# WAP to print numbers 1 to 100
num = 1
while num <= 100:
    print(num)
    num = num + 1
print ("Loop end")    


# # WAP to print numbers 100 to 1
num = 100
while num >= 1:
    print(num)
    num = num - 1
print ("Loop end")    


# Print the multiplication table of number n. 
i = 1
n = 3
#n = int(input("Enter the number: "))
while i <= 10:
    print(i * n)
    i = i + 1
print ("End of 3 Multiplication")    


# Print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
idx = 0 # TRAVERSE
while idx < len(list):
    print(list[idx])
    idx += 1
    
    # OR
    
# ["apple", "banana", "mango", "orange"]
fruits = ["apple", "banana", "mango", "orange"]
idx = 0 
while idx < len(fruits):
    print(fruits[idx])
    idx = idx + 1
print ('Count End')    


# search for a number x in this tuple using loop (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25)
x = int(input("enter the number : "))
idx = 0 # INITIALIZATION
while idx < len(num):
    if (num[idx] == x):
        print("Found at index", idx)
    else:
        print("Not found")    
    idx = idx + 1

    # OR

# nums = (1, 8, 27, 64, 125, 216, 343)
nums = (1, 8, 27, 64, 125, 216, 343)
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx = idx + 1

# For X value
nums = (1, 8, 27, 64, 125, 216, 343)
x = int (input (" Enter the vaule : "))
idx = 0
while idx < len(nums):
    if (nums[idx] == x ):
        print("Positive", idx)
    else:
        print("Negative")   
    idx = idx + 1 


        ## FOR lop question
         
# Print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]       
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in num:
    print(i)


# search for a number x in this tuple using loop (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int (input("Enter the valure: "))
idx = 0
for i in num:
    if (i == x):
        print("Value found at index :", idx)
    idx = idx + 1


# print numbers from 1 to 100
for i in range(1, 101):
    print(i)


# print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)     
 

# print the multiplication table of a number n 
n = 3   
for i in range (1, 11):
    print( i * n)


# WAp to find the sum of first n numbers # PROBLEM

num = int(input ("Enter the number :")) # Error
sum = 0
for i in range(1, num + 1):
    sum = sum + i
    print("total sum is:", sum)
# or

n = 5
sum = 0
for i in range(1, n+1):
    sum += i
    print(sum)

# while
n = 6
sum = 0     
i = 1
while i <= n:
    sum += i
    i += 1
print (sum)  

# WAP to find the factorial of first n numbers
n = 5
fact = 1   
i = 1
while i <= n:
    fact *= i
    i += 1
print (fact)  

n = 5
fact = 1   

for i in range(1, n+1):
    fact *= i
    
print (fact)  