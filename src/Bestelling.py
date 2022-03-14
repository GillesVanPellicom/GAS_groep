from QuatzalShop import *
from Gebruiker import *


class MyQueue:
    def __init__(self, cap):
        self.queue = []
        self.front = self.back = 0
        self.capacity = cap

    """
    Maakt een lege queue aan.

    Précondities: geen.
    Postcondities: er is een lege queue aangemaakt (size == 0).
    :param cap: een integer dat de capacity van de queue heeft.
    """

    def isEmpty(self):
        if self.front == self.back:
            return True
        self.queue.reverse()
        return False

    """
    Bepaalt of een queue leeg is. 

    Précondities: er bestaat een queue.
    Postcondities: boolean waarde True of False is teruggegeven
    :param: geen.
    """

    def enqueue(self, newItem):
        if (self.back == self.capacity - 1):
            # if(self.capacity == self.back):
            return False
        self.queue.insert(self.back, newItem)
        self.back += 1
        return True

    """
    Voegt het element ‘newItem’ toe aan het eind (de staart) van de queue.

    Précondities: geen.
    Postcondities: nieuw element staat in de queue. Geeft een boolean waarde terug.
    :param newItem: is een string (bv. honing, chilipeper,...) of integer.
    """

    def dequeue(self):
        if (self.front != self.back):
            self.queue.reverse()
            queueFront = self.queue.pop(0)
            self.back -= 1
            return queueFront, True
        return None, False

    """
    Plaatst de kop van een queue in queueFront en verwijdert dan deze kop.

    Précondities: de queue is niet leeg (er zit tenminste 1 element in).
    Postcondities: het laatst toegevoegde element is verwijdert. Geeft een boolean waarde en het verwijderde item (queueFront) terug.
    :param: geen.
    """

    def getFront(self):
        if (self.isEmpty()):
            return None, False
        else:
            queueFront = self.queue[self.front]
            return queueFront, True

    """
    Plaatst de kop van een queue (het eerst toegevoegde element) in
    ‘queueFront’ en laat de queue ongewijzigd.

    Précondities: de queue is niet leeg (er zit tenminste 1 element in).
    Postcondities: de queue is niet verandert (geen nieuwe elementen of verwijderde elementen);
    we kennen de waarde van de top (=laatst toegevoegde item= queueFront). Geeft een boolean waarde en de queueFront terug.
    :param geen.
    """

    def save(self):
        self.queue.reverse()
        self.back += 1
        return self.queue

    """
        Houdt de huidige queue bij.

        Précondities: geen.
        Postcondities: geeft huidige queue terug.
        :param geen.
    """

    def load(self, a):
        self.queue = a
        self.back = len(a)
        return self.queue.reverse()

    """
        Schrijft de queue over met een nieuwe queue.

        Précondities: geen.
        Postcondities: geeft nieuwe queue terug.
        :param a: is een queue.
    """


class bestelling:
    # ADT Bestelling
    ## data

    id = None  # No id on init, Primary key, Auto increment
    userId = []  # No userId on init, Foreing key
    orderDate = None  # No order date on init
    chocolademelkId = ["wit", "melk", "bruin", "zwart"]  # No chocolademelkId on init, Foreing key
    orderIsPickedUp = False  # Order not picked up on init

    ### functionaliteit
    def __init__(self, timestamp, chocID=0, alAfgehaald=False):
        self.timestamp = timestamp
        self.chocID = chocID
        self.alAfgehaald = alAfgehaald

        self.queue = []
        self.front = self.back = 0
        self.capacity = 10

    #print(email)
    def placeOrder(self, chocolademelkId, gebruikers):
        orders = MyQueue(10)
        #print("b")
        """
        Place order for UserId for chocolademelkId

        preconditie : userId and chocolademelkId exists
        postconditie : new order placed

        :param chocolademelkId: id of the correct instance of chocolademelk
        :param userId: id of the correct instance of user
        """
        #print("c")

        for i in chocolademelkId:
            for j in G.addGebruiker():
                if (email == j):
                    #print("d")
                    MyQueue.enqueue(self,i)
                    return MyQueue.save(self)

    def change(self, chocolademelkId, userId):
        """
        Edit order for UserId for chocolademelkId

        precondities: userId, chocolademelkId and corresponding order exists
        postconditie: order changed
        """
        pass

    def calcCredits(self):
        """
        Calculates amount of credits needed to execute

        :return integer amount of credits
        """
        pass

    def assignWorker(self, workerId):
        """
        Places worker on order

        :param workerId: id of the worker
        """
        pass
#print("\tBestelling: ", Ingredienten)
for i in range(4):
    B = bestelling(i)
#print(B.placeOrder(B.chocolademelkId, G.addGebruiker()))

