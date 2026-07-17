# FUNCTION --- Bolck of statement that perform a specific task.

def coun_sum(a, b):
    sum = a + b
    print(sum)
    return sum

coun_sum( 10, 5)

coun_sum( 10, 20) 

coun_sum( 10, 15)

      # OR

# Function Defination
def num_sum(a ,b): # Perameters
    return a + b
sum = num_sum(25, 25) # Function call: arguments
print(sum)


def stu_infor(): # No perameter , No return value
    print("Name")

stu_infor()
stu_infor()    

# average of 3 number

def cal_val(a, b, c):
    average = (a+b+c)/3
    print(average)
    return average

cal_val(1, 2, 3)
# BOTH ARE SAME
def cal_val(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

cal_val(1, 2, 3)



# Built in function <<< print, len, type, range >>>
print ("My name is") #SEP = " space "
print ("What is your nmae") #END = \n

print ("My name is", end =" ")
print("MRA")

# Default perameters --- assigning a default value to perameter, which is used when no argument is passed
def coun_pro(a, b=2): # (a, b=2) possible but (a=2, b) not possible
    print(a * b)
    return a * b

coun_pro(1)


## RECURSION --- when a function calls itself repeatedly (( LOOPS & RECURSION are interrelated))

def show(n):
    if(n == -1): # BASE case
        return   # Recursion function
    print(n)
    show(n - 1)
show(5)


# ********<<CALL-STACK>>******** --- (LIFO) The call stack is a mechanism Python uses to keep track of function calls and their execution order.
def show(n):
    if(n == 0): # BASE case
        return   # Recursion function
    print(n)
    show(n - 1)
    print("End")
show(3)

## RECURSION ******** V V I P
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print (fact (4))