'''
Run Ticket's garbage collector.

The ticket garbage collector scans the databases for closed tickets whose close
dates are strictly older than duration time ago, where duration is by default
two weeks. For all tickets is find, gc marks these tickets and removes them
from the database. Then, it scans the object database for objects that no
longer are linked to anything and removes them from the object database. This
command is run automatically by some of the other commands every so often.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('gc', help='Run garbage collector.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Gc called with args: {}".format(args))
    pass
