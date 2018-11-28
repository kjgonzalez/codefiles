'''
sets are an unordered collection of unique elements, and basic uses 
    include "membership testing and eliminating duplicate entries"
source:https://docs.python.org/3/library/stdtypes.html#set
'''

A=set('one two three four 5 6 7'.split(' '))
B=set('two four 6 eight 10'.split(' '))

A_only=A-B      # or: A.difference(B)
B_only=B-A

AandB=A-(A-B)   # or: AandB=A.intersection(B)
                # or: AandB=A&B

AorB=A|B        # or: AorB=A.union(B)
