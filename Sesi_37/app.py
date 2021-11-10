# class Dog():
#     species = 'Canis familiaris'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"    

# miles = Dog('Miles', 4)
# print(miles.name)
# print(miles.age)
# print(miles.species)
# print(miles.description())
# print(miles.speak('Bark'))

# print('\n')
# buddy = Dog('Buddy', 9)
# print(buddy.name)
# print(buddy.age)
# print(buddy.species)

# print(Dog.__name__)
# print(dir(Dog))

# Other Example
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))

# # Parent and Child
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)

buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak('Woof'))

# Extend the Functionality of a Parent Class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

print(miles.speak("Grrr"))




# #Parent
# class Mom():
#     def __init__(self, name, hair_color):
#         self.name = name
#         self.hair_color = hair_color

# #Child
# class Children(Mom):
#     def __init__(self, name):
        
#         super().__init__(name,)

#     def change_hair_color(self, new_hair_color):
#         self.hair_color = new_hair_color

