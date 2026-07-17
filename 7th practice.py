# Create a new file "practice.txt" using python. Add some data 
f= open("E:\Python Code\Codig\demo(r).txt", "w")
f.write("Hi everyone\nWe are learning File I/O\nUsing Java\nBut i like programming in Python")
f.close()
# OR
with open("E:\Python Code\Codig\demo(r).txt", "w") as f:
    f.write("Hi everyone\nWe are learning File I/O\nUsing Java\nBut i like programming in Python")


# WAF that replace of "java" with "python in above file" 
with open("E:\Python Code\Codig\demo(r).txt", "r") as f:
    data = f.read()

new_data =data.replace("Python", "JAVA")    
print (new_data)
with open("E:\Python Code\Codig\demo(r).txt", "w") as f:
    f.write(new_data)


# WAF Search if the word "learninf" exists in the file or not
def check_word():
    word = "learning"

    with open("E:\Python Code\Codig\demo(r).txt", "r") as f:
        data = f.read()

        if data.find(word) != -1:
            print("Exist")
        else:
            print("Not exist")

check_word()


# WAF to find in which line of the file does the word "learning" occur first.
def check_word():
    word = "learning"

    with open("E:\Python Code\Codig\demo(r).txt", "r") as f:
        data = f.read()

        if data.find(word) != -1:
            print("Exist")
        else:
            print("Not exist")

def che_for_lin():
    word = "learning"
    data = True
    line_no = 1
    with open("E:\Python Code\Codig\demo(r).txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print (line_no)
            line_no += 1
    return -1  

che_for_lin()



# From a file containing numbers separated by comma, print the count of even numbers
count = 0
with open("E:\Python Code\Codig\demo(r).txt", "r") as f:
        data = f.read()

nums = data.split(",")
for val in nums:
    if int(val) % 2 == 0:
     count += 1

print("Total even numbers:", count)


