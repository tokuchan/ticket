'''
Set a ticket's state to closed.

Tickets are automatically set open when they are created. By default, only open
tickets are displayed by status. Also, open tickets are never scavenged by the
garbage collector. This command sets a ticket's state to closed. Thereafter,
the ticket will not be displayed by status without an option, and after a
duration, the garbage collector will delete the ticket and any unattached files
from the database. Only close a ticket when you are truly done with it for
good.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('close', help='Set a ticket\'s state to closed.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Close called with args: {}".format(args))
    pass
