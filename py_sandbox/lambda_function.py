'''
objective: learn a little bit about the lambda function

Generally speaking: a lambda function is an anonymous function that can be created in about one line, and is typically used for something small and quick / temporary. here, we'll see some basic examples and perhaps a bit of a more advanced example (inspired by factory.py in girshick code

info sources:
https://www.w3schools.com/python/python_lambda.asp
https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593
'''

print('''
================================================================================
to start: a simple lambda function, which essentially mimics f(x) = x^2:''')
f = lambda x : x**2
for i in range(5):
    print(f(i))

print('''
================================================================================
lambda functions can take in two inputs:''')
f = lambda x,y: x*y
print(f(2,3))


print('''
================================================================================
they can be used as a function inside a function to generate some new ability:''')
def create_multiplier(val):
    return lambda a : a * val # return a function that multiplies an input by val
tripler = create_multiplier(3)
print(tripler(4))
doubler = create_multiplier(2)
print(doubler(5))


print('''
================================================================================
lambda functions are often used with map, filter, and reduce''')

# map(function_object, iterable1, iterable2,...)
list_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
output=map(lambda x : x['name'], list_a)
print([iout for iout in output])
# to put this into words: with anonymous function, return an iterable object of each dict entry 'name' for each dictionary in list list_a
# lambda function: return dict entry 'name', given a dict


print('''
================================================================================
lambda functions may actually be able to generate objects based on certain criteria''')

colors=['red','blue','yellow','green','purple','orange','white','black',]

class Dog:
    def __init__(self,furcolor):
        self.furcolor=furcolor
    def saycolor(self):
        return "the dog's fur is {}".format(self.furcolor)
# class Dog

# make a dictionary list of dogs that can be initialized if user gives desired color

dogtype={}

for icolor in  colors:
    dogtype[icolor]= (lambda furcol=icolor : Dog(furcol))
# this generates a dictionary of CLASSES, which can be called to generate an OBJECT for a given COLOR
print(type(dogtype['green']))
newdog=dogtype['green']() # generate an object from the dictionary of classes
print(newdog.saycolor()) # use function within object
#newdog.furcolor()

# we don't even need to keep the object in existence for longer than it really is needed
print(dogtype['blue']().saycolor())


print(
'''end''')
