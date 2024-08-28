# Mohamed Salem Younes
# Week 2 Assignment 
print(" Week 2 Assignment \n Mohamed Salem Younes")
print("-" * 80) 
"""
25/8/2024 01:01 am
Tasks

Beginner Level :

1- Conditions: Given a variable age = 15, write a Python
program that prints whether the person is a child,
teenager, or adult.

2- While Loop: Create a program that starts with a
variable number = 10. Use a while loop to subtract 1
from number until it becomes 0, printing each value of
number.

3- For Loop: Write a program that prints the
multiplication table (1 to 10) for the number 5



Intermediate Level :

1- Conditions: Given three variables a = 10, b = 25, and c
= 15, write a Python program that prints the largest
number among them without using the max() function.

2- While Loop: Start with a variable attempts = 0. Use a
while loop that continues to increment attempts until
it reaches 3, and print "Attempt number X" each time,
where X is the current attempt number.

3- For Loop: Create a program that calculates and prints
the factorial of 6 using a for loop

Advanced Level :

1- Conditions: Given a variable year = 2024, write a
program that determines if it is a leap year. The
program should check if the year is divisible by 4 but
not divisible by 100 unless it is also divisible by 400.

2- While Loop: Start with two variables a = 0 and b = 1.
Use a while loop to generate and print the first 10
numbers of the Fibonacci sequence.

3- For Loop: Write a Python program that takes the list
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10] and outputs a new
list with only the prime numbers from the original list
using nested for loops

"""

#---------------------------------------------------------------------------------------
# Beginner 1

age = 15
if age < 15 :
    print(f"Child {age} years")
elif 15 <= age < 24:
    print(f"Teenager {age} years")
else:
    print(f"Adult {age} years")
    
print("-" * 80) 

#---------------------------------------------------------------------------------------
#Beginner 2

number = 10 

while number >0:
    print(number)
    number-=1
else:
    print("End of the while loop!")

print("-" * 80) 
#---------------------------------------------------------------------------------------
#Beginner 3
for i in range(1,11):
    print(f"{i} * 5 = ", i*5)
else:
    print("End of the For loop!")
print("-" * 80) 
#---------------------------------------------------------------------------------------
# Intermediate 1
a=10
b=25
c=15

if a > b and a > c:
    print("The largest number is a =",a)
elif b>a and b > c:
    print("The largest number is b =",b)
else: 
    print("The largest number is c =",c)

print("-" * 80) 
#---------------------------------------------------------------------------------------
# Intermediate 2
attempts=0
while attempts<3:
    attempts+=1
    print("Attempts number is ",attempts)
print("-" * 80) 
#---------------------------------------------------------------------------------------
# Intermediate 3
number = 6
output=1
for i in range(1,number+1):
    output*=i
else:
    print(f"The factorial of {number} is {output}")
print("-" * 80) 
#---------------------------------------------------------------------------------------
# Advanced 1
year=2024
leap=False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

if leap:
    print(f"{year} is a Leap Year ")
else:    
    print(f"{year} is not a Leap Year ")

print("-" * 80) 
#---------------------------------------------------------------------------------------
# Advanced 2



print("-" * 80) 
#---------------------------------------------------------------------------------------
# Advanced 3



print("-" * 80) 
#---------------------------------------------------------------------------------------