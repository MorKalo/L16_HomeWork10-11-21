#implement the following UML. the __init__ should get the radius.
# calc_hekef will return the hekef (2 * Pi * radius). calc_area will return the area (Pi * radius ** 2).
# __str__ will print the radius , hekef and area

import math

class Circle:
    def __init__(self, radius):
        self.radius=radius

    def calc_hekef(self):
        return 2*math.pi*self.radius

    def calc_area(self):
        return math.pi*self.radius**2

    def __str__(self):
        return f'the radius is {self.radius} the hekef is {self.calc_hekef()} the area is{self.calc_area()}'

c1=Circle(3)
print(c1)