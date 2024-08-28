# Mohamed Salem Younes
# Week 1 Assignment 
print(" Week 1 Assignment \n Mohamed Salem Younes")
print("-" * 80) 
"""
18/8/2024 12:55 am
Tasks
Beginner Level :
Task (1)

List Creation and Indexing: Create a list of 5 favorite
fruits and print the first and last fruit using indexing.  
"""

#Create a list of 5 favorite fruits
fruits = ["Apple", "Orange", "Mango","Banana","Pineapple"]
#first fruit
first_fruit=fruits[0]

#second fruit 
last_fruit=fruits[-1]

# print the first and last fruit 
print("The First fruit is" , first_fruit)
print("The Last fruit is" , last_fruit)
print("-" * 80) 
# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

"""
18/8/2024 1:02 am
Tasks
Beginner Level:
Task (2)

Tuple Usage: Define a tuple with 3 cities you want to
visit. Attempt to change one city in the tuple to
observe that tuples are immutable.       
"""

Cities = ("London", "Tokyo" , "New York City")

# Tuples are immutable
# Cannot change their elements directly
try :
    Cities[0] = "Paris"
except:
    print("Error")
print(Cities)

# If you assign a tuple element to a variable and then change that variable.
# It does not affect the original tuple.
city_1 = Cities[0]
print("city_1:", city_1)


city_1 = "Bangkok"
print("New city_1:", city_1)

print("Tuple :", Cities)
print("-" * 80) 
# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

"""
18/8/2024 1:18 am
Tasks
Beginner Level:
Task (3)

Dictionary Basics: Create a dictionary to store 3 key value pairs, 
where the keys are subjects (like Math,Science, English) 
and the values are your scores in each. 
Print the score of a specific subject.

    
"""
subjects = {
    "Math":85,
    "Science":90,
    "English":95
}
print(subjects["Science"])

print("-" * 80) 
# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
"""
21/8/2024 10:53 pm
Tasks
Intermediate Level
Task (1)

List Operations: Create a list of 10 random numbers.
Add 2 more numbers to the list, remove one number,
and then sort the list in ascending order.
"""
random_list = [12,5,6,88,9,4,22,35,87,98]
random_list.append(77)
random_list.insert(99,7)
random_list.pop(7)
random_list.sort()
print(random_list)

print("-" * 80) 

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

"""
22/8/2024 04:00 pm
Tasks
Intermediate Level
Task (2)

Tuple Unpacking: Given a tuple (10, 20, 30), unpack its
values into three variables a, b, and c, and print them.
"""
tuple_X = (10,20,30)
a,b,c = tuple_X
print(a,b,c)

print("-" * 80) 

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

"""
23/8/2024 04:04 pm
Tasks
Intermediate Level
Task (3)

Dictionary Manipulation: Create a dictionary with 4
items where the keys are student names and the
values are their ages. Update the age of one student
and remove another student from the dictionary
"""
# Create a dictionary with 4 items 
# The keys are student names and the values are their ages 

Students = {
    "Mohamed" : 24,
    "Salem" : 59,
    "Younes" : 18,
    "Ali" : 28 
}

print("Students =",Students)
student_1_age=Students["Mohamed"]
print("Mohamed age:",student_1_age)

# Update the age of one student
Students["Younes"]=33
student_2_age=Students["Younes"]
print("Younes age:",student_2_age)
print("Students =",Students)

# Remove another student from the dictionary
Students.pop('Ali')
print("Students =",Students)
try:
    print(Students["Ali"])
except KeyError as e :
    print("Error", e)


# Remove another student from the dictionary
del Students['Salem']
print("Students =",Students)
try:
    print(Students["Salem"])
except KeyError as e :
    print("Error", e)
print("-" * 80) 

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
"""
23/8/2024 04:45 pm
Tasks
Advanced Level
Task (1)

Nested Lists: Create a list that contains 3 lists, where
each inner list contains 3 integers. Manually calculate
and print the sum of each inner list.
"""
nested_list = [
    [10,50,60],
    [12,65,77],
    [76,89,17]
]
print("Sum First_list = ",sum(nested_list[0]))
print("Sum Second_list = ",sum(nested_list[1]))
print("Sum Third_list = ",sum(nested_list[2]))

print("-" * 80) 

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
"""
23/8/2024 04:52 pm
Tasks
Advanced Level
Task (2)

Tuples as Dictionary Keys: Create a dictionary where
the keys are tuples representing coordinates (x, y) on
a grid, and the values are the names of objects located
at those coordinates. Access the object at a specific
coordinate by using its tuple key.

"""
places_names={
    (9,10):"House",
    (15,11):"Club",
    (25,3):"Supermarket",
    (6,6):"Garden"
}
print("The name of First place =",places_names[(9,10)])
print("-" * 80) 

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
"""
23/8/2024 04:04 pm
Tasks
Advanced Level
Task (3)

Complex Dictionary Operations: Create a dictionary
that maps student names to a list of their scores in 3
subjects. Manually calculate and print the average
score for each student.
"""
Students_Scores={   
    "Mohamed":[85,20,46,70],
    "Salem":[78,55,99,44],
    "Younes":[77,81,53,79]
}
print("Average Scores of student 1 =",sum(Students_Scores["Mohamed"])/len(Students_Scores["Mohamed"]))
print("Average Scores of student 2 =",sum(Students_Scores["Salem"])/len(Students_Scores["Salem"]))
print("Average Scores of student 3 =",sum(Students_Scores["Younes"])/len(Students_Scores["Younes"]))
print("-" * 80) 
# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
