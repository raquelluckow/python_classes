## Exercise 1 ##
#Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. 
#Create a function to display all attributes and their values in the Student class.
import math as m

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    def show(self):
        print('Student id: {}'.format(self.student_id))
        print('Student name: {}'.format(self.student_name))

student = Student(10740, "Raquel")
student.show()

## Exercise 2 ##
#Write a Python class named Circle constructed from a radius and two methods
#that will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        a = self.r**m.pi
        return a
    #Poderia chamar a função e a variável com o mesmo nome?
    def perimeter(self):
        p = 2*m.pi*self.r
        return p

circle = Circle(5)
print(circle.area())
print(circle.perimeter())

## Exercise 3 ##
#Define a class called Lunch.Its init() method should have two arguments:self and menu.
#Where menu is a string. Add a method called menu_price.It will involve a ifstatement:

class Lunch():
    def __init__(self,menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice: {}, Price 12.00".format(self.menu)) ##self.menu ou só menu?
        elif self.menu == "menu 2":
            print("Your choice: {}, Price 13.40".format(self.menu))
        else:
            print("Error in menu")
lunch = Lunch("menu 1")
lunch.menu_price() ## não entendi

import pandas as pd

