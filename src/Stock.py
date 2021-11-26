"""
zal de stocks aanmaken en bijhouden van alle ingredienten
"""

# ADT Stocks
## data
stock_chocoladeshot = None
stock_honing = None
stock_marshmallow = None
stock_chilipeper = None


### functionaliteit
class Stocks:
    def __init__(self):
        pass

    def nieuwelading_chocoladeshot(self, stock_chocoladeshot):
        """
        voeg extra stock toe aan de chocoladeshots

        preconditie : stock_chocoladeshot is een integer die de hoeveelheid stock voorsteld van de chocoladeshots
        postconditie : stock_chocoladeshot is verhoogt

        :param: stock_chocoladeshot is een integer die de hoeveelheid stock voorsteld van de chocoladeshots

        :return: geeft niets terug
        """
        pass

    def nieuwelading_honing(self):
        """
        voeg extra stock toe aan de honing

        preconditie : stock_honing is een integer die de hoeveelheid stock voorsteld van de honing
        postconditie : stock_honing is verhoogt

        :param: stock_honinh is een integer die de hoeveelheid stock voorsteld van de honinh

        :return: geeft niets terug
        """
        pass

    def nieuwelading_marshmallow(self):
        """
        voeg extra stock toe aan de marshmallow

        preconditie : stock_marshmallow is een integer die de hoeveelheid stock voorsteld van de marshmallows
        postconditie : stock_marshmallow is verhoogt

        :param: stock_marshmallow is een integer die de hoeveelheid stock voorsteld van de marshmallows

        :return: geeft niets terug
        """
        pass

    def nieuwelading_chilipeper(self):
        """
        voeg extra stock toe aan de chilipeper

        preconditie : stock_chilipeper is een integer die de hoeveelheid stock voorsteld van de chilipepers
        postconditie : stock_chilipeper is verhoogt

        :param: stock_marshmallow is een integer die de hoeveelheid stock voorsteld van de chilipepers

        :return: geeft niets terug
        """
        pass

    def verlaag_chocoladeshot(self, aantal = 1):
        """
        verlaagd de stock van de chocoladeshot met aantal (indien niet gespecifieerd 1)

        preconditie : er is nog stock
        postconditie : de stock is verlaagd

        :return:
        """
        pass

    def verlaag_honing(self, aantal = 1):
        """
        verlaagd de stock van de honing met aantal (indien niet gespecifieerd 1)

        preconditie : er is nog stock
        postconditie : de stock is verlaagd

        :return:
        """
        pass

    def verlaag_marshmallow(self, aantal = 1):
        """
        verlaagd de stock van de marshmallows met aantal (indien niet gespecifieerd 1)

        preconditie : er is nog stock
        postconditie : de stock is verlaagd

        :return:
        """
        pass

    def verlaag_chilipeper(self, aantal = 1):
        """
        verlaagd de stock van de chilipepers met aantal (indien niet gespecifieerd 1)

        preconditie : er is nog stock
        postconditie : de stock is verlaagd

        :return:
        """
        pass
