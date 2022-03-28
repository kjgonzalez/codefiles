'''
objective: synchronize files between two locations. 

future: 
* synchronize between more than three locations
* update old file with new file (look at date modified)

steps: 
1. open paths.txt file
2. import paths to memory, save in 'path' variable
3. get contents of each folder
4. figure out what's different between the two
5. copy data over
'''
def enclose(pathIn):
	''' enclose, "Windows Filepath Correction'
		add double quotes to filepaths, to allow correct
			interpretation by windows command prompt'''
	return '"'+pathIn+'"'



# get list of paths to be synchronized
f=file('paths.txt')
path=[]				# initialize array variable
for i in f:
	path.append(i)	# assuming that paths.txt only has a few rows
	path[-1]=path[-1].strip()
f.close()			# don't need text anymore
# now have var 'path' that holds top-level folders to sync

#get F0 (top level folder) files to sync
# will start only by transferring one way, then both ways.
'''
1. get list of files in path1
2. copy to path2
- - - - 
1. get list of files in path1
2. get list of files in path2
3. if two files have same name, check which is newer, delete older
4. copy files from path2 to path1
5. copy files from path1 to path2
'''
import os
# get list of files in path1
f_path=len(path)*[None] #set up 2D array of files in path
# f_path[basepath][files in basepath]
for i in range(len(path)):
	f_path[i]=os.listdir(path[i])

# KJGNOTE: Disabling this section temporarily for recursive function testing
# # copy files from path1 to path2
# # print len(f_path) # currently two items in toplvl f_path[j][i]
# for j in range(len(f_path)):
	# for i in range(len(f_path[j])):
		# for k in range(len(f_path)):
			# if(k != j):
				# print 'copy '+enclose(path[j]+os.sep+f_path[j][i])+' '+enclose(path[k])
				# os.system('copy '+enclose(path[j]+os.sep+f_path[j][i])+' '+enclose(path[k]))

# def rdl():


# quick refresher on recursive functions: 
# def lpad(a,n):
	# if(len(a)<n):
		# a=lpad('-'+a,n)
	# return a
# print lpad('test',6)

'''
steps
1. list contents of current folder
2. check for a folder
	a. if yes, setup forloop to go into each folder and repeat
3. if no, return 0
'''

# note: 'os' module alrdy imported
def listdir(hasFolder=1):
	a=os.listdir(

