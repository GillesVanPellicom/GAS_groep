class Werknemer:
    # ADT Werknemer
    ## data
    id = None  # No id on init, Primary key, Auto increment
    firstName = None  # No prename on init
    lastName = None # No surname on init
    credits = None

    ##
    def __init__(self, firstName, lastName, credits):
        self.firstName = firstName
        self.lastName = lastName
        self.credits = credits
        self.id = firstName

