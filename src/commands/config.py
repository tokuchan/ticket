'''
Set configuration key/value pairs.

The configuration data in ticket are set in key/value pairs. These pairs are
recorded in several places:

1. The file `/etc/ticketrc` sets system wide configuration key/value pairs.
2. The file `$HOME/.ticketrc` sets user-specific configuration key/value pairs.
3. The file `.ticket/config` sets folder-specific configuration key/value
   pairs.

This command allows the user to get an set key/value pairs for each of these
three locations easily and naturally.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('config', help='Configure the ticket system.')
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Config called with args: {}".format(args))
    pass
