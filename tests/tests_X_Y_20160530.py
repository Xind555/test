#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""bla"""

#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-tests --cover-xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests --cover-tests --cover-xml

import time, os
import unittest
import logging.config
from code import Math

logfilename         = time.strftime("%Y%m%d_%Hh%Mm%S")+"_"+os.path.basename(__file__)+".log"
logging.config.fileConfig(fname="log.cfg", defaults={"logfilename": logfilename})
logger              = logging.getLogger("sLogger")

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
		logger.info("OK")
	
	def test_bar(self):
		"""test_bar"""
		var = 'data' + self.session
		self.assertEqual(var, 'datafoobar')
		logger.info("OK")
	
	def test_sum(self):
		"""Check is sum method is equivalent to operator"""
		var = Math.sum(1,1)
		self.assertEqual(var, 2)
		logger.info("OK")
		
	def test_subs(self):
		"""Check is subs method is equivalent to operator"""
		var = Math.subs(1,1)
		self.assertEqual(var, 0)
		logger.info("OK")
		
	def test_mul(self):
		"""Check is mul method is equivalent to operator"""
		var = Math.mul(3,3)
		self.assertEqual(var, 9)
		logger.info("OK")

if __name__ == "__main__":
	unittest.main()

