'''
objective: explain esoteric parts of the builtin modules of python
'''

# 01 Strings =======================================================================================

# 1.01 Formatting Strings ==================================
# source: https://docs.python.org/3.4/library/string.html#format-string-syntax
a = 10.124835429
b = 'test'
print('basic   : {}'.format(a))
print('round   : {:.2f}'.format(a))
print('scienti : {:e}'.format(a))
print('sci+rnd : {:.2e}'.format(a))
print('integer : {:d}'.format(int(a))) # if don't convert, get an error
print('percent : {:.2%}'.format(a))
print('readable: {:,}'.format(round(a*1e6)))
print('Lpad    : |{:>8}|'.format(b))
print('Rpad    : |{:<8}|'.format(b))
print('Cpad    : |{:^8}|'.format(b))
print('pad spec: |{:+^8}|'.format(b)) # charcter before '^' will be repeated everywhere
print('hex-nice: |{:0>2X}|'.format(10))

# classic example: lpad with zeros:
print('typical : {:0>3}'.format(3))
# another way to pad strings

print('text with rpad '.ljust(30,'-'))

name='Fred'
age=42
print('his name is {} and he is {} years old'.format(name,age))
# post python3.6 thing: f-string literal. functionally identical as above
print(f'He said his name is {name} and he is {age} years old.') # not favored


# 02 Windows Command Line  =========================================================================

import os

# 2.01 Get Command Line output as string ===============================
x = os.popen('echo hello').read()
print(x)

# 03 Bytes<>Ints<>Hex =============================================================
'''
want to understand how bytes are manipulated & converted in python
DO NOT USE "hex()"! THIS ONLY RETURNS A NORMAL STRING OF WHAT A DECIMAL VALUE LOOKS LIKE AS A HEX
'''

# alphanumeric data
bytestr = b'this' # print() => b'this' # note: string of bytes
normstr = bytestr.decode() # print() => 'this' # normal string
bytestr2 = normstr.encode() # back to a bytestr
print(bytestr)

# note that mixing encodings can lead to incorrect-looking data
print(
    (chr(0).encode('utf-16')+'this'.encode()).decode('utf-16')
)

# numeric data: switch from between: decimal <=> hex <=> binary <=> decimal
# ex: 165 = 1010 0101 = 0xA5. want to pull out exact values from each place
valint=165
valhex=b'\xa5' # 165
valbin='0b10100101'

# how to swap between each:
print('as int :',valint)
print('int2hex:',valint.to_bytes(1,'little'))
print('int2bin:',bin(valint))
print('---')
print('as hex :',valhex)
print('hex2int:',int.from_bytes(valhex,'little'))
print('hex2bin:',bin(int.from_bytes(valhex,'little')))
print('---')
print('as bin :',valbin)
print('bin2int:',int(valbin,2))
print('bin2hex:',int(valbin,2).to_bytes(1,'little'))

# 04 Decorators ===================================================================

# background, long method:

def say_whee():
    print("Whee!")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

print('0th time')
say_whee()

print('1st time')
say_whee = my_decorator(say_whee)
say_whee()

print('2nd time')
say_whee = my_decorator(say_whee)
say_whee()

# short method
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

print('short method')

print('0th time')
def say_whee():
    print("Whee!")
say_whee()

print('1st time')
@my_decorator
def say_whee():
    print("Whee!")
say_whee()


print('2nd time')
@my_decorator
@my_decorator
def say_whee():
    print("Whee!")
say_whee()

# a few built-in decorators
class Rect:
    def __init__(self):
        self.x = 3
        self.y = 4
        self._z = 0
    @staticmethod
    def anyarea(ht,wd):
        return ht*wd
    @property
    def area(self):
        return self.x*self.y
    @property
    def z(self):
        return self._z
    @z.setter # benefit: run desired new value through a check / other operations if desired
    def z(self,val):
        assert val>=0, "value smaller than zero"
        self._z = val

# 05 Sets, lambda, maps =========================================================

# sets (src:https://docs.python.org/3/library/stdtypes.html#set)
A=set('one two three four 5 6 7'.split(' '))
B=set('two four 6 eight 10'.split(' '))

A_only = A-B      # or: A.difference(B)
B_only = B-A

AandB = A-(A-B)   # or: AandB=A.intersection(B)
                # or: AandB=A&B

AorB = A | B        # or: AorB=A.union(B)

# list comprehension
a = [i*2 for i in range(5)]
a = {jletter:inum for inum,jletter in enumerate(list('abcdef'))}
a = [i for i in range(16) if(i % 2)]

# lambda function, or anonymous function
f = lambda: print('hello')
f = lambda x: 2*x
f = lambda x,y: 2*(x+y)

# map function
# return a map object (iterator) of result safter applying function to each item of a list
# usage: map(function, iterator)

fn_sq = lambda x: x**2
x = list(range(10))
y = list(map(fn_sq,x))

pyt = lambda x,y:(x*x+y*y)**0.5
x0 = [1,3,5]
x1 = [3**0.5,4,12]
y = list(map(pyt,x0,x1))

# 'listify'
b = list(map(list,'one two thr'.split(' '))) # out:[['o','n','e'],['t','w','o'],['t','h','r']]


# 06 Sets, lambda, maps =========================================================
print('FOLLOWING IS ONLY POSSIBLE WITH PYTHON 3.7 AND UP')

# data classes (py3.7): mutable structs
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0 # can have default values

# NamedTuple's (py3.6): immutable structs
from typing import NamedTuple

class MyStruct(NamedTuple):
    foo: str
    bar: int
    baz: list



# eof





