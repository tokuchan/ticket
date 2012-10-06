'''
Change a ticket's state to open.

Only open tickets are displayed by status by default. Also, only open tickets
and their attachments are guaranteed safe from the garbage collector. Thus, if
one mistakenly closes a ticket that one didn't mean to, this command will allow
one to rectify one's mistake.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('open', help='Change a ticket\'s state to open.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Open called with args: {}".format(args))
    pass
