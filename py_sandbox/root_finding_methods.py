'''
date: 190509
objective: use a root finding method to find a desired value. in this file, will
    simply cover bisection and newton methods

'''

def root_bisection(function,yValue,lims,eps=1e-6,maxit=10000):
    ''' find xValue where function is equal to yValue, or f(x)=y
    INPUTS:
        * function: lambda function. single-value function, ideally obeys
            vertical rule (one y-value per x-value)
        * yValue: scalar float. solve where function is equal to yValue
        * lims: 2-scalar list. [xLower,xUpper] describing bounds of
            search space
        * eps: maximum allowable error
        * maxit: max number of iterations before giving up
    OUTPUT:
        * value of x at yValue
    '''
    # want to minimize this function
    g=lambda x:function(x)-yValue

    xL=lims[0]
    xU=lims[1]
    gval=eps*2
    iter=0
    while(iter<maxit and abs(gval)>eps):
        xC=(xL+xU)/2
        gval=g(xC)
        if(gval*g(xL)>0): xL=xC
        else: xU=xC
        iter+=1
    return xC,iter,gval+yValue

def root_newton(function,yValue,start_point,eps=1e-6,maxit=10000):
    ''' find xValue where function is equal to yValue, using newton method
    INPUTS:
        * function: lambda function. single-value function, ideally obeys
            vertical rule (one y-value per x-value)
        * yValue: scalar float. solve where function is equal to yValue
        * start_point: initial guess to begin solving from.
        * eps: maximum allowable error
        * maxit: max number of iterations before giving up
    OUTPUT:
        * value of x at yValue
    '''
    g=lambda x:function(x)-yValue
    x=start_point+0
    dfdx=lambda x:(function(x+1e-5)-function(x-1e-5)) / (2e-5) # centered
    gval=g(x)
    iter=0
    while(iter<maxit and abs(gval)>eps):
        x=x-g(x)/(dfdx(x)+1e-5)
        gval=g(x)
        iter+=1
    return x,iter,gval+yValue

print('Will solve for x in f(x)=x^2-2 with two different solvers')
print()
fn = lambda x: x**2-2
ydes=4

print('using bisection method:'+'='*10)
result=root_bisection(fn,ydes,[0,3])
print('answer: {} | No.Iterations: {} | approximation: {}'.format(*result))
print()

print('using newton method:'+'='*10)
result=root_newton(fn,ydes,5)
print('answer: {} | No.Iterations: {} | approximation: {}'.format(*result))
