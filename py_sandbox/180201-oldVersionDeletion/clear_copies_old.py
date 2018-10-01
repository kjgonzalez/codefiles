'''
Author: Kris Gonzalez
DateCreated: 180201
Objective: want to create script for correctly removing old creo files 
	(generated when saving. ex: item.prt.1, item.prt.2, etc)
Version: 1.0 (functioning)

Assumptions: 
* will not look at number of file, only latest date modified of each file. keep only the latest edit.
* will only look in same folder, won't do any recursive searching. 
* will check all files in folder that have TWO periods, no files like .py or .txt


'''
# will define own find-i'th-item-in-string-function
def nstrfind(mainstring,substr,n=1):
	'''
	Objective: find i'th item in a string. custom version of find. If user 
		doesn't specify n, then will return first location. if n is larger 
		than number of times substr occurs, return an error (-1).
	'''
	loc = -1
	curr=0
	if(mainstring.count(substr)<n):
		# error
		print 'lala'
		return -1
	for i in range(0,n):
		curr = loc+1
		loc=mainstring.find(substr,curr)
	return loc
# nstrfind

def ListAllSubfolders():
	# Objective: get list of current and all subfolders and return
	import os
	a=[]
	b=os.getcwd();
	for dirpath, dirnames, filenames in os.walk('.'):
		a.append(dirpath.replace('.\\',b+'\\'))
	return a
# ListAllSubfolders

def clear_single():
	'''
	Objective: in current working directory, identify which files are non-
		unique versioned (end with '.1', etc) files and keep only their newest 
		copies. files that are not versioned (eg. '.txt') are not modified.
	'''
	import os
	items = os.listdir('.') # get list of items to compare
	# 1.0 GET LIST OF ITEMS TO KEEP ######################################

	# 1.1 get sublist of only items that have two periods.
	for i in range(len(items)-1,-1,-1):
		if(items[i].count('.')!=2): del items[i]
	# now have list of only items that are "versioned files", possibly with multiples
	# for each item, split first into relevant pieces
	# main name / number / date
	CL=[] # 'CompleteList' ? 
	for i in items:
		dloc=nstrfind(i,'.',2) # find second period location
		CL.append([i[:dloc],i[dloc:],os.path.getmtime(i)])
	# now have Nx3 list of filename, number, and date
	# note: everything automatically in order

	# create UniqueList (precursor to KeepList)
	currentItem=CL[0]
	UL=[]
	UL.append(CL[0]) # initialize with first guess
	for ifile in CL:
		if(UL[-1][0]==ifile[0]): # if file matches same name, choose newer
			if(UL[-1][2]<ifile[2]): # if current file isn't as new as ifile, make it ifile
				UL[-1] = ifile
			# otherwise, move on to next
		elif(ifile[0]!=UL[-1][0]):
			UL.append(ifile)
	# when complete, print list of unique items

	# for i in UL: 
		# print i
	# print str(len(UL))+' unique items'

	# create Keep List
	KL=[]
	for iUL in UL:
		KL.append(iUL[0]+iUL[1])
	# for i in KL:
		# print i
	# have KL, ready to delete files not on 'the list' lol.

	# 2.0 DELETE DUPLICATE ITEMS ######################################### 
	for iCL in CL: 
		item = iCL[0]+iCL[1]
		if(item not in KL):
			os.remove(item)
			print 'deleted: '+item
	print 'deletion complete'
	return 1
# clear_single

def clear_recursive():
	'''
	Objective: Generate a list of current and all subfolders to clear out all 
		non-unique versioned (eg. 'item.prt.1', etc) files. In each folder, run
		function 'clear_single' then move to next folder. When finished, 
		return to orignial top-level folder.
	'''
	import os
	origFolder=os.getcwd()
	folders=ListAllSubfolders()
	for ifolder in folders:
		os.chdir(ifolder)
		clear_single()
	os.chdir(origFolder)
# cler_recursive









