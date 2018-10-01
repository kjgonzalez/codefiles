# python test

# purpose: attempt to use fuzzy logic

# fuzzification

# settings: 
# VN=25
# N=30
# F=35
# VF=37
# VVF=40


def fuzz(reading,cats):
	n=len(cats)
	fuz=range(n)
	for i in range(n):
		fuz[i]=0
	i=0
	# i is the index of the value that is less than the thing.


	if(reading<=cats[0]):
		# if the thing is less than the first value, then it's 100% the lowest

		fuz[0]=100
		# print "fuz: ",fuz
	elif(reading>=cats[n-1]):
		# if the thing is greater than the last value, then it's 100% the highest
		fuz[n-1]=100
		# print "fuz: ",fuz
	else:
		# if it's in between, then it's either 100% of some value, or some portion of two
		while(i<n):

			if(reading<cats[i]):
				i-=1
				break
			else:
				i+=1

		# print i
		# print cats[i]
		fuz[i+1]=(100-0)/(cats[i+1]-cats[i])*(reading-cats[i])+0
		fuz[i]=100-fuz[i+1]
		# print "%",cats[i],": ",fuz[i]
		# print "%",cats[i+1],": ",fuz[i+1]
		# print "fuz: ",fuz
		# print (cats[i]*fuz[i]+cats[i+1]*fuz[i+1])/100
	return fuz


# inputs and calibrations
L=138
R=123
sCal=[80,100,120,130,140]
# 	 VVF,VF ,F  ,N  ,VN

# fuzzification
Lz=fuzz(L,sCal)
Rz=fuzz(R,sCal)
print L,LFuz
print R,RFuz

	




# fuzz table (operations with fuzzified data)

HR=min()










# reading=26
# ins=[25,30,35,37,40]
# n=len(ins)
# fuz=range(n)
# for i in range(n):
# 	fuz[i]=0
# i=0
# # i is the index of the value that is less than the thing.


# if(reading<=ins[0]):
# 	# if the thing is less than the first value, then it's 100% the lowest

# 	fuz[0]=100
# 	print "fuz: ",fuz
# elif(reading>=ins[n-1]):
# 	# if the thing is greater than the last value, then it's 100% the highest
# 	fuz[n-1]=100
# 	print "fuz: ",fuz
# else:
# 	# if it's in between, then it's either 100% of some value, or some portion of two
# 	while(i<n):

# 		if(reading<ins[i]):
# 			i-=1
# 			break
# 		else:
# 			i+=1

# 	print i
# 	print ins[i]
# 	fuz[i+1]=(100-0)/(ins[i+1]-ins[i])*(reading-ins[i])+0
# 	fuz[i]=100-fuz[i+1]
# 	print "%",ins[i],": ",fuz[i]
# 	print "%",ins[i+1],": ",fuz[i+1]
# 	print (ins[i]*fuz[i]+ins[i+1]*fuz[i+1])/100
# 	print "fuz: ",fuz


