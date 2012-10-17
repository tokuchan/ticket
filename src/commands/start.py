'''
Start work on a ticket.

Tickets represent items of work. Therefore, it makes sense to spend time
working on them. This command alters a ticket's state to "working" and logs the
time it was run. Later, when one wishes to stop working on this ticket, one
uses the stop command. After that, the stop time is collected together with the
start time, and the ticket is ready to commit. Just like all other state
changes, the ticket is placed into the index. Thus, if one runs commit directly
after starting a ticket, the system will capture a note and record the event.
Note, working tickets cannot be "started" so one cannot run start on a ticket
twice.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('start', help='Start work on a ticket.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Start called with args: {}".format(args))
    pass
