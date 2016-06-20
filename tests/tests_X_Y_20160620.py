'''
Created on 

@author: dguibert
'''
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""bla"""

#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-tests --cover-xml
#nosetests -x --verbosity=3 --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=tests --cover-tests --cover-xml



import time, os, sys, serial, threading
import RPi.GPIO as GPIO
import unittest
import logging.config

from code import Math

logfilename         = time.strftime("%Y%m%d_%Hh%Mm%S")+"_"+os.path.basename(__file__)+".log"
logging.config.fileConfig(fname=os.environ['PYTHONSRC_GIT']+"/log.cfg", defaults={"logfilename": logfilename})
logger              = logging.getLogger("sLogger")

# indirection via bytearray b/c bytes(range(256)) does something else in Pyhton 2.7
bytes_0to255 = bytes(bytearray(range(256)))


def segments(data, size=1):
	for a in range(0, len(data), size):
		yield data[a:a + size]




class MyTest(unittest.TestCase):
	"""Test with timeouts"""
	
	def setUp(self):
		self.s = ser = serial.Serial()
		self.s.baudrate = '9600'
		self.s.port = '/dev/ttyAMA0'
		self.s.timeout = 1
		logger.info(self.s)
		self.s.open()
		logger.info(self.s)
		#ser.write(bytearray("L1\r", "ascii"))
	
	def tearDown(self):
		self.s.close()

	def test0_Messy(self):
		"""NonBlocking (timeout=0)"""
		# this is only here to write out the message in verbose mode
		# because Test3 and Test4 print the same messages

	def test1_ReadEmpty(self):
		"""timeout: After port open, the input buffer must be empty"""
		self.assertEqual(self.s.read(1).decode("utf-8"), '', "expected empty buffer")

	def test2_Loopback(self):
		"""timeout: each sent character should return (binary test).
		   this is also a test for the binary capability of a port."""
		for c in map(chr,range(256)):
			logger.info(c.encode('utf-8'))
			self.s.write(c.encode('utf-8'))
			time.sleep(0.02)	#there might be a small delay until the character is ready (especialy on win32)
			self.assertEqual(self.s.inWaiting(), 1, "expected exactly one character for inWainting()")
			self.assertEqual(self.s.read(1).decode("utf-8"), c, "expected a {0} which was written before".format(c))
		self.assertEqual(self.s.read(1).decode("utf-8"), '', "expected empty buffer after all sent chars are read")
 		


if __name__ == "__main__":
	unittest.main()

