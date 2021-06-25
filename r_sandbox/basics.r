# The Basics of R =========================================
# topics to cover: 
  # make a variable
  # math operations
  # logic operations
  # typical builtins
  # make a function
  # if-else statements
  # forloops, whileloops
  # file manipulation

# make a variable ======================
# two primitive types of variables: numeric (double) & strings (character)

# numeric / double
a = 1 # note: although "<-" is standard, "=" can be more convenient
b = 2
print(a+b)
print(paste('sum: ',a+b))

# character / strings
c = "some string"
print(c)

# lists
d = c(1,2,3,4)
print(d)


# math operations ======================
# sum, sub, mult, div, pow, modulus
print(1+1-2*3/3+5**2 - 7%%2) # note: sqrt is also a builtin

# logic operations =====================
print(TRUE == TRUE)
print(TRUE != F) # note, F & T can replace TRUE & FALSE
print(2 > 1)
print(2<=2)

# typical builtins =====================
print('print what you have') # note: in R, ' is also valid
c(1,2,3) # combine multiple values to create a list, single type
length(3) # length of an object's "first" dimension
typeof(3) # type of an object
print(paste(1,2)) # join two strings, converting things that aren't strings


# make a function ======================
pyt = function(a,b=4){
  return ((a*a+b*b)**0.5)
}
print(pyt(3,4))

# if-else statements ===================
a = 5
if(a<2) {
  print('less than 2')
} else if(a>10) {
   print('greater than 10')
} else{
   print('between 2 and 10, inclusive')
 }

# for-loops ============================
for(i in 1:5){
  print(paste('loop:',i))
}


# while loops ==========================
b = 10
while(b>0){
  print(paste("curr value:",b))
  b = b-2
}

# filesystem manipulation ====================
# is path a folder, does it exist, rename a file, get list of folders
getwd() # get working directory
file.path('a','b','c') # concatenate filepaths
dir.exists('.') # check that a directory exists
dir.create('delme') # create a folder
list.files() # list files / directories in a folder
# ??? how to delete a file / folder

# working with dataframes ====================

# create a dataframe


SAFE = c('a','b','c','d')

testArchives = c()
testR10s = c()
testTCIs = c()

for(iarchive in SAFE){
  testArchives = append(testArchives,existsArchive(...))
  testR10s = append(testR10s,existsR10(...))
  testTCIs = append(testTCIs,existsTCI(...))
}

write.csv(cbind(SAFE,testArchives,testR10s,testTCIs),
          "SAFE_check.csv")











