'''
Author: Kris Gonzalez
DateCreated: 180426
Objective: serious review of classes, objects, and related topics

Covers:
* basics
* creating an object
* class properties (attributes)
* class functions (methods)
* inheritance / subclass
* method overriding
* "super" function

'''

(''' ===========================================================================
Basics of a class in python ''')

class dog:
    '''
    this is a class that will outline properties and methods of dogs
    '''

    # global object properties
    species = 'canine'
    # kjgnote: don't put any 'self' items here!!!

    # object-specific properties are defined in the init method
    def __init__(self,name='bob',breed='labrador',age=3):
        import numpy as np
        self.np = np # this is how you can keep a module inside a class
        self.name = name
        self.breed = breed
        self.age = age
        self.hasitem = False
        self.hasitem_name = ''
    def bark(self):
        '''this function requires no inputs, and has a simple output'''
        print(self.name+' barks. Woof!')

    def barktwice(self):
        '''this function calls another function in the class'''
        self.bark()
        self.bark()

    def __itemstate(self,item='',state=False):
        '''this function assigns a state to two variables when used.
            designated as private var, so has two underscore chars'''
        self.hasitem = state
        self.hasitem_name = item

    def fetch(self,item):
        '''this function takes in an argument, and requires
            knowledge of another variable's state'''
        if(self.hasitem):
            # can't grab something else, already has something
            print(self.name+' stays put, already has '+self.hasitem_name)
        else:
                self.__itemstate(item,True)
                print(self.name+' grabs the '+self.hasitem_name)
    def giveitem(self):
        ''' if dog has an item, give it.'''
        if(self.hasitem):
            print(self.name+' gives you the '+self.hasitem_name)
            self.__itemstate() # default is to not have anything
        else:
            print(self.name+' doesn''t have anything')


(''' ===========================================================================
How a subclass / inheritance works in python
example: shape>>rectangle>>square
real-world: imdb>>kitti>>kitti_3d
''')

class shape:
    def __init__(self,color):
        self.color=color
    def perim(self):
        raise NotImplementedError
    def area(self):
        raise NotImplementedError

class rectangle(shape):
    def __init__(self,length,width,color='red'):
        shape.__init__(self,color)
        self.length=length
        self.width=width
    def perim(self):
        return 2*(self.length+self.width)

    @property
    def area(self):
        return self.length*self.width

class square(rectangle):
    def __init__(self,length,color='blue'):
        rectangle.__init__(self,length,length,color)

    def area(self):
        print('giving square area')
        return self.length*self.length

shap=shape('purple')
rect=rectangle(3,5)
squa=square(4)
# import ipdb;ipdb.set_trace()

(''' ===========================================================================
Class inheritance example 2 in python

source: https://www.python-course.eu/python3_inheritance.php
''')

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

#print(x)
#print(y)

# attempt at overloading with *args
def add(*args):
    # giving multiple arguments is still valid
    a=0
    for i in args: a+=i
    return a
#print('sums with increasing number of arguments:')
#for i in range(5):
    #print('i:{}\tsum:{}'.format(i,add(*range(i+1)) ))

(''' ===========================================================================
Using the "super" function
src1: https://www.pythonforbeginners.com/super/working-python-super-function
src2: https://www.python-course.eu/python3_multiple_inheritance.php

goal: want a "much more abstract and portable solution for initializing
    classes" (arguably within the subclass it's being called from)
additionally: seems to handle the "Method Resolution Order" much better than
    the default way of simply initializing the class.

''')

# will try and use the shapes examples

class triangle(shape):
    def __init__(self,sides_arr,color='blue'):
        super().__init__(color=color)
        self.lengths=sides_arr+[]
        self.lengths.sort()
        assert self.lengths[-1]<sum(self.lengths[:2]),"Longest side too long"
    def perim(self):
        return sum(self.lengths)

t=triangle([3.0,4.0,5.0])

