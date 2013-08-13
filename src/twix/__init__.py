# -*- coding: utf-8 -*-

"""
.. module:: twix
   :synopsis: Twix is a tmux session spawner, inspired by tmuxinator
              and others.
"""


__VERSION__ = (0, 0, 1, 'dev', '1')


def get_version(*args, **kwagrs):
    from twix import __VERSION__ as version
    return '.'.join(str(part) for part in version)
