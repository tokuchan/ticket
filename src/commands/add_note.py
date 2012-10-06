'''
Add a note to a ticket.

Normally, when the state of a ticket changes, that ticket is added to the index
and held for a commit. Then, when commit is run, the comment that the user
enters will be copied to every commited ticket. This command overrides this
behaviour, allowing the user to set the note on each ticket seperately. Then,
when commit is run, the commit comment is appended to the note for each ticket
and the whole thing becomes that ticket's logged note. This allows the user to
change state on several tickets at the same time, with unique comments for each
ticket, as well as one comment that is appended to all of the tickets, perhaps
the reason why the set of tickets were modified together in the first place.
'''

import argparse

def getArgumentParser(parsers):
    '''
    Given an argument parser, construct a subparser and set the default
    function. This allows us to transfer execution to the main function defined
    below.
    '''
    parser = parsers.add_parser('add_note', help="Set the given ticket's note independently of other tickets.")
    parser.set_defaults(func=main)                                              # We want to run the main function defined below.
    return parser
pass

def main(args):
    print("Add_note called with args: {}".format(args))
    pass
