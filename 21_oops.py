# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name   # encapsulation

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (Child)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

    # Method Overriding (Polymorphism)
    def speak(self):
        print(f"{self.name} barks. It's a {self.breed}.")

# Another Derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers")

# Accessing methods
dog1.speak()    # Output: Buddy barks. It's a Golden Retriever.
cat1.speak()    # Output: Whiskers meows.
