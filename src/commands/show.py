'''
Show the complete details of a particular ticket.

Given a single ticket, this command prints the entirety of that ticket's
information, including all notes and all attachments and references to screen.
This is the command that one runs to gather all information available about any
particular ticket.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('show', help='Show the complete details of a ticket.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Show called with args: {}".format(args))
    pass
