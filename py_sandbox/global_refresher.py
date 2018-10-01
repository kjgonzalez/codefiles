
#global a # does not work here. must be referred to inside a function
a = 1
def test():
	global a # important, need to declare that will refer to global variable a
	a=3
	print 'new value assigned.'

test()
print 'new value of a:',a


