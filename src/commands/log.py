'''
Print log of ticket changes.

Each time a ticket is altered, the user is supposed to enter a log message.
Each of these messages exists in a total order by the time the message was
created, as well as the time the ticket was created as a second sorting. Thus,
we can order all notes and present them in a log. This command prints out this
log.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('log', help='View the notes log.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Log called with args: {}".format(args))
    pass
