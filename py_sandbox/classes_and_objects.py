'''
Author: Kris Gonzalez
DateCreated: 180426
Objective: serious review of classes and objects

want to cover:
basics
creating an object
class properties
class methods

'''

class dog(object):
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
