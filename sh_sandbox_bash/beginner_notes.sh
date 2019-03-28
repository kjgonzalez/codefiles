# objective: try doing some bash-level logic stuff. try out doing loops, 
#   if-else statements, and functions
# date created: 190326
# author: Kris Gonzalez
# things to try:
#   variables
#   if-else statements
#   loops
#   function declarations
# 
# things to also check
#   modulus check?
#   can bash work with floats?
#   

# first, let's try making a variable =============
var1="test"
var2=true
var3=10
inparg1=$1 # format for i'th command line argument

# next, let's check out if statements ============
echo "variable: $var1"
if [ $var1 = "testt" ]
  then 
    echo "true and false are written like so (A)"
else
    echo "false and true are written like so (B)"
fi

if [ $var3 -gt 5 ] # YOU MUST HAVE SPACE FOR BRACKETS!
  then 
    echo "var3 greater than 5"
elif [ $var3 -eq 5 ]
  then 
    echo "var3 equal to 5"
elif [ $var3 -lt 5 ] 
  then 
    echo "var3 less than 5"
fi

# next, let's do a for loop ======================

cntr=1
while [ $cntr -le 10 ]
do
  echo $cntr
  (($cntr++))
done


# eof

