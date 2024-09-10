# Mohamed Salem Younes
# Week 3 Assignment 
print(" Week 3 Assignment \n Mohamed Salem Younes")
print("-" * 80) 
#---------------------------------------------------------------------------------------

"""
 Beginner Level :
 
1- Function with Multiple Arguments: Write a function
 calculate_total_price() that takes the price of an item
 and the quantity purchased, and returns the total price.
 Ensure the function handles cases where either
 argument is missing by setting default values.

"""
print("Begineer 1")
def calculate_total_price(*prices,price=0):
    total_prices=0
    for price in prices:
        total_prices+=price
    return total_prices


#call Function
total_prices = calculate_total_price(1,2,3,4,5,6,7)
print("The total price =",total_prices)


print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- Function with Conditional Logic: Create a function
 i s_even() that takes an integer as an argument and
 returns True if the number is even and False if it's odd.
 Include simple error handling for non-integer inputs
 using conditional statements.

"""
print("Begineer 2")

def number_check(number=0):
    if not isinstance(number, int):
        print("please use integer numbers as input")
    else:
        if number % 2==0:
            print(f"Number {number} is an Even number")
        else:
            print(f"Number {number} is an Odd number")


def is_even(value):
    
    if not isinstance(value, int):
        return "Parameter must be an integer."
    if value % 2 == 0:
        return True
    else:
        return False

#Call Function

number_check(17)
print(is_even(17))

#---------------------------------------------------------------------------------------

print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3- String Manipulation in Functions: Write a function
 format_name() that takes a first name and last name as
 arguments and returns a neatly formatted full name,
 e.g., "Ahmed Hazem". Ensure that the function handles
 cases where names are provided in lowercase.
 
"""
print("Begineer 3")

def format_name(first_name,last_name):
    print(f"{first_name.capitalize()} {last_name.capitalize()}")


#Call Function

format_name("ahmed" , "salem")

#---------------------------------------------------------------------------------------

print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
1- List Manipulation in Functions: Write a function
 remove_duplicates() that takes a list of numbers and
 returns a new list with all duplicate numbers removed,
 maintaining the original order.
"""
print("Intermediate 1")

def remove_duplicates(number_list):
    return set(number_list)

list1=[1,2,3,4,5,44,1,1,2,3,4,5,6,7,8,1,2,3,4,5,1,4]
list2=remove_duplicates(list1)
print(list2)

#---------------------------------------------------------------------------------------



print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- Recursive Function for Factorial Calculation: Write a
 function factorial() that takes an integer and returns
 i ts factorial using recursion. Ensure the function is
 optimized for larger inputs.
 
"""
print("Intermediate 2")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))




#---------------------------------------------------------------------------------------



print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3- Function with Multiple Return Values: Create a
 function calculate_statistics() that takes a list of
 scores and returns the highest score, the lowest score,
 and the average score. Ensure the function works
 correctly with positive numbers
"""
print("Intermediate 3")

numbers=[20,30,40,5,156,77,55,46]
def calculate_statistics(x):
    print("Scores :",x)
    print("The highest Score :",max(x))
    print("The Lowest Score :",min(x))
    print("The Average Score :",sum(x)//len(x))

calculate_statistics(numbers)
    



#---------------------------------------------------------------------------------------


print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
1- Higher-Order Function with List Filtering: Create a
 function filter_and_apply() that takes a list of numbers
 and another function as arguments. The function should
 filter out all non-positive numbers and then apply the
 given function (which could be squaring the number) to
 the remaining numbers, returning the modified list.
"""
print("Advanced 1")

def is_positive(number):
    return number > 0

def filter_and_apply(numbers, func):
    filtered_numbers = filter(is_positive, numbers)
    result = list(map(func, filtered_numbers))
    return result

def square(x):
    return x ** 2

numbers = [-5, 3, 0, -1, 4, 2]

modified_list = filter_and_apply(numbers, square)

print(modified_list)


#---------------------------------------------------------------------------------------


print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- Advanced Recursion with String Manipulation: Write a
 recursive function reverse_string() that takes a string
 and returns it reversed. Ensure the function handles
 both even and odd-length strings correctly.
 
"""
print("Advanced 2")

def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

string = "Mohamed Salem Younes"
reversed_string = reverse_string(string)
print(reversed_string)


#---------------------------------------------------------------------------------------



print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3- Implementing an Algorithm: Write a function
 binary_search() that implements the binary search
 algorithm. The function should take a sorted list of
 numbers and a target number, returning the index of the
 target in the list or -1 if the target is not found.
 
"""
print("Advanced 3")

def binary_search(arr, target):

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(numbers, target)
print(f"Index of {target}: {result}")


#---------------------------------------------------------------------------------------
