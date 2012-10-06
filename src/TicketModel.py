'''
Ticket Model class
Sean R. Spillane
sean@spillane.us

Implements a Ticket model object to represent the concept of task tickets in
the system.

This object provides a place to store the details of a particular Ticket. In
addition, several convenience methods provide things like the Ticket's ID, an
SHA hash, along with ways to iterate over various contents, like notes, files,
and tags. These Tickets can be directly constructed, as a new Ticket should be,
but they can also be returned by factories in IndexModel and DatabaseModel.
These latter methods are the means by which a Ticket object might be reified
from the databases.
'''

import datetime
import hashlib

class TicketModel:
    def __init__(self, 
            title, 
            author=None,
            summary=None, 
            ticket_open=True,
            working=False,
            creation_date=datetime.today(),
            ticket=None
            ):
        if not ticket is None:
            self.__title = ticket.getTitle() if not title is None
            self.__author = ticket.getAuthor() if not author is None
            self.__summary = ticket.getSummary() if not summary is None
            self.__ticket_open = ticket.isOpen() and ticket_open
            self.__working = ticket.isWorking() or working
            self.__creation_date = ticket.getSummary() if not creation_date is None
            pass
        self.__title = title
        self.__author = author
        self.__summary = summary
        self.__creation_date = creation_date
        self.__open = ticket_open
        self.__working = working
        pass

    def getTitle(Self):
        return self.__title

    def getSummary(self):
        return self.__summary

    def getAuthor(self):
        return self.__author

    def getCreationDate(self):
        return self.__creation_date

    def getID(self):
        return getID(self.__title)

    def isWorking(self):
        return self.__working

    def isOpen(self):
        return self.__open

    def merge(self, other):
        '''
        Given another Ticket, return a new Ticket, derived from our Ticket,
        overlaid with the other Ticket.
        '''
        return Ticket(ticket=self,
                title=other.getTitle(),
                author=other.getAuthor(),
                summary=other.getSummary(),
                ticket_open=other.isOpen(),
                working=other.isWorking(),
                creation_date=other.creation_date())
        pass

    pass

def getID(unicode_string):
    '''
    Given a unicode string, compute the SHA256 hexdigest.
    '''
    return hashlib.sha256(self.__title.encode('utf8')).digest()

