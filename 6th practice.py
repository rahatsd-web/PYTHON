# WAF tp print the length of a lis
marks = [94.0, 87.0, 99.7, 95.7, 45.8]
student = ['Rahat', 5.00, 'Dhaka', 23] 
def print_len(list):
    print(len(list))
  
print_len(marks)
print_len(student)


# Example::
fruit = ["mango", "apple", "litchi", "banana"]
car = ["bmw", "audi", "maserati", "toyota", "cherry", "renalt", "honda"]

def count_item(list):
    print(len(list))
count_item(fruit)
count_item(car) 


# WAF to print the element of a list in a single line
car = ["bmw", "audi", "maserati", "toyota", "cherry", "renalt", "honda"]
def car_name(list):
    print(len(list))

def car_name(list):
    for i in list:
        print(i, end=" ")

car_name(car) 
###
car = ["bmw", "audi", "maserati", "toyota", "cherry", "renalt", "honda"]
def car_name(list):
    print(len(list))
def car_name(list):
    for i in list:
        print(i, end = " ")
car_name(car)            


# WAF to find the factorial of n
def fact_num(n):
    fact = 1   
    for i in range(1, n+1):
        fact *= i
    print (fact)  

fact_num(5)


# WAF to convert USD to BDT
def exchange(usd_val):
    bdt_val = usd_val * 120
    print(usd_val,"USD =", bdt_val,"BDT")
exchange(100)
  

# WAF to input a number an check if it is even of odd
def num_val(n):
    if (n%2 == 0):
        print("number is even")
    else:
        print("number is odd")    
num_val(4)        

# WAF to input multipe number an check if it is even of odd
def num_val(numbers):
   for i in numbers:
       if (i % 2 == 0):
           print("Number is even")
       else:
           print("Number is odd")   
num_val([2,10, 40, 3, 45, 33, 86, 90])    


# WARF to calcuate the sum of first n natural number ******
def num_sum(n):
    if (n == 0):
        return 0
    return num_sum(n-1) + n
sum = num_sum(5)
print (sum) 


# WARF to print all elements in a list *******
def car_name(list, idx = 0):
    if (idx == len(list)):
        return
    print(list[idx])
    car_name(list, idx+1)
cars = ["bmw", "audi", "maserati", "toyota", "cherry", "renalt", "honda"]

car_name(cars)    