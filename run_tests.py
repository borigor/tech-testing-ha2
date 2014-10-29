#!/usr/bin/env python2
import unittest
import sys
from tests.test_main import TestMain


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestMain),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
