import sys
sys.path.append('../webCalReader/')

from nose.tools import *
import unittest
import webcalreader
#import urllib2

class WebCalReaderTests(unittest.TestCase):
    def basicTest(selfself):
        print ("what?")
        webcalreader.webCalReader()
