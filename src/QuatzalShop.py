# ADT QuatzalShop
from Chocoladeshot import *
from Chocolademelk import *
from Honing import *
from Marshmallow import *
from Chilipeper import *
from Gebruiker import *
from Stock import *
from Werknemer import *
from Bestelling import *
## Data
Time = 0
Stock = Stocks()

###
debugPrint = False # if true, print debug info in console
###


### functionaliteit

def TimeUpdate():   # update everything (called when time is changed)
    # for example: update werknemers (finish order, credits back on stack, ...)
    pass

# read input file:
input = open("input")
init = False
gestart = False
for line in input:
    words = line.split()
    for i in range(len(words)):
        word = words[i]
        if word == "#":
            break   # go to nextline
        if word == "init":
            init = True
            gestart = False
            break
        elif word == "start":
            if (debugPrint):
                print()
            init = False
            gestart = True
            break

        if init == True:
            # toevoegen van stock, werknemers, gebruikers
            if word == "shot":
                if len(words) - i > 5:
                    soort = words[i + 1]
                    aantal = int(words[i + 2])
                    jaar = int(words[i + 3])
                    maand = int(words[i + 4])
                    dag = int(words[i + 5])
                    if "#" in soort:
                        print("Error: incorrect command at line: ", line)

                    if soort == "wit":
                        soort = 0
                    elif soort == "melk":
                        soort = 1
                    elif soort == "bruin":
                        soort = 2
                    elif soort == "zwart":
                        soort = 3
                    else:
                        print("Incorrect soort at line: ", line)
                        break

                    if debugPrint:
                        print("add stock of shot:\t", soort, aantal, "\tvervaldatum: ----", jaar, maand, dag)
                    #Stock.add_chocoladeshot(soort, aantal, jaar, maand, dag)
                else:
                    print("Error: incorrect command at line: ", line)
            elif word == "honing":
                if len(words) - i > 4:
                    aantal = int(words[i + 1])
                    jaar = int(words[i + 2])
                    maand = int(words[i + 3])
                    dag = int(words[i + 4])

                    if debugPrint:
                        print("add stock of honing:", aantal, "\tvervaldatum: ----", jaar, maand, dag)
                    #Stock.add_honing(aantal, dag, maand, jaar)

                else:
                    print("Error: incorrect command at line: ", line)
            elif word == "marshmallow":
                if len(words) - i > 4:
                    aantal = int(words[i + 1])
                    jaar = int(words[i + 2])
                    maand = int(words[i + 3])
                    dag = int(words[i + 4])

                    if debugPrint:
                        print("add stock of MM:\t", aantal, "\tvervaldatum: ----", jaar, maand, dag)
                    #Stock.add_marshmallow(aantal, dag, maand, jaar)

                else:
                    print("Error: incorrect command at line: ", line)
            elif word == "chili":
                if len(words) - i > 4:
                    aantal = int(words[i + 1])
                    jaar = int(words[i + 2])
                    maand = int(words[i + 3])
                    dag = int(words[i + 4])

                    if debugPrint:
                        print("add stock of chili:\t", aantal, "\tvervaldatum: ----", jaar, maand, dag)
                    #Stock.add_chilipeper(aantal, dag, maand, jaar)

                else:
                    print("Error: incorrect command at line: ", line)
            elif word == "gebruiker":
                if len(words) - i > 3:
                    voornaam = words[i + 1]
                    achternaam = words[i + 2]
                    email = words[i + 3]
                    if "#" in voornaam or "#" in achternaam or "#" in email:
                        print("Error: incorrect command at line: ", line)

                    if debugPrint:
                        print("voeg gebruiker toe: ", voornaam, achternaam, email)
                    #gebruiker(voornaam, achternaam, email)

                else:
                    print("Error: incorrect command at line: ", line)
            elif word == "werknemer":
                if len(words) - i > 3:
                    voornaam = words[i + 1]
                    achternaam = words[i + 2]
                    credits = int(words[i + 3])
                    if "#" in voornaam or "#" in achternaam:
                        print("Error: incorrect command at line: ", line)

                    if debugPrint:
                        print("voeg werknemer toe: ", voornaam, achternaam+",", "credits:",credits)
                    #werknemer(voornaam, achternaam, credits)

                else:
                    print("Error: incorrect command at line: ", line)
            break

        if gestart == True:
            # nu bestellingen, stock, ...
            # tijd kan nu veranderen
            # het eerste 'woord' zal altijd het tijdstip zijn van waarop de instructie gebeurt, als
            # dit tijdstip kleiner is als time, dan is er een error

            tijdstip = int(word)
            newWords = words[1:] # words zonder tijdstip
            word = newWords[i]
            if int(tijdstip) >= Time:
                if (tijdstip != Time):
                    Time = tijdstip
                    TimeUpdate()
                    if debugPrint:
                        print("tijd: ", Time)

                if word == "bestel":
                    UID = newWords[i + 1]
                    Ingredienten = list()

                    for k in range(len(newWords)-7): # -7 omdat 2(tijdstip, bestel) + 5(time/date)
                        ingr = newWords[2 + k]
                        if type(ingr) == str:
                            Ingredienten.append(ingr)
                        else:
                            break # if i

                    minuut = newWords[-1]
                    uur = newWords[-2]
                    dag = newWords[-3]
                    maand = newWords[-4]
                    jaar = newWords[-5]

                    timestamp = [jaar, maand, dag, uur, minuut]

                    if debugPrint:
                        print("\tBestelling: ", UID, Ingredienten, "\t\t datum:", dag, maand, jaar+",", " tijdstip: ", uur, ":", minuut)
                    #bestelling()

                elif word == "stock":
                    word = newWords[i+1]
                    newWords = newWords[1:]
                    if word == "shot":
                        if len(newWords) - i > 5:
                            soort = newWords[i + 1]
                            aantal = int(newWords[i + 2])
                            jaar = int(newWords[i + 3])
                            maand = int(newWords[i + 4])
                            dag = int(newWords[i + 5])
                            if "#" in soort:
                                print("Error: incorrect command at line: ", line)

                            if soort == "wit":
                                soort = 0
                            elif soort == "melk":
                                soort = 1
                            elif soort == "bruin":
                                soort = 2
                            elif soort == "zwart":
                                soort = 3
                            else:
                                print("Incorrect soort at line: ", line)
                                break

                            if debugPrint:
                                print("\tadd stock of shot:\t", soort, aantal, "\tvervaldatum:", jaar, maand, dag)
                            # Stock.add_chocoladeshot(soort, aantal, jaar, maand, dag)
                        else:
                            print("Error: incorrect command at line: ", line)
                    elif word == "honing":
                        if len(newWords) - i > 4:
                            aantal = int(newWords[i + 1])
                            jaar = int(newWords[i + 2])
                            maand = int(newWords[i + 3])
                            dag = int(newWords[i + 4])

                            if debugPrint:
                                print("\tadd stock of honing:", aantal, "\tvervaldatum:", jaar, maand, dag)
                            # Stock.add_honing(aantal, dag, maand, jaar)

                        else:
                            print("Error: incorrect command at line: ", line)
                    elif word == "marshmallow":
                        if len(newWords) - i > 4:
                            aantal = int(newWords[i + 1])
                            jaar = int(newWords[i + 2])
                            maand = int(newWords[i + 3])
                            dag = int(newWords[i + 4])

                            if debugPrint:
                                print("\tadd stock of MM:\t", aantal, "\tvervaldatum:", jaar, maand, dag)
                            # Stock.add_marshmallow(aantal, dag, maand, jaar)

                        else:
                            print("Error: incorrect command at line: ", line)
                    elif word == "chili":
                        if len(newWords) - i > 4:
                            aantal = int(newWords[i + 1])
                            jaar = int(newWords[i + 2])
                            maand = int(newWords[i + 3])
                            dag = int(newWords[i + 4])

                            if debugPrint:
                                print("\tadd stock of chili:\t", aantal, "\tvervaldatum:", jaar, maand, dag)
                            # Stock.add_chilipeper(aantal, dag, maand, jaar)

                        else:
                            print("Error: incorrect command at line: ", line)

                elif word == "log":
                    if debugPrint:
                        print("\tKeyword: log.", "Create output HTML file")
                    pass
            else:
                print("Error: incorrect time at instruction: ", line)
            break

