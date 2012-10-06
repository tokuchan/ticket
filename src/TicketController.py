'''
Ticket Controller class.
Sean R. Spillane
sean@spillane.us

Implements a controller object to manage coupling between the UI and the model objects.

We recruit ourselves to the principle of model-view separation. To achieve this
lofty goal, we undertake to provide an application controller class, which
shall implement the basic operations of the ticket system. This means that most
of the commands that the user enters are actually expressed as methods on an
instance of this object. Thus, to add a new command to the ticket system, one
must add a command module to the UI, but also one might have to add features to
this controller.

The basic workflows involve manipulating ticket, file, tag, and note objects
from the model, which are then stored or retrieved from the index model object,
which implements simple, file-based, and temporary storage. The only commands
that currently manipulate the actual database are the commit command and the
garbage collector. These manipulations all take place under the aegis of this
controller.
'''

class TicketController:
    def __init__(self):
        pass
    pass

