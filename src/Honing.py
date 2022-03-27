class Honing:
    # ADT Honing
    ## data
    id = None  # No id on init, Primary key, Auto increment
    prijs = 0.5  # Price in eur
    expDate = None  # No expiration date on init
    jaar = None
    maand = None
    dag = None


    def __init__(self, ID, vervalJaar, vervalMaand, vervalDag):
        self.id = ID
        self.jaar = vervalJaar
        self.maand = vervalMaand
        self.dag = vervalDag
