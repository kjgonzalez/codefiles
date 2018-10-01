'''
kjgnote: able to remote load a module via: 
>> import os
>> origDir = os.getcwd()
>> os.chdir(ModuleDirectory)
>> import ModuleName
>> os.chdir(origDir)

'''

def pyt(arr):
	return sum([i**2 for i in arr])**0.5


