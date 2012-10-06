'''
Stop working on a ticket.

A ticket is a unit of work, that defines a specific task. Thus, one works on
tickets by starting them. After a start, the start time is captured to the
index, and then possibly commited. When work is complete, this command is used.
The stop time is captured, and a time log message is prepared by listing start
time, stop time, and calculated duration in seconds. This event is then added
to the index. This command can only be applied to tickets that are already in
the working state.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('stop', help='Stop working on a ticket.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Stop called with args: {}".format(args))
    pass
