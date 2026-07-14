# DICTIONARY  -- are used to store data values in key:value pairs, they are unordered, mutable(changeable) & don't allow duplicate keys

info = {
    "name" : "mra",
    "subjects" : ["python", "c", "java", "html"], # List
    "topics" : ("dictionary", "set"), # Tuples
    "age" : 22,
    "is_adult" : True,
    "12.99" : 99.0
}

print (info)
print (info["name"])
print (info["topics"])
print (info["12.99"])

info ["name"] = "Rahat ahmed" # for change the name value
print(info)

info ["surname"] = "BMW"  # for adding new value
print(info)


# Empty dictionary
null_dict = {}
print(null_dict)

null_dict = {}  # insert value inside null-dict
null_dict['name'] = "maserati"
print(null_dict)


## NASTED Dictionary.....
student = {
    "name" : "Mahin",
    "subjects" : {
        "phy" : 90,
        "che" : 88,
        "bio" : 97,
        "mat" : 89
    },
    "roll" : 69,
    "gpa" : 5.00
}

print(student)
print(student ["subjects"]) # only nasted ictionary
print(student ["subjects"] ["che"]) # nasted dictionary indivetual data


## Dictionary METHODS << keys, values, items, get, update >>

brand = {
    "BMW" : "M8",
    "Audi" : "Q7",
    "Maserati" : "Ghibli",
    "Toyota" : "camry"
}

print(brand.keys())  # returns all keys
print(brand.values()) #  returns all values
print(brand.items()) # return all (key, value) pairs as tuples
print(brand.get("BMW")) # return the key according to vaalue .<.<. method gives no ERROR it gives [[NULL]]
#print(brand("BMW")) # <<<< It gives ERROR
brand.update({"Nissan" : "GTR-35"}) 
print(brand) # inserts the specified items to the dictionry

new_brand = {"Renalt" : "Duster", "Porshe" : "911"}
brand.update(new_brand) # pass to new Dictionary
print(brand)


print(len(list(brand.keys()))) # convert dictionary to list & it's lenth

print(list(brand.items())) # Tuple inside List
pairs = list(brand.items()) # Indivitual tuple
print(pairs[2])
 

# SET in python --- set is the collection of the unordered items. Each item of the set must be unique & immutable
# set > mutable, st > element > immutable
collection = {2, 3, 4, 7, "hello world", "mra"}
print(collection)
print(type(collection))

collection1 = {2, 3, 2, 7, 2, "hello world", "mra", "hello world"}
print(collection1) # SET ignores duplicate values
print(len(collection1)) # totalnumbers of items except duplicate

collection1 = set() # empty dictionary sytex
print(type(collection1)) 


## SET Methods << add, remove, clear, pop, union, interseption >>
collection1 = set() 
collection1.add(1)
collection1.add(2)
collection1.add(3)
collection1.add(2)
print(collection1)  # add an elements
print(len(collection1))

collection1.remove(2)
print(collection1) # remove the  elemant

collection1.clear()
print(collection1) # empties the set

collection1 = {"wow", "nice", "mra", "hello world"}
print(collection1.pop()) # removes a random valu

# UNION & INTERSECTION
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1)
print(set2)
print(set1.union(set2)) # 1, 2, 3, 4
print(set1.intersection(set2)) # 2, 3

