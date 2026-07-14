# LIST  -- A built-in data type that stores set of values {{int, float, str etc}}


# Mutable Objects - A mutable object can be modified after creation. Lists are mutable.

marks = [94.0, 87.0, 99.7, 95.7, 45.8]
print (marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])
marks[0] = 80.0
print(marks)   


student = ['Rahat', 5.00, 'Dhaka', 23]  # Mutable
print(student)
student[0] = "Ahmed"
print(student)

# List - Slicing < similar to string slicing>
marks = [94.0, 87.0, 99.7, 95.7, 45.8]
print(marks[1:4])
print(marks[-3:])


## List - METHODS [append, sort, reverse, insert,  remome, pop]

list = [4, 5, 7, 9]
list.append(10)
print(list)

list = [5, 9, 7, 4]
print(list.append(10))
print(list.sort())
print(list)

list = [5, 9, 7, 4]
print(list.append(10))
print(list.sort(reverse = True))
print(list)

list = ["mango", "apple", "litchi", "banana"]
print(list.sort(reverse = True))
print(list) # Descending order 

list = ["mango", "apple", "litchi", "banana"]
print(list.sort())
print(list) #  Ascending order

list = ["n", "k", "a", "y", "b"]
print(list.reverse())
print(list)

list = [5, 9, 7, 4]
list.insert (1, 3)
print(list)

list = [5, 9, 7, 4]
list.remove(9)
print(list)

list = [5, 9, 7, 4]
list.pop (1)
print(list)


# TUPLES  -- a built-in data type that lets us create IMMUTABLE sequence of value.

tup = (0, 2, 4, 6, 8)
print(type(tup))
print(tup[0])
print(tup[3])

tup = (2,)
print(tup) # must add a trailing comma <,> in single value Tuple

tup = (2)
print(tup) # count as int
print(type(tup))


# TUPLE Slicing
tup = (0, 2, 4, 6, 8)
print(tup[1:4])

# TUPlE Methods { INDEX, COUNT}
tup = (0, 2, 4, 6, 8)
print(tup.index(6))

tup = (0, 1, 4, 5, 0, 9, 5)
print(tup.count(9)) 