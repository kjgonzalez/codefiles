'''
objective: modify some "magic number" in this module from a different location
    to affect how things run here.

update: yes, it's possible to change a "config value" after loading, then use
    the modified value to affect other functions.

Example:
    import config_runtime as c
    c.addStuff(1,2) # = 4
    c.num=3
    c.addStuff(1,2) # = 6
'''

num=1

def addStuff(a,b):
    return a+b+num
