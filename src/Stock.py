"""
zal de stocks aanmaken en bijhouden van alle ingredienten
"""

# ADT Stocks
from CirculaireDubbelgelinkteKetting import *
from Chocoladeshot import *
from Honing import *
from Marshmallow import *
from Chilipeper import *
## data

### functionaliteit
class Stocks:
    def __init__(self):
        self.chocoladeshot = LinkedChain()
        self.totalChocShot = 0  # totaal aantal chocolade shots (gaat nooit naar beneden), wordt gebruikt voor het geven
                                # van een ID aan de chocoladeshot instantie
        self.honing = LinkedChain()
        self.totalHoning = 0
        self.marshmallow = LinkedChain()
        self.totalMarsh = 0
        self.chilipeper = LinkedChain()
        self.totalChili = 0

    def getAmountHoning(self):
        return self.honing.getLength()
    def getAmountMarshmallow(self):
        return self.marshmallow.getLength()
    def getAmountChilipeper(self):
        return self.chilipeper.getLength()
    def getAmountChocoladeshotWit(self):
        amount = 0
        for i in range(1, self.chocoladeshot.getLength()+1):
            shot = self.chocoladeshot.retrieve(i)[0]
            if shot.chocoladetype == 0:
                amount+=1
        return amount
    def getAmountChocoladeshotMelk(self):
        amount = 0
        for i in range(1, self.chocoladeshot.getLength()+1):
            shot = self.chocoladeshot.retrieve(i)[0]
            if shot.chocoladetype == 1:
                amount+=1
        return amount
    def getAmountChocoladeshotBruin(self):
        amount = 0
        for i in range(1, self.chocoladeshot.getLength()+1):
            shot = self.chocoladeshot.retrieve(i)[0]
            if shot.chocoladetype == 2:
                amount+=1
        return amount
    def getAmountChocoladeshotZwart(self):
        amount = 0
        for i in range(1, self.chocoladeshot.getLength()+1):
            shot = self.chocoladeshot.retrieve(i)[0]
            if shot.chocoladetype == 3:
                amount+=1
        return amount

    def add_chocoladeshot(self, soort, aantal, jaar, maand, dag):
        """
        voeg extra stock toe aan de chocoladeshots

        preconditie :
        postconditie : een instantie van Chocoladeshot is toegevoegd aan zijn stock

        :param: soort = 0 (= "Wit"), = 1 (= "Melk"), = 2 (= "Bruin"), = 3 (= "Zwart")
                aantal = aantal toegevoegde stock
                jaar, maand, dag = vervaldatum.

        :return: bool: true als gelukt, false als mislukt
        """
        for i in range(aantal):
            chocShot = Chocoladeshot(self.totalChocShot, soort, jaar, maand, dag)
            self.chocoladeshot.insert(1, chocShot)
            self.totalChocShot += 1
        return True

    def use_chocoladeshot(self, soort):
        """
        gebruik een instantie van de chocoladestock

        preconditie : er bestaat stock van chocoladeshot
        postconditie : een instantie van Chocoladeshot is verwijderd van zijn stock

        :param soort: = 0 (= "Wit"), = 1 (= "Melk"), = 2 (= "Bruin"), = 3 (= "Zwart")
        :return: bool, true als gelukt, false als mislukt
        """
        if self.chocoladeshot.isEmpty() == False:
            for i in range(1, self.chocoladeshot.getLength()+1):
                # zoek een chocoladeshot instantie met de correcte soort
                if (self.chocoladeshot.retrieve(i)[0].chocoladetype == soort):
                    if self.chocoladeshot.delete(1) == False:
                        return False
                    return True
            return False
        else:
            return False

    def add_honing(self, aantal, jaar, maand, dag):
        """
        voeg extra stock toe aan de HoningStock

        preconditie :
        postconditie : een instantie van Honing is toegevoegd aan zijn stock

        :param: aantal = aantal toegevoegde stock
                jaar, maand, dag = vervaldatum.

        :return: bool: true als gelukt, false als mislukt
        """
        for i in range(aantal):
            hon = Honing(self.totalHoning, jaar, maand, dag)
            self.honing.insert(1, hon)
            self.totalHoning += 1
        return True

    def use_honing(self):
        """
        gebruik een instantie van de honingstock

        preconditie : er bestaat stock van honingstock
        postconditie : een instantie van Honing is verwijderd van zijn stock

        :param:
        :return: bool, true als gelukt, false als mislukt
        """
        if self.honing.isEmpty() == False:
            if self.honing.delete(1) == False:
                return False
            return True
        else:
            return False

    def add_marshmallow(self, aantal, jaar, maand, dag):
        """
        voeg extra stock toe aan de marshmallowStock

        preconditie :
        postconditie : een instantie van marshmallow is toegevoegd aan zijn stock

        :param: aantal = aantal toegevoegde stock
                jaar, maand, dag = vervaldatum.

        :return: bool: true als gelukt, false als mislukt
        """
        for i in range(aantal):
            marsh = Marshmallow(self.totalMarsh, jaar, maand, dag)
            self.marshmallow.insert(1, marsh)
            self.totalMarsh += 1
        return True

    def use_marshmallow(self):
        """
        gebruik een instantie van de marshmallowstock

        preconditie : er bestaat stock van marshmallowstock
        postconditie : een instantie van marshmallow is verwijderd van zijn stock

        :param:
        :return: bool, true als gelukt, false als mislukt
        """
        if self.marshmallow.isEmpty() == False:
            if self.marshmallow.delete(1) == False:
                return False
            return True
        else:
            return False

    def add_chilipeper(self, aantal, jaar, maand, dag):
        """
        voeg extra stock toe aan de chilipeperStock

        preconditie :
        postconditie : een instantie van chilipeper is toegevoegd aan zijn stock

        :param: aantal = aantal toegevoegde stock
                jaar, maand, dag = vervaldatum.

        :return: bool: true als gelukt, false als mislukt
        """
        for i in range(aantal):
            chili = Chilipeper(self.totalChili, jaar, maand, dag)
            self.chilipeper.insert(1, chili)
            self.totalChili += 1
        return True

    def use_chilipeper(self):
        """
        gebruik een instantie van de honingstock

        preconditie : er bestaat stock van honingstock
        postconditie : een instantie van Honing is verwijderd van zijn stock

        :param:
        :return: bool, true als gelukt, false als mislukt
        """
        if self.chilipeper.isEmpty() == False:
            if self.chilipeper.delete(1) == False:
                return False
            return True
        else:
            return False


if __name__ == "__main__":
    s = Stocks()
    s.add_chilipeper(1,2022,10,26)
    print(s.use_chilipeper())
    print()