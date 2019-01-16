'''
Objective: this file serves as the test module for the other library module, and
    will thus import the other module to be used here.

See module_lib.py for more information
'''

import module_lib as l



def test_pyt():
    assert l.pyt([3,4,12]) == 13

def test_pyt2():
    assert l.pyt([4,4]) == 4*2**0.5

def test_area():
    assert l.area_rect(-10,-10) == 100

def test_area2():
    assert l.area_rect(34,10) == 340

def test_fail():
    assert l.area_rect(3,4) == 14
