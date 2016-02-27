import sys
sys.path.append('../main/')

from nose.tools import *
import unittest
import main

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP!")

    def tearDown(self):
        print("TEAR DOWN!")
    
    def test(self):
        self.assertEqual(fun(3), 4)

    def testfail(self):
        self.assertEqual(fun(3), 5)

    def test_basic(self):
        print("I RAN!")
        main.IceCubeGameScheduleDataCollector()
        #main.blah()
