import Adafruit_BBIO.GPIO as gpio
import time

# avg #####################################################
def avg(xarray):
    # assumes that an array is being passed
    n=len(xarray)
    sumavg=0.0
    for i in range(0,len(xarray)):
        sumavg=sumavg+xarray[i]
    return sumavg/n

# pyt #####################################################
def pyt(a,b):
    return (a*a+b*b)**0.5

# ledINIT #################################################
def ledINIT():
    st='/sys/class/leds/beaglebone:green:usr0/trigger'
    value = open(st,'w')
    value.write(str("none"))
    value.close()

    st='/sys/class/leds/beaglebone:green:usr1/trigger'
    value = open(st,'w')
    value.write(str("none"))
    value.close()

    st='/sys/class/leds/beaglebone:green:usr2/trigger'
    value = open(st,'w')
    value.write(str("none"))
    value.close()

    st='/sys/class/leds/beaglebone:green:usr3/trigger'
    value = open(st,'w')
    value.write(str("cpu0"))
    value.close()

# led #####################################################
def led(which012,bright01):
    st='/sys/class/leds/beaglebone:green:usr0/brightness' #default LED
    if(which012==0):
        st='/sys/class/leds/beaglebone:green:usr0/brightness'
    elif(which012==1):
        st='/sys/class/leds/beaglebone:green:usr1/brightness'
    elif(which012==2):
        st='/sys/class/leds/beaglebone:green:usr2/brightness'
    else:
        print "error"
    #note: leaving 3 to trigger on cpu0, to give status

    value = open(st,'w')
    value.write(str(bright01))
    value.close()

#blink ####################################################
def blink(which012):
    led(which012,1)
    time.sleep(0.1)

    led(which012,0)
    time.sleep(0.1)

    led(which012,1)
    time.sleep(0.2)

    led(which012,0)

# stdev ###################################################
def stdev(xarray):
    n=len(xarray)
    xavg=avg(xarray)
    sumstd=0.0
    for i in range(0,n):
        sumstd=sumstd+(xarray[i]-xavg)**2
    sumstd=sumstd/(float(n)-1.0)
    return sumstd**0.5

# map #####################################################
def map(original,inLow,inHigh,outLow,outHigh):
    m=(outHigh-outLow)/(inLow-outLow)
    b=outHigh-inHigh*m
    return m*original+b

# tooClose ################################################
minDist=17 #cm
def tooClose(cmDistance):
    if(cmDistance<minDist): return 1
    else: return 0

# simpleSolve #############################################
def simpleSolve(kjgFn,yd,xl,xu):
    # use bisection method to do some simple root finding
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
    while (e>1e-10 and i<10000):
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
    return xr
  #def simpleSolve

# slopeLinReg #############################################
def slopeLinReg(xarray,yarray):
    n=len(yarray)
    xavg=avg(xarray)
    yavg=avg(yarray)
    betaC1=range(0,n)
    betaC2=range(0,n)
    for i in range(0,n):
        betaC1[i]=(xarray[i]-xavg)*(yarray[i]-yavg)
        betaC2[i]=(xarray[i]-xavg)**2
    return sum(betaC1)/sum(betaC2) #return lin regression slope, beta

# interceptLinReg #########################################
def interceptLinReg(xarray,yarray):
    beta=slopeLinReg(xarray,yarray)
    xavg=avg(xarray)
    yavg=avg(yarray)
    return yavg-beta*xavg # return lin regression intercept, alpha

