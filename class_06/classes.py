import pandas as pd 

# Definition = Class 
class Person:
    age = 0
    # Is called when the object is called. It is a special method. 
    def __init__(self, age): 
        self.age = age 
        self.lala = "lala"
    # Is called when you want to print the object.  
    def __str__(self):
        return "Person age is {}".format(self.age)

    # A wathever method.
    def birthday(self, num):
        self.age = num + self.age
        #return self.age


# P is an object
p = Person(2)
print(p.age)
print(p.lala)
p.birthday(2)
print(p.age)
print(p)
