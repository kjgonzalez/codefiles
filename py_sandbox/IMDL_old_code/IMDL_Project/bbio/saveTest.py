#!/bin/python

#test to see IO stuff

# a = int(raw_input("your favorite number: "))
# print a


def saveValues(arr):
	saveFile = open('savedThresh','w')
	for i in range(len(a)):
		saveFile.write(str(a[i])+'\n')
	saveFile.close()

def openValues():
	openFile=open('savedThresh','r')
	arr=range(6)
	j=0
	for i in openFile:
		arr[j]=int(i)
		j+=1
	openFile.close()	
	return arr


a=range(120,126)
saveValues(a)
print openValues()


# saveFile = open('test','w')

# for i in range(len(a)):
# 	saveFile.write(str(a[i])+'\n')
# saveFile.close()


# openFile=open('test','r')

# for i in openFile:
# 	print int(i)
# openFile.close()