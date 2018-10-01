# objective: try to get rid of page numbers that randomly get put into text
# UPDATE: code works, currently works on hunger games series of books


# get file to modify
a=raw_input("Enter in book name, including *.txt: ")
# a='sample.txt' #debugging
temp='temp.txt' #create "temp" file

# open/create up both files first time
book=open(a)
f=file(temp,'w')

# find and remove all pg numbers, save to temp
i=0;
for row in book:
	try: 
		numTest=int(row)
	except: 
		numTest=0
	if(len(row)<6 and len(row)!=1 and numTest>0):
		i+=1
	else:
		f.write(row)
# main forloop
book.close();
f.close()

# remove previous content / file length of original file
f=open(a,'w')
f.write("haha")
f.close();

# truly add in changes to new file. 
book=open(temp)
f=open(a,'w')
for row in book:
	f.write(row)
f.close()
book.close()

# it ain't pretty, but it gets the job done.
 
print "done, ", i, "page numbers found"