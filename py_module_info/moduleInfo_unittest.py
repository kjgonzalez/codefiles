'''
Start creating basic example of making unittests in python. typically accessed
  via pycharm, but also usable in command line


Important unit test concepts: 
"test ..."
* fixture: prep needed to perform testing (e.g. temp db's, directories, etc) 
* case: individual unit of testing, represented as a function of class TestCase
* suite: collection of test cases / suites, aggregate tests to run together
* runner: orchestrate execution of tests. can be graphical, textual, etc


USAGE 1 (if have __main__ call): 
    python moduleInfo_unittest.py -v

USAGE 2 (typical):
    python -m unittest moduleInfo_unittest.py -v

USAGE 3 (if have some structure and numerous tests):
    python -m unittest discover <args>

EXAMPLE OUTPUT:
test_Blah (__main__.TestExample) ... ok
test_add1 (__main__.TestExample) ... ok
test_pyt (__main__.TestExample) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK

'''

import unittest


# define some basic functions
def add1(x):
    return x+1
def pyt(x,y):
    return (x*x+y*y)**0.5
class Blah:
    def __init__(self,k:int):
        self.k = k
    @property
    def plus1(self):
        return self.k+1
    @staticmethod
    def add2(x):
        return x+2

class TestExample(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        super(TestExample,self).__init__(*args,**kwargs)
        # NOTE: overriding __init__ is optional, only if you want some kind of
        # data / information accessible everywhere
    
    def test_add1(self):
        self.assertTrue( add1(2) == 3)
        self.assertTrue( add1(-1) == 0)
    
    def test_pyt(self):
        self.assertTrue( pyt(3,4) == 5.0)
        self.assertTrue( pyt(-5,12) == 13.0)
    
    def test_Blah(self):
        self.assertTrue( Blah.add2(0) == 2)
        b = Blah(3)
        self.assertTrue( b.plus1 == 4)

#if __name__ =='__main__':
#    # NOTE: if you have some kind of continuous integration (CI) built
#    # into your repo, this may not be necessary
#    unittest.main()
