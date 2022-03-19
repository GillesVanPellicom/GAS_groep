class Honing:
    # ADT Honing
    ## data
    id = None  # No id on init, Primary key, Auto increment
    price = 0.5  # Price in eur
    expDate = None # No expiration date on init

    def __init__(self, ID, vervalJaar, vervalMaand, vervalDag):
        self.id = ID
        self.jaar = vervalJaar
        self.maand = vervalMaand
        self.daag = vervalDag