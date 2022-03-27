class Gebruiker:
    # ADT Gebruiker
    ## data
    id = None  # No id on init, Auto increment
    firstName = None  # No prename on init
    lastName = None # No surname on init
    email = None # No email on init, Primary key

    def __init__(self, voornaam, achternaam, email):
        self.firstName = voornaam
        self.lastName = achternaam
        self.email = email
        self.id = email





