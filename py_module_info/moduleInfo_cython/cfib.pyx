def fib(n):
    # return all fibonacci numbers up to n
    a,b = 0,1
    fibs = [b]
    while(b<n):
        a,b=b,b+a
        fibs.append(b)
    return fibs