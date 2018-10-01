
# purpose: read in file and find smallest minimum wage of state

'''
1. load file
2. find line that starts with '$'
3. return value to array
4. print out maximum value of array

'''
# load file, check number of lines
f=open('minimumWages.txt')
i=0;
for row in f:
	if(row[0]=='$'):
		# ll[i]=float(row[1:5])
		i+=1
f.close()

# reload file, with known number of lines
# find lines that start with '$'
# return to array, print out the max
ll=range(0,i)
f=open('minimumWages.txt')
i=0;
for row in f:
	if(row[0]=='$'):
		ll[i]=float(row[1:5])
		i+=1

f.close()

print max(ll)

