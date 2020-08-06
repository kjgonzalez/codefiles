

# 1. take in data points
# 2. take inverse of distance (cm)
# 3. get slope(measurements, inv_x), multiply times correction
# 4a. to get slope: 
# beta=sum((xi-xavg)*(yi-yavg))/[sum(xi-xavg)]^2
# alpha=yavg-beta*xavg
# 4. 

def avg(xarray):
	# assumes that an array is being passed
	n=len(xarray)
	sumavg=0.0
	for i in range(0,len(xarray)):
		sumavg=sumavg+xarray[i]
	return sumavg/n
def simpleSolve(kjgFn,yd,xl,xu):
	# part of simpleSolve
	def ee1(x,y):
		#choose ee1 if yd==0
		return abs(x)
	#def ee1

	def ee2(x,y):
		#choose ee2 if yd!=0
		return abs((x+0.0)/y)
	#def ee2

	def f2(x):
		return kjgFn(x)-yd +1.0-1.0
	#def f2
	e=1.0;
	i=0;
	xr=0.0
	while (e>1e-10 and i<1e6):
		xr=(xl+xu)/2.0

		if(f2(xl)*f2(xr)<0):
			xu=xr
		else:
			xl=xr
		if(yd==0):
			e=ee1(f2(xr),yd)
		else:
			e=ee2(f2(xr),yd)
		#end ifstatement

		i=i+1 #dont need it yet
	# end whileloop
	return round(xr,9)
def getBeta(xarr,yarr):
	xavg=avg(xarr)
	yavg=avg(yarr)

	#array initalization
	betaC1=range(0,len(yarr))
	betaC2=range(0,len(yarr))

	#get beta
	for i in range(0,len(yarr)):
		betaC1[i]=(xarr[i]-xavg)*(yarr[i]-yavg)
		betaC2[i]=pow((xarr[i]-xavg),2)
	#end forloop

	beta = sum(betaC1)/sum(betaC2)
	return beta
def irCalibrate(xarr,yarr):
	# first, take inverse of cm data
	for i in range(0,len(xarr)):
		xarr[i]=1.0/(xarr[i]) #REMEMBER TO USE PERIODS FOR NON-INTEGERS

	beta=getBeta(xarr,yarr)
	#good up to here
	
	b1=1.0
	a=0.0

	def f(xx):
		return (beta*xx/yarr[0]-1/xarr[0])-(beta*xx/yarr[len(yarr)-1]-1/xarr[len(yarr)-1])


	b1=simpleSolve(f,0,0,10) # simple solve isn't working correctly
	
	# print b1
	b=b1*beta
	# print b
	a=1/xarr[0]-b/yarr[0]
	# print a
	for i in range(0,len(xarr)):
		xarr[i]=1.0/(xarr[i]) #REMEMBER TO USE PERIODS FOR NON-INTEGERS


	return (a,b)
def LoadArray():
	import csv
	i=0
	fileName=raw_input("File (\"filename.csv\"): ")
	button=int(raw_input("press 1 for comma separated values \
		\npress 2 for tab separated values \nSelection: "))
	if(button==1):
		delim=','
	elif(button==2):
		delim='\t'
	with open(fileName,'rb') as f:
		liner=csv.reader(f,delimiter=delim)
		for row in liner:
			i+=1

	# create appropriately lengthed array
	# print "No. Rows: ",i
	a=range(0,i)
	b=range(0,i)
	i=0
	# open file again, load with appropriate length array
	with open(fileName,'rb') as f:
		liner=csv.reader(f,delimiter=delim)
		for row in liner:
			a[i],b[i]=float(row[0]),float(row[1])
			# print a[i],"\t",b[i]
			i+=1
	return a,b

(ar1,ar2)=LoadArray()


if(len(ar1)==len(ar2)):
	print 
	print "a,b:"
	print irCalibrate(ar1,ar2)