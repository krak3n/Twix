# -*- coding: utf-8 -*-

"""
.. module:: twix.cmd
   :synopsis: Twix Command Line Interface
"""

from docopt import docopt
from textwrap import dedent
from twix import get_version


def main():
    """ Main entry point into the application. Uses ``docopt`` to spawn the
    initial command line interface to the user.
    """

    interface = """
    Twix {version}

    Twix is a Tmux session manager in the same vein as Tmuxinator and friends.

    Documentation:
        https://twix.readthedocs.org

    Usage:
        twix start <name>
        twix new <name> [--extends=<existing>]
        twix copy <name> <new>
        twix wipe [<name>]
        twix show <name>
        twix list

    Options:
        --extends=<existing>   Create a new config which extends from another
        -h --help              Show this help text.
        --version              Show version.

    Example:
        twix create foo
        twix foo
    """

    interface = dedent(interface.format(version=get_version()))
    args = docopt(interface, version='Twix {0}'.format(get_version()))
