
# Classes exercises
## Exercise 1
### Problem
Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.

### Solution
```python
class Student:
    def __init__(self, _id, name):
      student_id = _id
      student_name = name
    def display(self):
        print(f'Student id: {self.student_id}\nStudent Name: {self.student_name}')

s = Student(123, "carlos")
s.display()
```

## Exercise 2
### Problem
Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.

### Solution
```python
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
```

## Exercise 3
### Problem
Define a class called Lunch.Its __init__() method should have two arguments:selfanf menu.Where menu is a string. Add a method called menu_price.It will involve a ifstatement:

if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().

### Solution
```python
class Lunch(object):
    def __init__(self,menu):
      self.menu=menu

    def menu_price(self):
       if self.menu=="menu 1":
          print "Your choice:", menu, "Price 12.00"
       elif self.menu=="menu 2":
          print "Your choice:", menu, "Price 13.40"
       else:
          print "Error in menu"

Paul=Lunch("menu 1")
Paul.menu_price()
```



