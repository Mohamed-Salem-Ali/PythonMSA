# Mohamed Salem Younes
# Week 4 Assignment 
print(" Week 4 Assignment \n Mohamed Salem Younes")
print("-" * 80) 
#---------------------------------------------------------------------------------------

"""
 Beginner Level :
 
1- Class and Object Relationships
Create a class Animal with attributes species and sound.
Define a method make_sound to print thesound. 
Then, create subclasses Dog and Cat that inherit from Animal and set different sounds.
Instantiate these objects and call their methods

"""
class Animal:
    def __init__(self,species,sound):
        self.species=species
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.species} makes a {self.sound} sound!!")

class Dog(Animal):
    def __init__(self):
      super().__init__('Dog','bark')

class Cat(Animal):
    def __init__(self):
      super().__init__("Cat","meow")
            
dog=Dog()
cat=Cat()

dog.make_sound()
cat.make_sound()

print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
2- Using Inheritance and the Super() Function
Create a base class Person with attributes name and age, and a method display_info. 
Create asubclass Employee that inherits from Person and adds an attribute salary. 
Use super() in theEmployee class to initialize the base class’s attributes. 
Create objects and display their information

"""
print("Begineer 2")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"{self.name} {self.age}")

class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name,age)
        self.salary=salary
        
    def display_info(self):
        super().display_info()
        print(f"Salary : {self.salary}")
        
person =Person("Salem",24)
employee = Employee("Younes",45,10000) 

person.display_info()    
employee.display_info()
#---------------------------------------------------------------------------------------

print("-" * 80) 
#---------------------------------------------------------------------------------------
"""
3- Basic Polymorphism with Classes
Create a class Vehicle with a method start_engine that prints "Engine started." 
Create two subclassesCar and Boat, each with its own version of start_engine. 
Demonstrate polymorphism by callingstart_engine from objects of Car and Boat. 
"""
print("Begineer 3")

class Vehicle:
    def start_engine(self):
        print("Engine start")

class Car(Vehicle):
    def start_engine(self):
        print("Car start")

class Boat(Vehicle):
    def start_engine(self):
        print("Boat start")

def start_vehicle_engine(vehicle):
    vehicle.start_engine()

car = Car()
boat = Boat()

start_vehicle_engine(car)  
start_vehicle_engine(boat)

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
