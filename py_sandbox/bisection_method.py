''' 
date: 190509
objective: use a root finding method to find a desired value. '''


def root_bisection(function,yValue,lims,eps=1e-6,maxit=10000):
    ''' find xValue where function is equal to yValue, or f(x)=y 
    INPUTS:
        * function: lambda function. single-value function, ideally obeys 
            vertical rule (one y-value per x-value)
        * yValue: scalar float. solve where function is equal to yValue
        * lims: 2-scalar list. [xLower,xUpper] describing bounds of 
            search space
    '''
    # want to minimize this function
    f=lambda x:function(x)-yValue
    
    xL=lims[0]
    xU=lims[1]
    yC=eps*2
    iter=0
    while(iter<maxit and abs(yC)>eps):
        xC=(xL+xU)/2
        yC=f(xC)
        if(yC*f(xL)>0): xL=xC
        else: xU=xC
        iter+=1
    return xC
fn = lambda x: x**2-2
xtemp=root_bisection(fn,4,[0,3],maxit=100)

ytemp=fn(xtemp)

print(xtemp,ytemp)


