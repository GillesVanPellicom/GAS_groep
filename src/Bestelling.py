class bestelling:
    # ADT Bestelling
    ## data

    id = None  # No id on init, Primary key, Auto increment
    userId = None  # No userId on init, Foreing key
    orderDate = None  # No order date on init
    chocolademelkId = None  # No chocolademelkId on init, Foreing key
    orderIsPickedUp = False  # Order not picked up on init

    ### functionaliteit
    def __init__(self, timestamp, chocID=0, alAfgehaald=False):
        pass

    def placeOrder(self, chocolademelkId, userId):
        """
        Place order for UserId for chocolademelkId

        preconditie : userId and chocolademelkId exists
        postconditie : new order placed

        :param chocolademelkId: id of the correct instance of chocolademelk
        :param userId: id of the correct instance of user
        """
        pass

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
