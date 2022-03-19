# ADT Marshmallow
## data
id = None
prijs = 0.75
vd = None # vd = vervaldatum

### functionaliteit
class Marshmallow:
    def __init__(self, ID, vervalJaar, vervalMaand, vervalDag):
        self.id = ID
        self.jaar = vervalJaar
        self.maand = vervalMaand
        self.daag = vervalDag
