#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-tests --cover-xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests --cover-tests --cover-xml


[nosetests]
stop=TRUE
verbosity=3
with-xunit=TRUE
xunit-file=nosetests.xml
with-coverage=TRUE
cover-tests=TRUE
cover-inclusive=TRUE
cover-package=tests
cover-xml=TRUE
cover-xml-file=coverage.xml

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

