from QuatzalShop import *

class StackItemType:
    def __init__(self, value):
        self.value = value
class MyStack:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.size = 0  # =leeg,insert op positie nul (voor de top te bepalen)
        self.topItem = self.items[max_size - 1]

    """
    Creëert een lege stack.

    Précondities: max_size>0
    Postcondities: er is een lege stack aangemaakt (size == 0)
    :param max_size: max grootte van de stack
    """

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    """
        Bepaalt of een stack leeg is.

        Précondities: er bestaat een stack.
        Postcondities: boolean waarde True of False is teruggegeven
        :param: geen.
    """

    def push(self, newItem):
        if self.size == len(self.items):
            return False
        else:
            self.items[self.size] = newItem
            self.size += 1
            return True

    """
        Voegt een element (newItem) toe aan de stack.

        Précondities: geen.
        Postcondities: nieuw element staat in de stack. Geeft een boolean waarde terug.
        :param newItem: is een string (bv. honing, chilipeper,...) of integer.
    """

    def pop(self):
        if self.isEmpty():
            return None, False
        else:
            delItem = self.items[self.size - 1]
            self.items[-1] = None
            self.size -= 1
            return delItem, True

    """
        Verwijdert het laatst toegevoegde element uit de stack (de top).

        Précondities: de stack is niet leeg (er zit tenminste 1 element in).
        Postcondities: het laatst toegevoegde element (de top) is verwijdert. Geeft een boolean waarde en het verwijderde item (delItem) terug.
        :param: geen.
    """

    def getTop(self):
        if self.isEmpty():
            return None, False
        self.topItem = self.items[self.size - 1]
        return self.topItem, True

    """
        Vraagt het laatst toegevoegde element uit de stack op.

        Précondities: de stack is niet leeg (er zit tenminste 1 element in).
        Postcondities: de stack is niet verandert (geen nieuwe elementen of verwijderde elementen);
        we kennen de waarde van de top (= laatst toegevoegde item= topItem). Geeft een boolean waarde en de topItem terug.
        :param geen.
    """

    def save(self):
        return self.items[:self.size]

    """
        Houdt de huidige stack bij.

        Précondities: geen.
        Postcondities: geeft de huidige stack terug.
        :param geen.
    """

    def load(self, a):
        self.items = a
        self.size = len(a)
        return self.items

    """
        Schrijft de stack over met een nieuwe stack.

        Précondities: geen.
        Postcondities: Geeft nieuwe stack terug.
        :param a: is een stack.
    """


class Gebruiker:
    # ADT Gebruiker
    ## data
    id = None  # No id on init, Auto increment
    firstName = None  # No prename on init
    lastName = None # No surname on init
    mail = None # No email on init, Primary key

    def __init__(self):
        self.firstName = voornaam
        self.lastName = achternaam
        self.mail = email

    def addGebruiker(self):
        gebruikers = MyStack(10)
        for i in users:
            gebruikers.push(i)
        gebruikers.save()
        return gebruikers.save()
        #print(gebruikers.save())

G = Gebruiker()
#print(G.addGebruiker())
#print(users)
