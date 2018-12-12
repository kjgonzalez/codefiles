'''
objective: calculate primes of a given number, and return as a dict where d[prime]=count
'''

from sys import argv
def getprimes(integer):
    assert type(integer)==int, "Given value needs to be an integer"
    curr=int(integer+0)
    div=2
    d={}
    while(curr!=1):
        if(curr%div==0):
            d[div]=d[div]+1 if(div in d.keys()) else 1
            curr=curr/div
        else:
            div+=1
    return d

print(getprimes(int(argv[1])))
