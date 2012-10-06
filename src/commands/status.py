'''
List the status of tickets.

This command lists the status of tickets. By default, only open and working
tickets are displayed. In addition, in a separate pane, tickets in the index
are listed.  This way, the user knows exactly which tickets are being edited
and which are not. In addition, each ticket's displayed line number can be used
as a relative reference for that ticket. Since the status listing is order by
the age of the last status change, this presents an easy and natural way to
refer to tickets, without having to remember their SHA hashes.

In addition to this command's ability to display tickets in order of status
change, the user can also request other orderings, as well as filters, and a
specified column order. Thus, this command is a powerful tool for ticket system
reporting, as well as a quick way to keep on top of tasks.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('status', help='Display the status of the ticket system.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Status called with args: {}".format(args))
    pass
