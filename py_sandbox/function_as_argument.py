'''
simple demo on how to give a function as an argument to another function
'''

def square(x): return x**2

def callfn(x,fn):
    return fn(x)

print(callfn(3,square))
# output will be '9'