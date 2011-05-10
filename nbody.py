#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
        
class Test:
    def test1(self):
        a = Body(name='bob',y=2,mass=3)
        print a
    def test2(self):
        a = Body(name='bob',y=2,mass=3)
        b = Body(name='jill',x=-1,mass=2)
        print a
        print b
    def test3(self):
        a = Body(name='bob',y=2,mass=3)
        b = Body(name='jill',x=-1,vy = 1,mass=2)
        sys = System(bodies=[a, b],name='world')
        print sys
    def test4(self):
        a = System(n=2,name='world')
        print a
    def test5(self):
        a = Body(-1,name='bob')
        b = Body(1,name='jill')
        sys = System(bodies=[a, b],name='world')
        print sys
        sys.step(0.5)
        print sys
        


a = Test()
a.test5()