''' ITERATORS ============================================================== '''
class counters:
    def __init__(self):
        self.items=[1,2,3,4,5,6,7,8,9]
        self._index=0
    def __iter__(self):
        ''' this enables the object to be iterable '''
        return self
    def __len__(self):
        ''' this enables the object to use "next" function '''
        return len(self.items)
    def __next__(self):
        ''' specific behavior that happens everytime you iterate over the class '''
        if(self._index>=len(self.items)):
            self._index=0
            raise StopIteration
        res = self.items[self._index]
        self._index += 1
        return res

c=counters()
print('version 1:',end=' ')
for i in c:
    print(i,end=' ')
print()
print('version 2:',end=' ')
for i in range(len(c.items)):
    print(next(c),end=' ')


''' ABSTRACTMETHOD ========================================================= '''
from abc import abstractmethod

class Animal:
    def __init__(self,name):
        self.name=name
        self.loc = (0,0)

    @abstractmethod
    def move(self,location):
        ''' by writing @abstractmethod, child class MUST implement "concrete"
            version of this method, otherwise run into an error
        '''
        pass

class Cat(Animal):
    def __init__(self,name):
        # Animal.__init__(self,name)
        super().__init__(name) # alternate method of calling
    # def move(self,location):
        # self.loc = location
        # print('{} moves to {}'.format(name,location))

c = Cat('tammy')
c.move((1,2))


''' creating a __call__ method ========================================= '''
# call enables the entire object to be used like a function
print()
class AddTwo:
    def __init__(self,a):
        self.a = a

    def __call__(self):
        return self.a+2

    def method_add(self):
        return self.a+2
x = AddTwo(2)
print(x)
print( x() )
print( x.method_add() )

# eof

''' All "magic" methods aka "dunder" (double underscore) methods ======= '''
# this section will exist as a complete collection of all magic methods used in python classes
print('= {} {}'.format('dunder methods','='*50))
class Dunders:
    def __init__(self):
        ''' used when class is initialized. usage: x = Dunders(args) '''
        print('initialized')
        self.val = 0
        self.arr = [1,2,3,4,5]
        self._index = 0
    def __str__(self):
        ''' used when class is called like a string object '''
        return 'object called like a string'
    def __call__(self):
        ''' used when object called like a function '''
        return 1
    def __getitem__(self, item):
        ''' used when object called like a dict / array '''
        return 'a'*item
    def __len__(self):
        ''' used when object acts like an array '''
        return 2
    def __iter__(self):
        ''' allows the object to be iterable '''
        return self
    def __next__(self):
        ''' allows using "next" builtin '''
        if(self._index>=len(self.arr)):
            self._index=0
            raise StopIteration
        res = self.arr[self._index]
        self._index += 1
        return res
    def __repr__(self):
        ''' allows using "repr" builtin. "official" string of object. "different" than __str__ '''
        return 'Very important string'
    def __reversed__(self):
        ''' allows using "reversed" builtin. can still return w/e you want '''
        return [7,6,5,4,3]
    def __del__(self):
        ''' handles deletion of object '''
        print('this object being deleted')
    def ignored(self):
        print('''note: will be skipping these:
         * __eq__ - check for equality, and others: (lt, le, ne, gt, ge)
         * __bool__ - check for true/false. if not defined, len() is used (True for non-zero values)
         * __bytes__ - return a bytes representation of data
         * __add__ - addition
         * __getattr__
         * __setattr__
         * __delattr__
         * __getattribute__
         * __dir__
         * any others mentioned on: https://docs.python.org/3/reference/datamodel.html#specialnames
         ''')



# examples of each
x = Dunders() # __init__
print(x) # __str__
print(x()) # __call__
print(x[4]) # __getitem__
print('using len dunder:',len(x)) # __len__
print(next(x)) # __next__
print([i for i in x]) # __iter__
print(repr(x)) # __repr__
print(list(reversed(x))) # __reversed__












