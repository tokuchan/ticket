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
            summary=None, 
            author=None,
            creation_date=datetime.today()
            ):
        self.__title = title
        self.__summary = summary
        self.__author = author
        self.__creation_date = creation_date
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
        return hashlib.sha256(self.__title.encode('utf8')).digest()
    pass

