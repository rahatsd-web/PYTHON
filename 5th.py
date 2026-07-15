# LOOPS --- loops are used to repeat instruction  << WHILE, FOR >>

# ......WHILE......
count = 0     #... Variable are known as ITERATOR  /// For run inside loop is called ITERATION
while count <= 6:
    print("Hello World")
    print("Hello World",count)  # .... CONDITION >> WORK >> UPDATION
    count = count + 1

print(count)    

# Print (1 - 5 / 5 - 1)
i = 1
while i <= 5:
    print(i)
    i +=1
print("Low to High")    
###
i = 5
while i >= 1:
    print(i)
    i -=1
print("High to Low")    

#i = 5 # Infinite looop
#while i < 6:
#    print(i)
#    i -= 1

## BREAk & CONTINUE

# Break -- used to terminate the loop when encountred
num = 1
while num <= 100:
    print(num)
    if (num == 55):
        break
    num = num + 1
print ("Loop end")    

 # or

 # For X value
nums = (1, 8, 27, 64, 125, 216, 27, 343)
x = 27
idx = 0
while idx < len(nums):
    if (nums[idx] == x ):
        print("Positive", idx)
        break
    else:
        print("Negative")   
    idx = idx + 1 
print("value end")

# Continue -- terminates executionin the current iteration & continues execution of the loop with the next iteration
i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue # acts as SKIP
    print(i)  # it ignore both of this statements
    i += 1
     
# or

i = 1
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue # for odd number
    print(i)  
    i += 1
     
i = 1
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue # for even number
    print(i)  
    i += 1



## --- FOR --- loops are used for sequential traversal. For traversing list, String, tuples etc

num = [1, 3, 5, 7, 9]
for x in num:
    print("FOR loop value is", x)

fruits = ["apple", "banana", "mango", "orange"]
for x in fruits:
    print(x)

str = "basabo"
for x in str:
    print(x)    


## RANGE ---- range() creates a sequence of numbers. It is commonly used with a for loop.

val = range(5)  # 1
for i in val:
    print(i)    # 1 & 2 both are same
                   
for i in range(6):  # 2
    print(i)


# Start, Stop, Step    
for i in range(6):  # range(stop)
    print(i)

for i in range(6, 10):  # range(start, stop)
    print(i)

for i in range(2, 10, 2):  # range(start, stop, step)
    print(i)


# EVEN & ODD 
for i in range(2, 100, 2):  # range(start, stop, step)
    print(i)

for i in range(1, 100, 2):  # range(start, stop, step)
    print(i)



# print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)      

# PASS Statement --- It is used as a placeholder when Python requires code, but you are not ready to write it yet.
for i in range(6):
    pass
print("usefull value")


