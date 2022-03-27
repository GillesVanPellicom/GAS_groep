class Bestelling:
    # ADT Bestelling
    ## data

    id = None  # No id on init, Primary key, Auto increment
    user = None  # No userId on init, Foreign key
    orderDate = None  # No order date on init
    chocolademelk = None  # No chocolademelk on init, Foreing key
    orderIsPickedUp = False  # Order not picked up on init

    ### functionaliteit
    def __init__(self, chocolademelk, user, timestamp):
        self.chocolademelk = chocolademelk
        self.user = user
        self.orderDate = timestamp

    """
    Gets credits req'd to execute order

    Precondition: bestelling has been instantiated with constructor
    Postcondition: returns credits

    @rtype: int
    @returns: integer expressing credits
    """

    def getCredits(self):
        return self.chocolademelk.credits
