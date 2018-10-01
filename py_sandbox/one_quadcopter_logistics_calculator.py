#Run Logistics Calculator

# 1. setup points table
# 2. perform boulder-rock-sand fill up for first "run"
# 	a. get biggest item, add to cart, subtract from count
# 	b. get next biggest item, add to cart, subtract from count
# 	c. when full, calculate number of times able to perform "run"
# 3. repeat
capacityComparison=range(0)

for j in range(2100,5500,200):
	C = j #g, carrying capacity of quadcopter
	# make list / table of items
	bottle=[
	#name /wt /pts/qty
	['2L', 2000, 7,4],
	['1L', 1000, 5,6],
	['500mL',500,4,8],
	['12oz', 341,3,10],
	['8oz',227,2,15]
	]

	# make some "constants"
	NM=0; WT=1; PTS=2; QTY=3;

	n=len(bottle)
	# for i in range(n):
	# 	print bottle[i]

	# initialize counter for overall iterative process
	qtyCount=range(n)
	basketCount=range(n)
	for i in range(n):
		qtyCount[i]=bottle[i][QTY]
	runsList=range(0)
	RunTotal=0

	# print "Start"
	while(max(qtyCount)>0):
		# calculate a run:
		for i in range(n):
			basketCount[i]=0
		Crun=C; #initialize current "basket"
		basketList=range(0) #initialize basketList var
		basketPts=0
		
		# print Crun, qtyCount, basketList
		#start of looping
		i=0
		while(i<5):
			#if basket can hold certain bottle, and there's still 
			#more to grab of that bottle...
			if(Crun>bottle[i][WT] and qtyCount[i]>0):
				Crun=Crun-bottle[i][WT] # subtract weight from capacity
				qtyCount[i]-=1 # reduce count of item to zero
				basketCount[i]+=1 #increase count in basket
				basketList.append(bottle[i][NM])
				basketPts+=bottle[i][PTS]
			else: 
				i=i+1
			# print i
		# print Crun
		# print qtyCount, basketCount
		# print basketList
		runNo=1
		#now test how many times that particular run can be 
		# done, and subtract from qtyCount

		while (i<1000):
			test=range(n)
			for i in range(n):
				test[i]=qtyCount[i]-basketCount[i]
			if(min(test)>=0):
				#this means that all values zero or greater, 
				# may decrease qtyCount overall
				for i in range(n):
					qtyCount[i]-=basketCount[i]
				runNo+=1
			else: 
				i=2000
		# print runNo
		# print qtyCount
		RunTotal+=runNo
		runsList.append([runNo,basketPts, C-Crun, basketList])

		# at this point, now know runNo, basketList, and qtyCount (remaining)
		# do all ths again until max(qtyCount)=0
	# print 'done'
	sum=0
	# print "RunNo | basketPts | basketWt | basketList"
	# for i in range(len(runsList)):
	# 	print runsList[i]
	# 	# sum+=runsList[i][0]*runsList[i][1]
	capacityComparison.append([C, RunTotal])
for i in range(len(capacityComparison)):
	print capacityComparison[i]
