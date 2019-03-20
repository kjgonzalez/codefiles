'''
Objective: create simple buffer object class that can hold a certain number of 
    things in memory and dump out stuff that at's "end" of buffer. Essentially,
    just want to keep the latest L number of things in memory, and be able to 
    recall them in chronological order
'''

class Buffer:
    ''' Hold L number of things in buffer until needed. return buffer in
        chronological order, "FIFO" 
    EXAMPLE:
        buf=Buffer(4)
        buf.toBuffer('a')
        buf.toBuffer('b')
        buf.toBuffer('c')
        buf.toBuffer('d')
        buf.toBuffer('e')
        buf.getBuffer 
        >> ['b','c','d','e']
    '''
    def __init__(self,length):
        self._L=length
        self._buf=[[i,None] for i in range(length)]
        self._k = 0 # pointer to latest location in buffer
        self._has_reset=False
    # def __init__
    
    def __len__(self):
        ''' return length of buffer, not number of contents held '''
        return self._L

    def toBuffer(self,item):
        ''' put something in buffer, update pointer '''
        self._buf[self._k][1]=item
        self._k+=1
        if(self._k==self._L):
            self._k=0 # reset pointer back
            self._has_reset=True
        return 0 # status that all is ok
    # def toBuffer
    
    def getBuffer(self):
        ''' Return values in buffer (oldest first), ignoring any indices that 
            haven't been written to yet. 
        '''
        if(self._has_reset):
            out=[self._buf[i][1] for i in range(self._k,self._L)]+ \
                [self._buf[i][1] for i in range(0,self._k)]
        else:
            out=[self._buf[i][1] for i in range(0,self._k)]
        return out
    # def buffer
    
    @property
    def length(self):
        ''' return length of buffer, not number of contents held '''
        return self._L
    # def length
# class Buffer

# eof
