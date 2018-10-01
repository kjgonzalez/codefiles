print 'hello world'

def createFile():
	f=file('test.txt','w')
	newl='\n'
	f.write('one two'+newl)
	f.write('open C:\\a\\b\\c\\d\\superCool.txt'+newl)
	f.write('one two four'+newl)
	f.write('one two'+newl)
	f.write('saveas C:\\a\\b\\c\\d\\superCool.txt')
	f.close()
	return 1

def countLinesinFile(filename):
	f=file(filename)
	n=0
	for i in f:
		n=n+1
	f.close()
	return n

#print createFile()

import os
print os.name

'''
objective: read in a file, change a certain piece in a line,
then save the file again. only want to replace specific places
in the file
'''

def replace(line,orig,new):
	loc=0
	if(orig in line):
		loc=line.index(orig)
		return line[:loc]+new+line[loc+len(orig):]
	else: 
		print 'error'

a='life is good sometimes'
print replace(a,'good','bad')

key='Cool'
replacement='Hot'

n=countLinesinFile('test.txt')
f=file('test.txt')
f2=file('test2.txt','w')
for i in range(0,n):
	curline=f.readline()

	# modify line if necessary
	if(key in curline):
		curline=replace(curline,key,replacement)
	# direct copy all of file
	f2.write(curline) #write line to new file


f.close()
f2.close()

# later on, could possibly rename file to overwrite original or 
# to overwrite a common 'runme' file
os.system('start /B notepad test2.txt')

