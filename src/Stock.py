"""
zal de stocks aanmaken en bijhouden van alle ingredienten
"""

# ADT Stocks
from src.wrappers.MasterWrapper import *
from Chocoladeshot import *
from Honing import *
from Marshmallow import *
from Chilipeper import *


## data

### functionaliteit
class Stocks:
    marshmallow = None
    totalMarsh = None
    honing = None
    totalHoning = None
    chilipeper = None
    totalChili = None
    chocoladeshot = None
    totalChocShot = None

    jaar = 2022
    maand = 3
    dag = 29

    def __init__(self):
        self.chocoladeshot = MasterWrapper()
        self.totalChocShot = 0  # totaal aantal chocolade shots (gaat nooit naar beneden), wordt gebruikt voor het geven
        # van een ID aan de chocoladeshot instantie
        self.honing = MasterWrapper()
        self.totalHoning = 0
        self.marshmallow = MasterWrapper()
        self.totalMarsh = 0
        self.chilipeper = MasterWrapper()
        self.totalChili = 0

    """
    Returns amount left in stock of Honing

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountHoning(self):
        return self.honing.tableLength()

    """
    Returns amount left in stock of Marshmallow

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountMarshmallow(self):
        return self.marshmallow.tableLength()

    """
    Returns amount left in stock of Chilipeper

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountChilipeper(self):
        return self.chilipeper.tableLength()

    """
    Returns amount left in stock of ChocoladeShotWit

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountChocoladeshotWit(self):
        amount = 0
        for i in range(self.chocoladeshot.tableLength()):
            shot = self.chocoladeshot.tableRetrieve(i)[0]
            if shot.chocoladetype == 0:
                amount += 1
        return amount

    """
    Returns amount left in stock of ChocoladeShotMelk

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountChocoladeshotMelk(self):
        amount = 0
        for i in range(self.chocoladeshot.tableLength()):
            shot = self.chocoladeshot.tableRetrieve(i)[0]
            if shot.chocoladetype == 1:
                amount += 1
        return amount

    """
    Returns amount left in stock of ChocoladeShotBruin

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountChocoladeshotBruin(self):
        amount = 0
        for i in range(self.chocoladeshot.tableLength()):
            shot = self.chocoladeshot.tableRetrieve(i)[0]
            if shot.chocoladetype == 2:
                amount += 1
        return amount

    """
    Returns amount left in stock of ChocoladeShotZwart

    Precondition: stock is not empty
    Postcondition: N/A

    @rtype: int
    @returns: amount
    """
    def getAmountChocoladeshotZwart(self):
        amount = 0
        for i in range(self.chocoladeshot.tableLength()):
            shot = self.chocoladeshot.tableRetrieve(i)[0]
            if shot.chocoladetype == 3:
                amount += 1
        return amount

    """
    Adds chocoladeshot to stock

    Precondition: stock is initialized
    Postcondition: chocoladeshot stock +x

    @type soort: int
    @param soort: type chocoladeshot
    @type aantal: int
    @param aantal: hoeveelheid
    @type jaar: int
    @param jaar: vervaljaar
    @type maand: int
    @param maand: vervalmaand
    @type dag: int
    @param dag: vervaldag


    @rtype: boolean
    @returns: True if success
    """
    def add_chocoladeshot(self, soort, aantal, jaar, maand, dag):

        for i in range(aantal):
            chocShot = Chocoladeshot(self.totalChocShot, soort, jaar, maand, dag)
            self.chocoladeshot.tableInsert(chocShot)
            self.totalChocShot += 1
        return True

    """
    Uses one chocoladeshot

    Precondition: stock is not empty
    Postcondition: chocoladeshot stock -1
    
    @type soort: int
    @param sorot: type of chocoladeshot

    @rtype: Chocoladeshot
    @returns: object taken out of the stock
    """
    def use_chocoladeshot(self, soort):

        # haal eerst de vervallen instanties eruit
        for i in range(self.chocoladeshot.tableLength(), 0, -1):
            tmp = self.chocoladeshot.tableRetrieve(i - 1)[0]
            if tmp.jaar >= self.jaar:
                continue
            if tmp.maand >= self.maand:
                continue
            if tmp.dag >= self.dag:
                continue
            self.chocoladeshot.tableDelete(i - 1)

        # use
        if self.chocoladeshot.tableIsEmpty() == False:
            for i in range(self.chocoladeshot.tableLength()):
                # zoek een chocoladeshot instantie met de correcte soort
                if self.chocoladeshot.tableRetrieve(i)[0] == None:
                    return None
                if (self.chocoladeshot.tableRetrieve(i)[0].chocoladetype == soort):
                    instance = self.chocoladeshot.tableRetrieve(i)[0]
                    self.chocoladeshot.tableDelete(i)
                    return instance
            return None
        else:
            return None

    """
    Adds honing to stock

    Precondition: stock is initialized
    Postcondition: honing stock +x

    @type aantal: int
    @param aantal: hoeveelheid
    @type jaar: int
    @param jaar: vervaljaar
    @type maand: int
    @param maand: vervalmaand
    @type dag: int
    @param dag: vervaldag


    @rtype: boolean
    @returns: True if success
    """
    def add_honing(self, aantal, jaar, maand, dag):

        for i in range(aantal):
            hon = Honing(self.totalHoning, jaar, maand, dag)
            self.honing.tableInsert(hon)
            self.totalHoning += 1
        return True

    """
    Uses one honing

    Precondition: stock is not empty
    Postcondition: honing stock -1

    @rtype: Honing
    @returns: object taken out of the stock
    """
    def use_honing(self):

        # haal eerst de vervallen instanties eruit
        for i in range(self.honing.tableLength(), 0, -1):
            tmp = self.honing.tableRetrieve(i - 1)[0]
            if tmp.jaar >= self.jaar:
                continue
            if tmp.maand >= self.maand:
                continue
            if tmp.dag >= self.dag:
                continue
            self.honing.tableDelete(i - 1)

        # use
        if not self.honing.tableIsEmpty():
            if self.honing.tableRetrieve(0)[0] is None:
                return None
            instance = self.honing.tableRetrieve(0)[0]
            self.honing.tableDelete(0)
            return instance
        else:
            return None

    """
    Adds marshmallow to stock

    Precondition: stock is initialized
    Postcondition: marshmallow stock +x

    @type aantal: int
    @param aantal: hoeveelheid
    @type jaar: int
    @param jaar: vervaljaar
    @type maand: int
    @param maand: vervalmaand
    @type dag: int
    @param dag: vervaldag


    @rtype: boolean
    @returns: True if success
    """
    def add_marshmallow(self, aantal, jaar, maand, dag):

        for i in range(aantal):
            marsh = Marshmallow(self.totalMarsh, jaar, maand, dag)
            self.marshmallow.tableInsert(marsh)
            self.totalMarsh += 1
        return True

    """
    Uses one marshmallow

    Precondition: stock is not empty
    Postcondition: marshmallow stock -1

    @rtype: Marshmallow
    @returns: object taken out of the stock
    """
    def use_marshmallow(self):

        # haal eerst de vervallen instanties eruit
        for i in range(self.marshmallow.tableLength(), 0, -1):
            tmp = self.marshmallow.tableRetrieve(i - 1)[0]
            if tmp.jaar >= self.jaar:
                continue
            if tmp.maand >= self.maand:
                continue
            if tmp.dag >= self.dag:
                continue
            self.marshmallow.tableDelete(i - 1)

        # use
        if not self.marshmallow.tableIsEmpty():
            if self.marshmallow.tableRetrieve(0)[0] is None:
                return None
            instance = self.marshmallow.tableRetrieve(0)[0]
            self.marshmallow.tableDelete(0)
            return instance
        else:
            return None

    """
    Adds chilipeper to stock

    Precondition: stock is initialized
    Postcondition: chilipeper stock +x

    @type aantal: int
    @param aantal: hoeveelheid
    @type jaar: int
    @param jaar: vervaljaar
    @type maand: int
    @param maand: vervalmaand
    @type dag: int
    @param dag: vervaldag


    @rtype: boolean
    @returns: True if success
    """
    def add_chilipeper(self, aantal, jaar, maand, dag):

        for i in range(aantal):
            chili = Chilipeper(self.totalChili, jaar, maand, dag)
            self.chilipeper.tableInsert(chili)
            self.totalChili += 1
        return True

    """
    Uses one chilipeper

    Precondition: stock is not empty
    Postcondition: chilipeper stock -1

    @rtype: chilipeper
    @returns: object taken out of the stock
    """
    def use_chilipeper(self):

        # haal eerst de vervallen instanties eruit
        for i in range(self.chilipeper.tableLength(), 0, -1):
            tmp = self.chilipeper.tableRetrieve(i - 1)[0]
            if tmp.jaar >= self.jaar:
                continue
            if tmp.maand >= self.maand:
                continue
            if tmp.dag >= self.dag:
                continue

            self.chilipeper.tableDelete(i - 1)

        # use
        if self.chilipeper.tableIsEmpty() == False:
            if self.chilipeper.tableRetrieve(0)[0] == None:
                return None
            instance = self.chilipeper.tableRetrieve(0)[0]
            self.chilipeper.tableDelete(0)
            return instance
        else:
            return None


if __name__ == "__main__":
    s = Stocks()
    print(s.getAmountChocoladeshotBruin())
    print(s.getAmountChocoladeshotMelk())
    s.add_chocoladeshot(2, 1, 2022, 3, 29)
    s.add_chocoladeshot(1, 3, 2022, 3, 28)
    print(s.getAmountChocoladeshotBruin())
    print(s.getAmountChocoladeshotMelk())
    print(s.use_chocoladeshot(2))
    print(s.use_chocoladeshot(1))
    print(s.getAmountChocoladeshotBruin())
    print(s.getAmountChocoladeshotMelk())
    s.add_chocoladeshot(2, 3, 2021, 3, 29)
    s.add_chocoladeshot(1, 3, 2022, 2, 28)
    print(s.getAmountChocoladeshotBruin())
    print(s.getAmountChocoladeshotMelk())
    print(s.use_chocoladeshot(2))
    print(s.use_chocoladeshot(1))
    print(s.getAmountChocoladeshotBruin())
    print(s.getAmountChocoladeshotMelk())
    s.add_chilipeper(1, 2022, 10, 26)
    s.add_marshmallow(82, 2022, 10, 26)
    print(s.use_chilipeper())
    print()