input.close()

"""
#### Usecase: gebruiker meldt aan (met of zonder account)

def bestaand_account(email):
    """
"""
    controlleert of de meegegeven email behoort tot een bestaand account in de database

    preconditie : email is een valid email adres
    postcondiite : return True als de email een bestaand account heeft, False indien niet

    :param email:
    :return: return True als de email een bestaand account heeft, False indien niet
    """
"""
    pass

def meldt_aan(email, wachtwoord):
    """
"""
    meldt de gebruiker aan met zijn email en wachtwoord

    preconditie : de email is gelinkt aan een bestaand account, het wachtwoord is correct
    postconditie : gebruiker is aangemeldt

    :param email:
    :param wachtwoord:
    :return:
    """
"""
    pass

def meldt_af():
    """
"""
    de al aangemelde gebruiker meldt zich af

    preconditie : de gebruiker is aangemeld
    postconditie : de gebruiker is afgemeld
    :return:
    """
"""
    pass

#### Usecase: annuleer bestelling

def annuleer_bestelling(bestellingID):
    """
"""
    de bestelling geplaatst door de gebruiker wordt afgezegd

    preconditie : de bestelling met bestellingID bestaat
    postconditie : de bestelling is verwijdert

    :param bestellingID:
    :return:
    """
"""
    pass

#### Usecase: werknemer maakt bestelling, verwijder bestelling wanneer afgerond

def verwijder_bestelling(afgerond, bestellingID):
    """
"""
    verwijder de bestelling uit het systeem

    preconditie : de bestelling bestaat in het systeem
    postconditie : de bestelling bestaat niet meer in het systeem

    :param bestellingID:
    :return:
    """
"""
    pass

def maak_bestelling(WID,bestellingID):
    """
"""
    assign de werknemer aan de bestelling

    preconditie : werknemer is nog niet bezig met een andere bestelling, en heeft genoeg crediet
    postconditie : werknemer is klaar met bestelling, bestelling wordt afgerond roept verwijder_bestelling(bestellingID) op

    :param WID:
    :param bestellingID:
    :return:
    """
"""

#### Usecase: voeg ingredient toe aan bestaande bestelling, verwijder ingredient

def Extra_Ingredient(bestellingID, ingredient):
    """
"""
    voeg ingredient toe aan de bestaande bestelling

    preconditie : bestellingID bestaat al
    postconditie : ingredient toegevoegd aan bestelling

    :param bestellingID:
    :param ingredient:
    :return:
    """
"""
    pass

def Verwijder_Ingredient(bestellingID, ingredient):
    """
"""
    verwijder ingredient uit de bestelling

    preconditie : bestellingID bestaat, en ingredient zit in bestelling
    postconditie : ingredient zit niet langer in bestelling

    :param bestellingID:
    :param ingredient:
    :return:
    """
"""
    pass
"""