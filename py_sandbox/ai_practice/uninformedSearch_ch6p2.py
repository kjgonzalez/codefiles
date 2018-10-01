'''
Author: Kris Gonzalez
Date Created: 180305
Objective: learn how to program a breadth first 
	search in python, using Ertel's book. this 
	will help you understand the basics of 
	searching algorithms.

'''

# so, will first focus on building a space where 
	# the search will need to happen.
from time import time as tcurrent
def getOrig():
	return [[1,0,2],[4,5,3],[7,8,6]]
# get original puzzle start
def getAns():
	return [[1,2,3],[4,5,6],[7,8,0]]
# get original ordered answer
def genp(n=3):
	''' Generate a random NxN puzzle. This puzzle is 
		deterministic and observable to the computer.
	'''
	pool=range(0,n*n+1)
	out=[]
	temp=[]
	from random import random as r
	# part 1: scramble number order and get list
	m=n*n-1
	for i in range(n*n+1):
		# make an index. append. remove from list. repeat
		pos = int(round(r()*m))
		temp.append(pool[pos])
		del pool[pos]
		m=m-1
	# part 2: put all numbers in array
	for i in range(0,n):
		out.append(temp[i*n:i*n+n])
	return out

def disp(puzzle):
	for i in puzzle:
		print i
# disp

def shift(puzzle,d):
	''' Given a specific puzzle, shift (switch) one piece 
		with another piece. the '0' value is always 
		considered a blank space, and is the only one 
		that may switch with another, adjacent piece.
		p = puzzle
		d = direction
		
	'''
	# first, find location of zero
	#from copy import copy
	#p=copy(puzzle) # simply and prevent overwriting (?) may need 'copy'
	p=[]
	for i in puzzle:
		row=[]
		for j in i:
			row.append(j)
		p.append(row)
	
	for irow in range(len(p)):
		for icol in range(len(p[irow])):
			#print p[irow][icol]
			if(p[irow][icol] == 0):
				r0=irow;c0=icol
	
	# once found, determine if shift is valid
	# KJGNOTE: 0=right, 1 = up, 2 = left, 3 = down
	# bounds: col/row: [0,n]
	# print '0:', r0,c0
	r1=r0
	c1=c0
	if(d==0):
		# want to go right
		c1=c0+1
		if(c1>len(p)-1): return -1
	elif(d==1):
		# want to go up
		r1=r0-1
		if(r1<0): return -1
	elif(d==2):
		# want to go left
		c1=c0-1
		if(c1<0): return -1
	elif(d==3):
		# want to go down
		r1=r1+1
		if(r1>len(p)-1): return -1
	else:
		return -1 #error

	# print '1:', r1,c1
	
	#r1=len(p)-1 #temp
	#c1=len(p)-1
	#once switch is determined valid, switch
	temp=p[r0][c0]
	p[r0][c0] = p[r1][c1]
	p[r1][c1]=temp
	#print p
	return p
# def shift

def nextall(current):
	''' Objective: list all possible successors to current 
		state of puzzle. saves trouble of having to write 
		this each search. currently part of bfs. this function
		serves as the equivalent for ertel's "successors" 
		function.
		current: current state of puzzle
	'''
	nextlist = [] # start empty
	for i in range(0,4): #need to test all 4 directions
		test=shift(current,i)
		if(test != -1):
			# print 'i:',i
			# disp(test)
			nextlist.append(test)
		# else: print 'direction',i,'denied'
	return nextlist
# def nextall


# quickDebug ===============================================
# a=getOrig()
# disp(a)
# print nextall(a)

'''
with the above functions, can now proceed to creating code that will
	automatically solve the puzzle. will start with breath first
	search

KJGNOTE: it seems like BreadthFirstSearch (BFS) calls itself, and therefore is recursive...

general structure, per ertel book: 

bfs(nodelist,goal)
newnodes = <empty>
for all nodes member of node list
	if goalreached(node, goal)
		return ("solution found", node)
	new nodes = append(newnodes, successors(node))
if new nodes != <empty>
	return bfs(newnodes,goal)
else
	return (nosolution)
'''


