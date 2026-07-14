# WAP to askthe user to enter names of their 3 favourite movies & store them in a list

movies = []
movi1 = str (input("Enter the first movie name: "))
movi2 = str (input("Enter the second movie name: "))
movi3 = str (input("Enter the third movie name: "))
movies.append(movi1)
movies.append(movi2)
movies.append(movi3)
print(movies)
# OR
movies = []
movies.append(input("Enter the first movie name: "))
movies.append(input("Enter the second movie name: "))
movies.append(input("Enter the third movie name: "))
print(movies)

# WAP to check is a list contains a palindrome of elements. ### A palindrome is a word, number, or sequence that reads the same forward and backward.
list = [90, 88, 67, 88, 90]
copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("palindrome")
else:
    print("not palindrome")    
##

list1 = [1, 4, 5, 9, 5, 4, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not plindrome")   


# WAP to count the number of stuent with the "A" grade in the following tuple
grade = ("C", "D", "A", "A", "B","B", "A")
print(grade.count("A"))

grade = ["C", "D", "A", "A", "B","B", "A"]
grade.sort()
print(grade)
