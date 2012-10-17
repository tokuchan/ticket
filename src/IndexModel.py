'''
Index Model class
Sean R. Spillane
sean@spillane.us

Implements a model object to represent the concept of the object index. This
object provides a temporary storage place for tickets that are under edit. As
such, it provides the same interface as the final database, but also provides
several syncing methods, so that commits are relatively painless.
'''

import shelve
import TicketModel

index_file = '.ticket/index_db'

class IndexModel:
    def __init__(self):
        pass

    def updateTicket(self, ticket):
        '''
        Extract the ID of an extant Ticket, then update our copy of that
        ticket. If the ID does not obtain, then we create our ticket first.
        '''
        with shelve.open(index_file) as shelf:                                  # Provide a context managed index db.
            the_ticket = self.reifyTicket(ticket.getID())                       # Reify the Ticket, using reifyTicket().
            updated_ticket = the_ticket.merge(ticket)                           # Update the ticket.
            shelf[ticket.getID()] = updated_ticket                              # Write the new ticket object to the index.
            pass
        pass

    def reifyTicket(self, ticket_id):
        '''
        Given a ticket ID, create a new Ticket object, and fill it in with the
        details from our index. If there is no ticket in our index, we should
        then try to get a reified Ticket from the main database, and return
        that.
        '''
        with shelve.open(index_file) as shelf:
            the_ticket = shelf.get(ticket_id, TicketModel.Ticket())             # If the ticket isn't in the index, create it.
            return the_ticket
            pass
        pass

    def deleteTicket(self, ticket_id):
        '''
        Given a ticket id, remove that Ticket from our index. If there is no
        Ticket in our index, then simply do nothing.
        '''
        with shelve.open(index_file) as shelf:
            del shelf[ticket_id]
            pass
        pass

    pass
