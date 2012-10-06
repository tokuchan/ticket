'''
Index Model class
Sean R. Spillane
sean@spillane.us

Implements a model object to represent the concept of the object index. This
object provides a temporary storage place for tickets that are under edit. As
such, it provides the same interface as the final database, but also provides
several syncing methods, so that commits are relatively painless.
'''

class IndexModel:
    def __init__(self):
        pass

    def updateTicket(self, ticket):
        '''
        Extract the ID of an extant Ticket, then update our copy of that
        ticket. If the ID does not obtain, then we create our ticket first.
        '''
        # The ticket's ID.
        # Reify the Ticket, using reifyTicket().
        # Merge the two tickets into one.
        # Write the new ticket object to the index.
        pass

    def reifyTicket(self, ticket_id):
        '''
        Given a ticket ID, create a new Ticket object, and fill it in with the
        details from our index. If there is no ticket in our index, we should
        then try to get a reified Ticket from the main database, and return
        that.
        '''
        # Does ticket ID exist in index?
        # If not, does ticket ID exist in database?
        # If so, retrieve ticket data from database.
        # If so, retrieve ticket data from index.
        # Given ticket data, construct and return a new Ticket.
        pass

    def deleteTicket(self, ticket_id):
        '''
        Given a ticket id, remove that Ticket from our index. If there is no
        Ticket in our index, then simply do nothing.
        '''
        # The ticket's ID.
        # Does the ticket exist in our index?
        # If so, delete it.
        pass

    def __write_object(self, objID, objRef):
        '''
        Given an object reference, use serialization to record that object to a
        file in the index folder, named by the objID.
        '''
        pass

    def __read_object(self, objID):
        '''
        Given an object ID, use serialization to read in that object from a
        file in the index, using the object ID.
        '''
        pass
    pass
