from enum import Enum


class ChocoladeshotType(Enum):
    WIT = 1
    MELK = 2
    BRUIN = 3
    ZWART = 4

class Chocoladeshot:
    # ADT Chocolademelk
    # data
    id = None  # No id on init, Primary key, Auto increment
    prijs = 2  # Price in eur
    chocoladetype = None # Type of chocolate. Use enum ChocoladeshotType

    def __init__(self, ID, type, vervalJaar, vervalMaand, vervalDag):
        self.id = ID
        self.chocoladetype = type
        self.jaar = vervalJaar
        self.maand = vervalMaand
        self.daag = vervalDag


