#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

##nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests --cover-tests --cover-xml

import unittest
from code import Math


class MyTest(unittest.TestCase):


	def setUp(self):
		self.session = 'foobar'

	def tearDown(self):
		self.session = None

	def test_foo(self):	
		"""test_foo"""			
		a = 1
		self.assertEqual(a, 1)

	def test_bar(self):
		"""test_bar"""		
		b = 'data' + self.session
		self.assertEqual(b, 'datafoobar')

	def test_sum(self):  
		"""Check is sum method is equivalent to operator"""
		x = Math.sum(self, 1,1)
		self.assertEqual(x, 2)



if __name__ == "__main__":
	unittest.main()

