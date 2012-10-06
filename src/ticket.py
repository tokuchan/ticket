#!usr/bin/env python3
# It might be wise to replace this string with a template, so that cmake can stick in the right executable when it installs.
'''
Personal Ticket Tracker.

I find that I need a simple system to let me manage my tasks in a
context-related way. Since there doesn't seem to be anything terribly
compelling available for this purpose, I have chosen to write something. In
this program, we have a simple runner. Since Argparse really whips the Llama's
ass, we can handle subcommands elegantly. Each subcommand will come from a
module, and the constructor for the subcommand object will accept an argparse
object, so that it might call `add_parser()` on it and add its arguments. Thus,
new commands are added by writing an appropriate module, then importing that
module and adding its contructor to the initialization list. Thus do we handle
subcommands neatly in one program.
'''
# Table of Contents:
# [Command Imports]
# [Regular Imports]
# [Main Function]

# [Command Imports]

# [Regular Imports]
import argparse

# [Main Function]
def main():
    '''
    Run the main program.
    @param args the Argparse object.
    '''
    parser = argparse.ArgumentParser()                                          # Construct a new argument parser.
    # Add any global arguments here.
    subparsers = parser.add_subparsers(help='sub_command help')                 # Add a set of sub parsers.
    # Construct and initialize command objects here.
    args = parser.parse_args()                                                  # Parse command arguments.
    # Run program.
    pass
