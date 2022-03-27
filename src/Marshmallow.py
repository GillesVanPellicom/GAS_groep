# ADT Marshmallow
## data


### functionaliteit
class Marshmallow:
    id = None
    prijs = 0.75
    expDate = None  # No expiration date on init
    dag = None
    jaar = None
    maand = None


    def __init__(self, ID, vervalJaar, vervalMaand, vervalDag):
        self.id = ID
        self.jaar = vervalJaar
        self.maand = vervalMaand
        self.dag = vervalDag
