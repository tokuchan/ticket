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
import commands.add as add
import commands.add_note as add_note
import commands.close as close
import commands.commit as commit
import commands.config as config
import commands.gc as gc
import commands.init as init
import commands.log as log
import commands.open as open
import commands.show as show
import commands.start as start
import commands.status as status
import commands.stop as stop

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
    add.getArgumentParser(subparsers)                                           # Load up the add parser.
    add_note.getArgumentParser(subparsers)                                      # Load up the add_note parser.
    close.getArgumentParser(subparsers)                                         # Load up the close parser.
    commit.getArgumentParser(subparsers)                                        # Load up the commit parser.
    config.getArgumentParser(subparsers)                                        # Load up the config parser.
    gc.getArgumentParser(subparsers)                                            # Load up the gc parser.
    init.getArgumentParser(subparsers)                                          # Load up the init parser.
    log.getArgumentParser(subparsers)                                           # Load up the log parser.
    open.getArgumentParser(subparsers)                                          # Load up the open parser.
    show.getArgumentParser(subparsers)                                          # Load up the show parser.
    start.getArgumentParser(subparsers)                                         # Load up the start parser.
    status.getArgumentParser(subparsers)                                        # Load up the status parser.
    stop.getArgumentParser(subparsers)                                          # Load up the stop parser.
    
    # Parse arguments and run program.
    args = parser.parse_args()                                                  # Parse command arguments.
    args.func(args)                                                             # Each subcommand must use set_default(func=main_function) to define their main.
    print("Main program called with args: {}".format(args))
    pass

if __name__ == '__main__':
    main()
    pass
