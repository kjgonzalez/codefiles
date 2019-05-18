'''
dateCreated: 190518
objective: how to make a nice table with pandas from numpy. in this example,
    will generate a dummy table with count & AP values for 9 different classes
'''


import numpy as np
import pandas as pd

names='car cyc dc misc ped sitting tram truck van'.split(' ')
vals1= np.array(np.random.rand(9)*100+10,int)
vals2 = np.array([0.8, 0.7, 0.4, 0.8, 0.7, 0.5, 0.8, 0.9, 0.8])
vals= np.column_stack((vals1,vals2))

table=pd.DataFrame(data=vals,index=names,columns=['count','AP'])
print(table)
# sample=[['Car']]
