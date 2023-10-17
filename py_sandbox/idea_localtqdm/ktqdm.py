'''
objective: lazy, kjg-specific tqdm that outputs only on multiples of 10%
'''
import sys
import time

def reprint(text):
    sys.stdout.write('\r'+text)

class Ktqdm:
    def __init__(self,iterobj):
        self.obj = iter(iterobj)
        self.havemaxit=hasattr(iterobj,'__len__')
        self.maxit = len(iterobj) if(self.havemaxit) else Nonea
        self.maxfmt = len(str(self.maxit))
        self.i = 0
        self.t0=None
        self.nextgoal=0.1

    def printoverwrite(self,text):
        pass # todo: able to overwrite previous print

    def __iter__(self):
        self.t0=time.time()
        self.nextgoal=0.1
        # print('iter')
        #print('')
        return self

    def __next__(self):
        if(self.havemaxit):
            if(self.i/self.maxit >= self.nextgoal):
                # estimate remaining time
                el = time.time()-self.t0
                tot = el*self.maxit/self.i
                pct = round(self.i/self.maxit*100)
                reprint(f'{self.i:0>{self.maxfmt}}/' + 
                        f'{self.maxit} ({el:0.2f}/{tot:0.2f} s) {pct:>3}%')
                if(pct>=100): 
                    print('')
                self.nextgoal+=0.1
        else:
            reprint(f'{self.i} ({time.time()-self.t0:0.2f} s) / nothing')
        self.i+=1
        return next(self.obj)
    #def __del__(self):
    #    print('here')
        

if(__name__ == '__main__'):
    obj = Ktqdm(range(732))
    # print('other thing')
    for i in obj:
        time.sleep(0.00251)
    print('done')


# eof

