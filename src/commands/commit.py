'''
Initialize a ticket database.

When this command is run on an unticketed folder, we add a new .ticket folder
and write into it the various components of the system. These components
include:

1. The sqlite3 `tickets` database that actually holds the tickets themselves.
2. The `objects` folder, which will hold attachments and other files that need
   to exist outside of the database.
3. The `config` folder, which will hold any configuration files that we need to
   read/write.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('init', help='Initialize a new ticket database in the current folder.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Init called with args: {}".format(args))
    pass
