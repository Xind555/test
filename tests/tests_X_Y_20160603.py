#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Hello World client in Python
Connects REQ socket to tcp://localhost:5555
Sends "Hello" to server, expects "World" back
"""

import time, os
import unittest
import logging.config
import zmq

logfilename         = time.strftime("%Y%m%d_%Hh%Mm%S")+"_"+os.path.basename(__file__)+".log"
logging.config.fileConfig(fname="../log.cfg", defaults={"logfilename": logfilename})
logger              = logging.getLogger("sLogger")

class MyTest(unittest.TestCase):
    """bla"""
    
    def setUp(self):
        """Socket to talk to server"""
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://192.168.1.88:5555")
        logger.info("Connecting to hello world server…")
    
    def tearDown(self):
        pass
        
    def test_bar(self):
        """Do 10 requests, waiting each time for a response"""
        for request in range(5):
            logger.info("Sending request %s …" % request)
            self.socket.send(b"Hello")
            message = self.socket.recv()
            logger.info("Received reply %s [ %s ]" % (request, message))
            self.assertEqual(b"World", message)

if __name__ == "__main__":
    unittest.main()
