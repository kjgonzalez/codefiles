import os
os.system('dir /s /b > delme.txt')
f=file('delme.txt') # needs .txt extension, forloop exclusion
a=[]
for i in f:
	if('.' not in i):
		a.append(i[:-1])
f.close()
os.system('del delme.txt')
for i in a:
	print i