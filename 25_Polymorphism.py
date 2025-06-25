class Animal:
    def speak(self):
        return "The animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "The dog barks"

class Cat(Animal):
    def speak(self):
        return "The cat meows"

# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.speak())

# Create objects
a = Animal()
d = Dog()
c = Cat()

# Call the function with different types
animal_sound(a)
animal_sound(d)
animal_sound(c)
