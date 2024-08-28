"""
Mohamed Salem Younes

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

