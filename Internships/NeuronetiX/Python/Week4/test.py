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

