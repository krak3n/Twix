# -*- coding: utf-8 -*-

"""
.. module:: twix.cmd
   :synopsis: Twix Command Line Interface
"""

from docopt import docopt
from textwrap import dedent
from twix import get_version
from twix.copy import Copy
from twix.list import List
from twix.new import New
from twix.show import Show
from twix.start import Start
from twix.wipe import Wipe


def run():
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
        twix copy <existing> <new>
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

    cmds = ['start', 'new', 'copy', 'wipe', 'show', 'list']
    cmd = next((k for k, v in args.iteritems() if k in cmds and v), None)

    func = globals().get(cmd)
    func(args)


def start(args):
    """ Start a Tmux session

    :param args: The cli arguments
    :type args: dict
    """

    Start(args.get('<name>'))


def new(args):
    """ Create a new configuration file

    :param args: The cli arguments
    :type args: dict
    """

    kwargs = {}
    if args.get('--extends'):
        kwargs['extends'] = args.get('<existing>')

    New(args.get('<name>'), **kwargs)


def copy(args):
    """ Copy an existing configuration to a new configuration

    :param args: the cli arguments
    :type args: dict
    """

    Copy(args.get('<existing>'), args.get('<new>'))


def wipe(args):
    """ Wipe all configurations and a specific one

    :param args: the cli arguments
    :type args: dict
    """

    Wipe(name=args.get('<name>'))


def show(args):
    """ Show the shell commands executed by a configuration

    :param args: the cli arguments
    :type args: dict
    """

    Show(args.get('<name>'))


def list(args):
    """ List existing configurations

    :param args: the cli arguments
    :type args: dict
    """

    List()
