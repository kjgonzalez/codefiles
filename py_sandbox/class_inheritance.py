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
        Person.__init__(self,first,last) # first, create the "person" level characteristics
        self.staffnumber = staffnum # then assign new characteristics
    
    def GetEmployee(self):
        return self.Name()+', '+self.staffnumber

# note: using *<list> to give arguments is called unpacking a container / iterator
x = Person(*'marge simpson'.split(' ')) 
y = Employee(*'homer simpson 1007'.split(' '))

print(x.Name())
print(y.GetEmployee())

'''
however, what if we just put the methods "Name" and "getEmployee" into a __str__ method?

note1: Overriding is an object-oriented programming feature that allows 
    a subclass to provide a different implementation of a method that is 
    already defined by its superclass or by one of its superclasses. 

note2: Overloading is the ability to define the same method, with the same 
    name but with a different number of arguments and types. It's the ability 
    of one function to perform different tasks, depending on the number of 
    parameters or the types of the parameters.
'''

print('with overriding:')
class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age
    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)
class Employee(Person):
    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum
    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber

x = Person('marge','simpson',36) 
y = Employee('homer','simpson',28,'1007')

print(x)
print(y)

# attempt at overloading with *args
def add(*args):
    # giving multiple arguments is still valid
    a=0
    for i in args: a+=i
    return a

print('sums with increasing number of arguments:')
for i in range(5):
    print('i:{}\tsum:{}'.format(i,add(*range(i+1)) ))









# eof