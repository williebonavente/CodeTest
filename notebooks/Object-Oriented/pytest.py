"""
    objects 
        - has attributes
            - adjectives (describe) name, age, color
        - behaviors
            - verb (actions) dancing, singing, talking
    classes

"""

# Creating a class
class Parrot:
    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 15

# create parrot2 object
parrot2 = Parrot()
parrot2.name = "Viola"
parrot2.age = 10

# accessing attributes
print(f"{parrot1.name} is {parrot1.age} years old.")
print(f"{parrot2.name} is {parrot2.age} years old.")