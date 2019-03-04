= 190302 =======================================================================
have reached pg 158, have been able to actually train the network on an image, 
    and must now iterate through entire database and then test network.
    
= 190302 =======================================================================
have reached page 143, now moving on to the mnist database.
note: although have downloaded the 100-value mnist example, must also create 
    helper function that can convert the labels into correct format (10-value 
    array) and actual images into a numpy array (reshape the flattened array)


= 190213 =======================================================================
have reached Part 2, pg ~139, working to create own network


kjgnote: simple normalization works best, probably least computationally
	expensive as well. if norm1=(x-avg)/std and norm2=(x-xmin)/(xmax-xmin)-0.5, then
	they're both linearly scaling the data nearly identically, just to different
	scales.
= 190211 =======================================================================
at about page 99, and have been able to work out the error update equation. next
	is to actually implement it.
= 190210 =======================================================================
at about page 97. 
to use gradient descent, need to use calculus to find slope of error function 
	wrt weights

= 190205 =======================================================================
working on next section, backpropagation. got to pg 78. use comp notebook as
    companion

= 190204 =======================================================================
as of "today", have covered up to page 70
