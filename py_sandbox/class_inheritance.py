'''
objective: learn a little bit about class inheritance in python

source: https://www.python-course.eu/python3_inheritance.php
'''


# first example: 

class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
    def Name(self):
        return self.firstname+' '+self.lastname
# class Person

class Employee(Person): # this class is now based on previous, more general class
    def __init__(self,first,last,staffnum):
        Person.__init__(self,first,last) # first, create the person...?
        self.staffnumber = staffnum # then assign new characteristics?
    
    def GetEmployee(self):
        return self.Name()+', '+self.staffnumber

# note: using *<list> to give arguments is called unpacking a container / iterator
x = Person(*'marge simpson'.split(' ')) 
y = Employee(*'homer simpson 1007'.split(' '))

print(x.Name())
print(y.Name)