def bfs(nodelist,goal):
	''' Objective: perform breadth-first-search on 3x3 puzzle.
		eventually, maybe can expand to other puzzle sizes.
	nodeList: for user, this is 1st, current state of item. within 
		self-calls, this is the growing list of possible states
	goal: this is the answer (for 3x3, ordered from 1-8, starting
		at top left: [[1,2,3],[4,5,6],[7,8,0]]
	
	NOTE: this algorithm does not prevent cycling, meaning there
		can be infinitely long branches.
		'''
	newnodes = []
	for node in nodelist: 
		if(node == goal): # "GoalReached"
			print 'bfs: solution found!'
			return node
		for inode in nextall(node):
			newnodes.append(inode)
	if(newnodes != []):
		# print 'next set for call:'
		# print newnodes
		print 'length of next list: ',len(newnodes)
		return bfs(newnodes,goal)
	else:
		print 'bfs: no solution'
		return -1

print '============================'
print 'breadth-first search'
goal = getAns()
start = getOrig()
# KJGNOTE: DO NOT RUN THIS WITH RANDOM LIST. IT DOES NOT FINISH.
print 'orig: ',start
# print goal
a=tcurrent()
print bfs([start],goal)
print 'elapsed time [ms]:',(tcurrent()-a)*1000

# next: depth-first search
def dfs(node,goal,it=0):
	'''
	KJGNOTE: THIS FUNCTION ONLY EXISTS AS AN EXAMPLE TO 
		HOW IT WOULD BE PROGRAMMED. PRACTICALLY SPEAKING, IT IS NOT 
		USUALLY FEASIBLE.
	'''
	print 'DO NOT RUN ME'
	return -1 
	maxit=100
	if(node == goal): # "Goal Reached"
		print 'dfs: solution found!'
		return node
	elif(it>maxit):
		print 'no solution'
		return -1
	newnodes = nextall(node)
	i = 0
	while (newnodes != []):
		print 'going to next level.'
		it=it+1
		ans=dfs(newnodes[i],goal,it)
		if(ans==goal): 
			return ans
		i=i+1
	print 'dfs: no solution'
	return -1


print '============================'
print 'depth-first search'
goal = getAns()
start = getOrig()
print 'orig: ',start
# print goal
a=tcurrent()
print dfs(start,goal)
print 'elapsed time [ms]:',(tcurrent()-a)*1000

def itde(node,goal):
	''' Objective: will perform dfs, but modified so as 
		to allow only searching to a specific depth. will 
		create entirely new dfs function, dfs_b. 'itde'
		function stands for "iterative deepening"
	'''
	depthlimit=0
	havesolution=False
	while(not havesolution):
		havesolution = dfs_b(node,goal,0,depthlimit)
		depthlimit=depthlimit+1
	# print 'have solution?'
	return havesolution
# def itde

def dfs_b(node,goal,depth,limit):
	''' Objective: perform depth-first-search, but with 
		a depth limit.
	'''
	if (node == goal):
		# solution found
		print 'dfs_b: solution found!'
		print node
		return True
	newnodes = nextall(node)
	i=0 # check each branch
	while(newnodes!=[] and depth < limit and i<len(newnodes)):
		result = dfs_b(newnodes[i],goal,depth+1,limit)
		if(result==True):
			# solution found?
			return True
		i=i+1
	# print 'dfs_b: no solution'
	return False
	
# dfs_b
print '\n\n\n\n\n\n'
print '============================'
print 'ID_dfs'
goal = getAns()
start = getOrig()
start = genp()
print 'orig: ',start
# print goal
a=tcurrent()
print itde(start,goal)
print 'elapsed time [ms]:',(tcurrent()-a)*1000



