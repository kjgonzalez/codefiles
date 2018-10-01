#This is a space where you can create whatever you want



class doggie:
	# stuff in this section, before (or 
	# after) the def __init__, is common
	# to all objects of this class
	breed="canaan" #all 'doggie' objects have breed="canaan"

	# stuff defined in the __init__ is 
	# uniquely defined at runtime when
	# the object is created. variables
	# unique to each object MUST be 
	# created here, otherwise they'll
	# be common to all objects (BAD)
	def __init__(self, name):
		self.name = name # each 'doggie' object must be named
		self.tricks = [] # each 'doggie' object starts with this
	# NOTE 1: variables unique to each
		# object MUST be created here, 
		# otherwise they'll be common to 
		# all objects, BAD
	# NOTE 2: private instance variables
		# don't exist in python... why. 
		# however, the convention is to 
		# put an underscore before the 
		# variable, such as "_tricks", 
		# to denote the variable shouldn't...
		# be fucked with. basically.

	# functions and attributes listed
	# here are common to all objects
	# of this class
	origin="wolf" # like "breed", is possessed by all 'doggie' objects

	# this attribute (function) is also possessed by 
	# all, i.e. all 'doggie' objects can learn a new trick
	def addTrick(self, trick):
		self.tricks.append(trick)

d=doggie('fido')
print d.breed
print d.name
print d.origin
c=doggie('lassie')
print c.origin
c.addTrick("roll over")
c.addTrick("play dead")
print c.tricks

c.tricks.append("test")
print c.tricks
