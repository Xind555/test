#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""bla"""

#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-tests --cover-xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests --cover-tests --cover-xml

import unittest
from code import Math

class MyTest(unittest.TestCase):
	"""bla"""
	
	def setUp(self):
		self.session = 'foobar'
	
	def tearDown(self):
		self.session = None
	
	def test_foo(self):
		"""test_foo"""
		var = 1
		self.assertEqual(var, 1)
	
	def test_bar(self):
		"""test_bar"""		
		var = 'data' + self.session
		self.assertEqual(var, 'datafoobar')
	
	def test_sum(self):
		"""Check is sum method is equivalent to operator"""
		var = Math.sum(1,1)
		self.assertEqual(var, 2)

if __name__ == "__main__":
	unittest.main()

