'''
Commit all tickets in the index to the database.

The ticket-editing commands, as well as add, all operate on the index, a
directory that contains temporary references to objects in the database. When
all edits are done, and it's time to commit changes, this command opens EDITOR,
collects a comment from the user which it applies to all tickets to be
committed. Then, commit actually opens a new transaction, updates the ticket
DB, and the file DB, then closes the transaction.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('commit', help='Commit all tickets in the index to the database.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Commit called with args: {}".format(args))
    pass
