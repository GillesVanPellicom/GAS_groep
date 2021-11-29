class Chocolademelk:
    # ADT Chocolademelk
    ## data
    id = None  # No id on init, Primary key, Auto increment
    prijs = 2  # Price in eur

    def __init__(self):
        pass

    ## functionaliteit
    def addChocoladeshot(self, chocoladeshotStock, chocoladeshot):
        """
        Adds a chocoladeshot to chocolademelk
        Precondition : chocoladeshot is chosen from enum and stock not 0
        postconditie : de prijs van de chocolademelk i s verhoogd met 1 EUR
        :param chocoladeshotStock: integer expressing stock.
        :param chocoladeshot: class
        voorstelt :
        0 = WIT
        1 = MELK
        2 = BRUIN
        3 = ZWART
        """

    pass

    def addHoning(self, honingStock, honing):
        """
        Adds a honing to chocolademelk
        Precondition : stock not <0
        postconditie : price +0.50 EUR
        :param honingStock: integer expressing stock
        :param honing: class
        """

    def addMarshmallow(self, marshMallowStock, marshmallow):
        """
        Adds a marshmallow to chocolademelk
        Precondition : stock not 0
        postconditie : price +0.75 EUR
        :param marshMallowStock: integer expressing stock
        :param marshmallow : class
        """

    def addChilipeper(self, chilipeperStock, chilipeper):
        """
        Adds a chillipeper to chocolademelk
        Precondition : stock not 0
        postconditie : price +0.25 EUR
        :param chilipeperStock: integer expressing stock
        :param chilipeper: class
        """
