# -*- coding: utf-8 -*-

"""
.. module:: twix.twix
   :synopsis: Base Twix class
"""

from six import print_


class Run(object):

    @classmethod
    def run(cls):
        print_('Twix')
