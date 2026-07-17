# File I / O --- Python can be used to perform operations o a file. (read & write data)

# (( Open, Read & Close File )) -- We have to open a file before reading or writing
# (( r, w, x, a, b, t, +)) frequently use

# Reading...
f = open("E:\Python Code\Codig\demo(r).txt","r")
data = f.read() # read entire file
print(data)
print (type(data))
f.close()


f = open("E:\Python Code\Codig\demo(r).txt","r")
data = f.read(12) # Number of charascter specify (The Importan)
print(data)
f.close()


f = open("E:\Python Code\Codig\demo(r).txt","r")
line1 = f.readline() # read one line at a time
print(line1)
line4 = f.readline()
print(line4)
line50 = f.readline() # Create empty next line when there is no more text in text file
print(line50)
f.close()

# Writing...  (W)-Over write, (a)-add at the end
f = open("E:\Python Code\Codig\demo(w).txt", "w")
f.write("My name is Rahat Ahmed, I am 20 years old, I am a student 9800")

f.close()

f = open("E:\Python Code\Codig\demo(w).txt", "a")
f.write(" \nI move to nodeJS")

f.close()

# f = open(demo.txt", "w" / "a") It create the file autometicaly which is not exist


# Reading & Writing (( r+ w+ a+))
f = open("E:\Python Code\Codig\demo(r).txt","r+")
f.write("abc") # replace the 1st writing number of letters (OVERWRITE)
print(f.read) # Pointer pree no TRUNCATED
f.close()

#f = open("E:\Python Code\Codig\demo(r).txt","w+")
#print(f.read()) ## It is TRUNCATED
#f.write("def")
#f.close()

f = open("E:\Python Code\Codig\demo(r).txt","a+")
print(f.read()) ## Pointer post no TRUNCATED
f.write("def")
f.close()

# With syntax
with open("E:\Python Code\Codig\demo(r).txt", "r") as f:
    data = f.read() # With -> will close the file autometically
    print(data)

with open("E:\Python Code\Codig\demo(w).txt", "w") as f:
   f.write("new data") 


# DELETING --- using the os module ( module is like a code library) 
# For installing os -- pip / pip3

import os
os.remove("E:\Python Code\Codig\sample.txt")
