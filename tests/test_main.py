# -*- coding: utf-8 -*-

"""
.. module:: tests.test_main
   :synopsis: Tests for twix.main
"""

import mock
import unittest

from twix.main import run


class MainTests(unittest.TestCase):

    def setUp(self):
        patcher = mock.patch('twix.main.docopt')
        self.docopt = patcher.start()
        self.addCleanup(patcher.stop)

    @mock.patch('twix.main.Start')
    def test_start_called(self, mock_start):
        """ Ensure twix.main.start is called when start command
        is supplied to docopt.
        """

        args = {
            'start': True,
            '<name>': 'foo'
        }

        self.docopt.return_value = args
        run()

        mock_start.assert_called_with('foo')
