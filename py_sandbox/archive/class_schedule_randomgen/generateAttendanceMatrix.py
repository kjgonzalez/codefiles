'''
Author: Kristian Gonzalez
DateCreated: 180322
Objective: Output a randomly generated attendance matrix 
    file of experiment / group attendance times.
* rule 1: each team must be present in every column
* rule 2: each row must have a set of unique teams

NOTE: script will overwrite old files with the same name.
'''

# CONTROL SECTION ##########################################
nGroups = 12
nExperiments = 5
# note: nWeeks = nGroups
fileout='out.csv'
itmax=100 #maximum attempts to build a valid matrix

# CONTROL SECTION END ######################################

# initializations
import random

# note: refer to a specific point as mat[row][col], 0-index
# note: row = week, col = experiment

# generate necessary functions
def getCol(matrix,desCol):
    return [matrix[i][desCol] for i in range(len(matrix))]

def getRow(matrix,desRow):
    return matrix[desRow]

def uniqueRowCheck(mat):
    ''' objective: check that each row has a unique set of elements
    '''
    for irow in mat:
        for icol in irow:
            if(irow.count(icol) > 1):
                return False
    return True

def uniqueColCheck(mat):
    ''' objective: check that each column has unique elements
    '''
    for i in range(len(mat[0])):
        icol=getCol(mat,i)
        for irow in icol:
            if(icol.count(irow) > 1):
                return False
    return True

def inRC(value,matrix,row,col):
    # return true/false if a value is in row or column
    if(value in getRow(matrix,row) or value in getCol(matrix,col)):
        return True
    else:
        return False

def getsubpool(pool,matrix,row,col):
    subpool=[]
    for i in pool:
        if(not inRC(i,matrix,row,col)):
            subpool.append(i)
    return subpool

def genMatrix(nGroups,nExperiments):
    '''
    general steps:
    1. generate pool of group numbers and empty matrix
    2. remove all values that are in row or column
    3. add random element
    '''
    # first, will generate an empty matrix that only outputs zeroes
    mat = [[0 for ex in range(nExperiments)] for wks in range(nGroups)]
    # if want to write col-by-col
    pool = range(1,nGroups+1)
    for icol in range(len(mat[0])):
        # in each new column, generate new set of values
        for irow in range(len(mat)):
            subpool = getsubpool(pool,mat,irow,icol)
            # insert value into each element
            elem=random.sample(subpool,1)[0]
            mat[irow][icol] = elem
    # col style
    return mat

# attempt to generate matrix, 
tryAgain=True
it=0
mat=[]
while(tryAgain and it<itmax):
    it=it+1
    try:
        mat=genMatrix(nGroups,nExperiments)
        tryAgain = False
        print('solved')
    except ValueError:
        print('didn\'t work')

# Once complete, display results
for irow in mat:
    print(irow)
print('all rows with unique elements?',uniqueRowCheck(mat))
print('all cols with unique elements?',uniqueColCheck(mat))

# export matrix as csv file
f = open(fileout,'w')
a = [str(i+1) for i in range(nExperiments)]
firstline='...,Exp'+',Exp'.join(a)+'\n'
f.write(firstline)
i=0
for iweek in mat:
    i=i+1
    iweek = [str(col) for col in iweek]
    a=','.join(iweek)
    f.write('week'+str(i)+','+a+'\n')
f.close()

print('done')
