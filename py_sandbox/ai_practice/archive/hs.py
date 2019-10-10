'''
orig name: heuristicSearch_ch6p3
Author: Kris Gonzalez
Date Created: 180305
Objective: learn how to program heuristic search in python, 
	using Ertel's book. this is to help understand the 
	basics of searching algorithms and AI overall.

overall problem to solve will be looking at the 
	shortest distance to travel between two 
	points on a given map of Oberschwaben, based 
	on Ertel's book

first, will need to setup a small database of 
distances to Ulm. will use all lowercase and 
avoid using umlauts.

connections between cities: 
pathsinfo.csv

distances of each city to ulm: 
ulmdists.csv
'''



# get ulmdist ==============================
f=file('ulmdists.csv')
ulmdist = {}
for row in f:
	a=row.split(',')
	ulmdist[a[0]] = int(a[1])
f.close()
# now have ulmdistances

# get near ==============================
near = {}
f=file('pathsinfo.csv')
for row in f:
	a=row[:-1].split(';')
	near[a[0]] = a[1].split(',')

# now have all data loaded for heuristic search. 
# next, need to be able to pull data based on 
#	some input / state













def nextall(node):
	''' Objective: return available nodes 
		connected to given node.
		want to receive as type: string
		want to return as list of strings
	'''
	return near[node]

def dist(node):
	''' Objective: return the value of the node
		given
	want to receive as type: string
	watn to return as type: int / float
	'''
	return ulmdist[node]

# will start at linz, as shown in figure 6.15
start = ['linz']
start = 'linz'
goal = ['ulm']
goal = 'ulm'

# define how the program searches. based on ertel book, general shape: 
def addnodes(new,old):
	''' Objective: return sorted and combined list of new 
	and old nodes that the algorithm can take. first node must be the 
	best option
	new = result from nextall. must be a list
	old = current list of best paths. must be a list.
	'''
	# create new list to put everything into, and avoid errors
	all=[]
	for i in old:
		all.append(i)
	for i in range(len(new)):
		for j in range(len(all)):
			print dist(new[i]),'vs',dist(all[j])
			if(dist(new[i]) < dist(all[j])):
				all.insert(j,new[i]) # insert this string into place in list
				break;
			elif(j==len(all)-1):
				# have reached the end, this is the worst option
				all.append(new[i])
	# at this point, should have all available nodes
	return all
# def addnodes

def heuristic(start,goal):
	''' Objective: use heuristics to figure out best path to somewhere.
	
	kjgnote: doesn't use recursion like before.
	'''
	nodelist = start
	while True:
		if(nodelist != []):
			# no further steps possible
			print 'heur: no solution'
			return -1
		node = nodelist[0] # first node in list is considered 'best option'
		nodelist=nodelist[1:] # remove current node from list, save others
		if(node == goal):
			# solution found
			print 'heur: solution found'
		# if node isn't solution, add new possibilities to list and reorder
		nodelist = addnodes(nextall(node),nodelist) #need to add function 'addnodes'














