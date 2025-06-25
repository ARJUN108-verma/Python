# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Another Derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call methods
dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.
