"""
Mohamed Salem Younes

18/8/2024 1:18 am

Tasks
Beginner Level:

Task (3)


Dictionary Manipulation: Create a dictionary with 4
items where the keys are student names and the
values are their ages. Update the age of one student
and remove another student from the dictionary.
    
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