# irCalibrate #############################################
def irCalibrate(xarr,yarr):

  def getIRBeta(xarr,yarr):
    for i in range(0,len(xarr)):
      xarr[i]=1.0/(xarr[i]) #REMEMBER TO USE PERIODS FOR NON-INTEGERS
    #get average for beta calc
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
  #def getIRBeta

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
    while (e>1e-10 and i<10000):
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
    return xr
  #def simpleSolve


  beta=getIRBeta(xarr,yarr)
  #print beta

  #gotta start looping here

  b1=1.0
  a=0.0

  #xp=range(0,len(x))
  #for i in range(0,len(x)):
  #  xp[i]=beta*b1/y[i]+a
  ##create xp
  #xd1=xp[1]-x[1]
  #xd2=xp[len(x)]-x[len(x)]

  def f(xx):
    return (beta*xx/yarr[0]-1/xarr[0])-(beta*xx/yarr[len(yarr)-1]-1/xarr[len(yarr)-1])

  b1=simpleSolve(f,0,0,10)
  b=b1*beta
  #print b
  a=1/xarr[0]-b/yarr[0]
  #print a
  for i in range(0,len(xarr)):
    xarr[i]=1.0/(xarr[i]) #REMEMBER TO USE PERIODS FOR NON-INTEGERS


  return (a,b)

# irReadcm ################################################
irReadVarA=-2.1485 #default value
irReadVarB=7.4789 #default value
def irReadcm(adcValue):
    var1=aRead(adcValue)/(1800.0)
    return irReadVarB/(var1+1e-6)+irReadVarA #calibration

# LCDMenu #################################################
def LCDMenu():
    menu0=['1. add','2. cal','3. Run']
    sequ1=['add-N1','add-N2','add-RES']
    sequ2=['sub-N1','sub-N2','sub-RES']
    menu2=['3a. cam','3b. IR']
    sequ3a=['cam s1','cam s2']
    sequ3b=['IR s1','IR s2']

    pinUP = "P8_17"
    pinDN = "P8_18"
    pinYES = "P8_19"


    def userInput():
        notdone=1
        choice=3
        while(notdone):
            if gpio.input(pinUP):
                notdone=0
                choice=0
            if gpio.input(pinDN):
                notdone=0
                choice=1
            if gpio.input(pinYES):
                notdone=0
                choice=2
            time.sleep(.05)
        time.sleep(.2)
        return choice

    def TopMenu():
        user=0  #this will be used for selection
        i=0     #this will be used as menu pointer
        # TopMenu
        while (user!=2):
            print "Top Menu"
            print menu0[i]
            user=userInput()

            # up/down, keep in bounds
            if(user==0):i-=1
            if(user==1):i+=1
            if(i<0):i=len(menu0)-1
            if(i==len(menu0)):i=0
        return i

    def AddSequence():
    # AddSequence
        i=0
        user=0
        n1=0
        while(user!=2):
            # choose n1
            print sequ1[i]
            print n1
            user=userInput()

            # when in sequence, user doesn't choose i
            if(user==0):n1-=1
            if(user==1):n1+=1
        # choose n1

        i+=1
        user=0
        n2=0
        while(user!=2):
            # choose n2
            print sequ1[i]
            print n2
            user=userInput()

            # when in sequence, user doesn't choose i
            if(user==0):n2-=1
            if(user==1):n2+=1
        # choose n2
        i+=1
        print sequ1[i]
        print n1+n2
        userInput()

    def CamCalSequence():
        print "Camera Calibration"
        userInput()

    def IRCalSequence():
        print "IR Calibration"
        userInput()

    def CalMenu():
    # CalibrationMenu
        i=0 #2nd level menu
        user=0 #reset
        while (user!=2):
            print menu0[1]
            print menu2[i]
            user=userInput()

            # up/down, keep in bounds
            if(user==0):i-=1
            if(user==1):i+=1
            if(i<0):i=len(menu2)-1
            if(i==len(menu2)):i=0
        return i

    option=TopMenu() # use as pointer
    if(option==0):
        AddSequence()
    elif(option==1):
        option = CalMenu()
        if(option==0):
            CamCalSequence()
        elif(option==1):
            IRCalSequence()
    elif(option==2):
        print "run robot now!"
        return 1
    else:
        # just end the program
        print "ERROR: option out of bounds, terminating"
        return 1

def analogRead(adcNum):

    path='/sys/devices/ocp.2/helper.14/AIN'
    a=900
    try:
        for i in range(0,4): # try n-times
            f=open(path+str(adcNum))
            a=f.read()
            f.close()
        a=a[0:len(a)-1]
        return int(a)
    except IOError as e:
        # print "kjg: IOError"
        return int(a)

