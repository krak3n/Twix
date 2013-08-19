# -*- coding: utf-8 -*-

"""
.. module:: tests.test_main
   :synopsis: Tests for twix.main
"""

import mock
import unittest


class MainTests(unittest.TestCase):

    def setUp(self):
        patcher = mock.patch('twix.main.docopt')
        self.docopt = patcher.start()
        self.addCleanup(patcher.stop)
