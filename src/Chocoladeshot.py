class Chocoladeshot:
    # ADT Chocolademelk
    # data
    id = None  # No id on init, Primary key, Auto increment
    prijs = 2  # Price in eur
    expDate = None # No expiration date on init
    chocoladetype = None # Type of chocolate. Use enum ChocoladeshotType
    jaar = None
    maand = None
    dag = None
    def __init__(self, ID, type, vervalJaar, vervalMaand, vervalDag):
        self.id = ID
        self.chocoladetype = type
        self.jaar = vervalJaar
        self.maand = vervalMaand
        self.dag = vervalDag