def aRead(adcNum):

    a=0
    k=3
    for i in range(0,2**k):
        a+=analogRead(adcNum)
    a = a >> k
    return a




# end of file #############################################

# def getIR():
# 	Ldist=kj.irReadcm(irLPin)
# 	Mdist=kj.irReadcm(irMPin)
# 	Rdist=kj.irReadcm(irRPin)
# 	return (Ldist,Mdist,Rdist)
#
# def decision(Ldist,Mdist,Rdist):
#
# 	Ldist = kj.tooClose(Ldist)
# 	Mdist = kj.tooClose(Mdist)
# 	Rdist = kj.tooClose(Rdist)
# 	if((not Ldist) and (not Mdist) and (not Rdist)):
# 		# print "fwd" ###
# 		fwd(speed)
# 	elif((not Ldist) and Rdist):
# 		# print "left" ###
# 		left(speed)
# 	elif((not Rdist) and ((not Ldist and Mdist) or (Ldist and not Mdist))):
# 		# print "right" ###
# 		right(speed)
#
# 	elif((Ldist) and ((not Rdist and Mdist) or (Rdist and not Mdist))):
# 		# print "backup, turn" ###
# 		bwd(speed)
# 		sleep(1.5)
# 		right(speed)
# 		sleep(1.5)
# 	else:
# 		# print "backup, 180" ###
# 		bwd(speed)
# 		sleep(1.5)
# 		right(speed)
# 		sleep(1.5)
#
# def fwd(dutyCycle):
# 	# print "fwd"
# 	gpio.output(L1pin,0)
# 	gpio.output(L2pin,1)
# 	gpio.output(R1pin,1) #this makes mR turn clockwise, fwd motion.
# 	gpio.output(R2pin,0)
# 	try:
# 		pwm.set_duty_cycle(LpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
# 	try:
# 		pwm.set_duty_cycle(RpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
#
# def bwd(dutyCycle):
# 	# print "bwd"
# 	gpio.output(L1pin,1)
# 	gpio.output(L2pin,0)
# 	gpio.output(R1pin,0)
# 	gpio.output(R2pin,1)
# 	try:
# 		pwm.set_duty_cycle(LpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
# 	try:
# 		pwm.set_duty_cycle(RpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
#
# def left(dutyCycle):
# 	# will initially do 0-radius turns
# 	# print "left"
# 	gpio.output(L1pin,1)
# 	gpio.output(L2pin,0)
# 	gpio.output(R1pin,1)
# 	gpio.output(R2pin,0)
# 	try:
# 		pwm.set_duty_cycle(LpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
# 	try:
# 		pwm.set_duty_cycle(RpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
#
# def right(dutyCycle):
# 	# will initially do 0-radius turns
# 	# print "right"
# 	gpio.output(L1pin,0)
# 	gpio.output(L2pin,1)
# 	gpio.output(R1pin,0)
# 	gpio.output(R2pin,1)
# 	try:
# 		pwm.set_duty_cycle(LpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
# 	try:
# 		pwm.set_duty_cycle(RpwmPin,dutyCycle)
# 	except IOError as e:
# 		print "KJG: pwm error"
#
# def stop():
# 	# print "stop"
# 	gpio.output(L1pin,1)
# 	gpio.output(L2pin,1)
# 	gpio.output(R1pin,1)
# 	gpio.output(R2pin,1)
# 	try:
# 		pwm.set_duty_cycle(LpwmPin,0)
# 	except IOError as e:
# 		print "KJG: pwm error"
# 	try:
# 		pwm.set_duty_cycle(RpwmPin,0)
# 	except IOError as e:
# 		print "KJG: pwm error"
#
# def pause():
# 	pauseDone=0
# 	stop()
# 	sleep(1)
# 	while(not pauseDone):
# 		print "."
# 		sleep(.2)
# 		if gpio.event_detected(mainPin):
# 			pauseDone=1
# 			print "returning..."
#
# 	sleep(1)





