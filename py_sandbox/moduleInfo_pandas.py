'''
dateCreated: 190518
objective: how to make a nice table with pandas from numpy. in this example,
    will generate a dummy table with count & AP values for 9 different classes

KJG190814: perhaps also want to look into how to get a csv file via pandas? 
'''


import numpy as np
import pandas as pd
import tempfile as tmp

names='car cyc dc misc ped sitting tram truck van'.split(' ')
vals1= np.array(np.random.rand(9)*100+10,int)
vals2 = np.array([0.8, 0.7, 0.4, 0.8, 0.7, 0.5, 0.8, 0.9, 0.8])
vals= np.column_stack((vals1,vals2))

# basic initialization
table=pd.DataFrame(data=vals,index=names,columns=['count','AP'])
print(table)
# sample=[['Car']]

# write out a file like so:
f = tmp.NamedTemporaryFile(mode='w',suffix='.csv',delete=False)
fname = f.name
pd.DataFrame(np.random.rand(3,3),columns=list('abc')).to_csv(f)
f.close()

# can read in a file like so:
dat = pd.read_csv(fname,header=None) # if have no header, give "None"
print('shape:',dat.shape)

# initialize an empty dataframe and add data later:
# simple method is to initialize with known columns, and add row data later
dat = pd.DataFrame(columns = ['a','b','c'])
dat.loc[0]=[1,2,3]
print(dat)
print('number of rows in table:',len(dat))
print('number of columns in table:',len(dat.columns))

# add a column or row to a dataframe: 
df = pd.DataFrame(np.random.rand(3,3),columns=list('abc'))
df['d']=[1,2,3]
df.loc[len(df)] = np.arange(df.shape[1])
print(df)

# merge two tables in various ways
x = pd.DataFrame(np.ones((4,4)),columns=list('abcd'))
y = pd.DataFrame(np.zeros((4,4)),columns=list('abce'))
# merge 1: append to the end
z = pd.merge(x,y,how='outer')
print('merge1:\n',z,sep='')
# merge 2: merge on specific column
z = pd.merge(x,y,how='outer',on=['a'])
print('merge2:\n',z,sep='')

# select a subset of data
x = pd.DataFrame({'name':['a']*5+['b']*5, 'dat':np.random.rand(10)})
print(x)
print('rows with "a" in them:')
print( x[x['name']=='a'] )

# sort a dataframe by a given column
# NOTE: can have a list of sorting priority (sort by column a, then column b, then...)
print('unsorted')
arr = (np.random.rand(3,4)*100).round().astype(int)
x = pd.DataFrame(arr,columns=list('abcd'))
print(x)
print('sorted ascending by column b')
x2 = x.sort_values(by=['b'],inplace=False) # "inplace" prevents having to make a new array
print(x2)

print('sorted descending by column c')
x3 = x.sort_values(by=['c'],ascending=False)
print(x3)

# drop a row or a column from the data
x = pd.DataFrame(np.random.rand(3,3),columns=list('abc'))
print('dropping rows columns')
# drop a column
print('original\n{}'.format(x))
print('drop a column:\n{}'.format( x.drop(['a'],axis=1) ))
print('drop a row:\n{}'.format( x.drop([0]) ))

# NOTE: the indices are preserved during these operations, so you need "reset_index" to reset these values
print('drop a row and use new indices:\n{}'.format( x.drop([0]).reset_index(drop=True) ))

# swap two columns around (note: not really that convenient)
print('swapping columns around:\n{}'.format(x.reindex(columns=['b','a','c'])))

print('alternative method:\n{}'.format( x[['b','a','c']] ))