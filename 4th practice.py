## store following word meaning in a python dictionary:
data = {
    "table" : "a peace of furmiture", 
    "cat" : "a small animal",
    "car" : ["is fast", "so expensive"],
    "pc" : ("is good", "solve problems")
}

print(data)
print(type(data))
print(type(data["car"]))
print(type(data["pc"]))


# U R given a list of subjects for students. assume one classrooom is required for 1 subject. How many classroom are needed by all students
subjects ={
    "python", "java", "c++", "python", "javascript","java",
    "python", "java", "c++", "c"
}
print(subjects)
print(len(subjects))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Strat with an empty dictionary & add. use subject name as key & mark as value
result ={}
print(result)
che = int(input("Enter the value :")) 
phy = int(input("Enter the value :")) 
bio = int(input("Enter the value :")) 
result.update({"che" : che})
result.update({"phy" : phy})
result.update({"bio" : bio})
print(result)
print(type(result))

# EXTRA
marks ={}
ban = int (input("Enter ban:"))
marks.update({"ban" : ban})
eng= int (input("Enter ban:"))
marks.update({"eng" : eng })
mat = int (input("Enter ban:"))
marks.update({"mat" : mat })
che = int (input("Enter ban:"))
marks.update({"che" : che })

print("Indivitual mark is", marks)
print (type(marks))


# Figure out a way to store 9 & 9.0 as seperate values in the set. 
values = {9, "9.0"}
print(values)
print(type(values))

# OR
value1 = ("int", 7)
value2 = ("float", 7.0)
value = {value1, value2}
print(value)
print(type(value))

#or

value ={
     ("int", 2), ("float", 2.0)
}
print(value)
print(type(value))
