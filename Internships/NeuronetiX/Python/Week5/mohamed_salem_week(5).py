# Mohamed Salem Younes
# Week 5 Assignment 
print(" Week 5 Assignment \n Mohamed Salem Younes")
print("-" * 80) 
#---------------------------------------------------------------------------------------

"""
 Beginner Level :
 
1- Basic Calculator with Multiple Exceptions: 
Create a program that asks the user to input two numbersand an operation (addition, subtraction, etc.). 
Handle cases where the user enters invalid numbers,chooses an invalid operation, or tries to divide by zero
"""
try:
    x = float(input("The first number: ")) 
    y = float(input("The second number: "))  
    

    operation = input("Choose an operation:\n1 - Addition\n2 - Subtraction\n3 - Division\n4 - Multiplication\n")
    
    if operation == "1":
        print("Result =", x + y)
    elif operation == "2":
        print("Result =", x - y)
    elif operation == "3":
        if y == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result =", x / y)
    elif operation == "4":
        print("Result =", x * y)
    else:
        print("Invalid operation. Please choose a valid operation (1-4).")

except ValueError:
    print("Please enter valid numbers.")

except Exception as e:
    print(f" Error occurred: {e}")
    
print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- List Element Retrieval: Write a function that takes a list and asks the user for an index to retrieve anelement. 
Handle cases where the index is out of range or the input is not an integer. 
Print anappropriate error message in each case.

"""

def RetrieveElement(list):
    try:
        index = int(input("index of the list: "))
        
        element = list[index]
        print(f"Element at index {index} is: {element}")
    
    except ValueError:
        print("enter a valid integer")
    
    except IndexError:
        print("Index is out of range")
    
    except Exception as e:
        print(f"error : {e}")

list = [1231,132,1,321,32,32,132,132,1858,84,9]
RetrieveElement(list)


#---------------------------------------------------------------------------------------

print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3-  Dictionary Key Lookup with Basic Error Handling: Ask the user to input a key to look up in a pre-defined dictionary.
Use try-except to handle cases where the key does not exist. Additionally, 
handlecases where the user input is not valid, such as providing an empty string or a non-string data type (likea number)
"""
print("Begineer 3")



#---------------------------------------------------------------------------------------

print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
1- 
"""
print("Intermediate 1")



#---------------------------------------------------------------------------------------



print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- 
 
"""
print("Intermediate 2")






#---------------------------------------------------------------------------------------



print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3- 
"""
print("Intermediate 3")


    



#---------------------------------------------------------------------------------------


print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
1- 
"""
print("Advanced 1")




#---------------------------------------------------------------------------------------


print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- 
 
"""
print("Advanced 2")



#---------------------------------------------------------------------------------------



print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3- 
 
"""
print("Advanced 3")



#---------------------------------------------------------------------------------------
