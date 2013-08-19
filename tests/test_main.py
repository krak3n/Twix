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
        """ Ensure twix.start.Start is called when start command
        is supplied to docopt.
        """

        args = {
            'start': True,
            '<name>': 'foo'
        }

        self.docopt.return_value = args
        run()

        mock_start.assert_called_with('foo')

    @mock.patch('twix.main.New')
    def test_new_called(self, mock_new):
        """ Ensure twix.new.New is called when new command
        is supplied to docopt.
        """

        args = {
            'new': True,
            '<name>': 'foo'
        }

        self.docopt.return_value = args
        run()

        mock_new.assert_called_with('foo')

    @mock.patch('twix.main.New')
    def test_new_called_with_extends(self, mock_new):
        """ Ensure twix.new.New is called when new command
        is supplied to docopt with extends arg.
        """

        args = {
            'new': True,
            '<name>': 'foo',
            '--extends': True,
            '<existing>': 'bar'
        }

        self.docopt.return_value = args
        run()

        mock_new.assert_called_with('foo', extends='bar')

    @mock.patch('twix.main.Copy')
    def test_copy_called(self, mock_new):
        """ Ensure twix.copy.Copy is called when copy command
        is supplied to docopt.
        """

        args = {
            'copy': True,
            '<existing>': 'foo',
            '<new>': 'bar'
        }

        self.docopt.return_value = args
        run()

        mock_new.assert_called_with('foo', 'bar')
