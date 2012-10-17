'''
Add a new ticket to the index.

Create a new ticket and add it to the index. The user's EDITOR is invoked and
the user given an opportunity to enter a comment. The first sentence of this
comment will be stripped and used as the title for the ticket, while the
remainder will be used for the ticket's summary. To add other features to this
ticket, the user must run other commands, such as add_file to add a reference
to a file to the ticket.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('add', help='Add a new ticket to the index.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Add called with args: {}".format(args))
    pass
