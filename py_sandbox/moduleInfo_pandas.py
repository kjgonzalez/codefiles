'''
dateCreated: 190518
objective: how to make a nice table with pandas from numpy. in this example,
    will generate a dummy table with count & AP values for 9 different classes

KJG190814: perhaps also want to look into how to get a csv file via pandas? 
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

# can read in a file like so:
dat = pd.read_csv('../lib/data/iris.csv',header=None) # if have no header, give "None"
print('iris dataset shape:',dat.shape)

# initialize an empty dataframe and add data later:
# simple method is to initialize with known columns, and add row data later
dat = pd.DataFrame(columns = ['a','b','c'])
dat.loc[0]=[1,2,3]
print(dat)
print('number of rows in table:',len(dat))
print('number of columns in table:',len(dat.columns))
