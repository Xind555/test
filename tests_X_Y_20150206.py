#!/usr/local/bin/python3


import unittest
import operator

from code import Math


class MyTest(unittest.TestCase):


	def setUp(self):
		self.session = 'foobar'

	def tearDown(self):
		self.session = None

	def test_foo(self):	
		a = 1
		self.assertEqual(a, 1)

	def test_bar(self):
		"""test_bar"""		
		b = 'data' + self.session
		self.assertEqual(b, 'datafoobar')

	def test_sum(self):  
		"""Check is sum method is equivalent to operator"""
		self.assertEqual(Math.sum(self, 1,1), 2)



if __name__ == "__main__":
	unittest.main()

