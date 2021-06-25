'''
'''
import os
from klib import getlist
from pprint import pprint
import unittest

class Tests_klib(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        super(Tests_klib, self).__init__(*args, **kwargs)
        pass

    def test__setup(self):
        self.assertTrue(True)
