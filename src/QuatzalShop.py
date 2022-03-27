# ADT QuatzalShop
from Gebruiker import *
from Stock import *
from Bestelling import *
from Chocolademelk import *
from src.datastructures.Stack import *
from src.datastructures.Queue import *
from Werknemer import *
import math

## Data
Time = 0
Stock = Stocks()
users = MasterWrapper()
workForce = Stack()
busyWorkForce = MasterWrapper()
orders = Queue()
newOrders = Queue()

###
debugPrint = False  # if true, print debug info in console
###

logColums = MasterWrapper()

### functionaliteit
"""
Main simulation loop.
Gets ticked every timestamp change

Precondition: QuatzalShop is initialized
Postcondition: Simulation updated

"""


def TimeUpdate():  # update everything (called when time is changed)
    # for example: update werknemers (finish order, credits back on stack, ...)
    writeColumn()

    newOrders.destroyQueue()
    newOrders.createQueue()

    # assign workers to orders
    while workForce.isEmpty() == False and orders.isEmpty() == False:
        currentOrder = orders.pop()
        currentWorker = workForce.pop()

        # place all worker that are done with their assignment back on workforce
        for i in range(busyWorkForce.tableLength()):
            if busyWorkForce.tableRetrieve(i)[0] == Time + 1:
                tmp = busyWorkForce.tableRetrieve(i)
                busyWorkForce.tableDelete(i)
                workForce.push(tmp)

        # calculate amount of time worker will be busy
        creditsReqd = Time
        if currentOrder.getCredits() <= currentWorker.credits:
            creditsReqd += 1
            busyWorkForce.tableInsert((creditsReqd, currentWorker))
        else:
            creditsReqd = math.ceil(currentOrder.getCredits() / currentWorker.credits) + Time
            busyWorkForce.tableInsert((creditsReqd, currentWorker))

    """
    Places order

    Precondition: stock is initialized
    Postcondition: chilipeper stock +x

    @type chocolademelk: Chcoclademelk
    @param chocolademelk: ordered chocolademelk
    @type gebruiker: Gebruiker
    @param gebruiker: user making the order

    @rtype: boolean
    @returns: True if success
    """


def placeOrder(chocolademelk, gebruiker):
    bestelling = Bestelling(chocolademelk, gebruiker, Time)
    orders.push(bestelling)
    newOrders.push(bestelling)
    return True

    """
    writes start of the log file (standard html tags)
    and starts the html table

    Precondition: input file reads start
    Postcondition: logStartstring gets pushed to logColumns
    """
def startOutputLogString():
    logStartStr = """<html>
    <head>
</head>
    <body>
        <h1>Log</h1>
        <table border="1px">
            <thead>
                <td>tijdstip</td>
                <td>Stack</td>"""
    for i in range(workForce.tableLength()):
        worker = workForce.tableRetrieve(i)[0]
        logStartStr += """
                <td>""" + worker.firstName + worker.lastName + """</td>"""
    for i in range(busyWorkForce.tableLength()):
        worker = busyWorkForce.tableRetrieve(i)[0]
        logStartStr += """
                <td>""" + worker.firstName + worker.lastName + """</td>"""
    logStartStr += """
                <td>Nieuwe bestellingen</td>
                <td>Wachtende bestellingen</td>
                <td>wit</td>
                <td>melk</td>
                <td>bruin</td>
                <td>zwart</td>
                <td>honing</td>
                <td>marshmallow</td>
                <td>chili</td>
            </thead>
            <tbody>"""

    logColums.tableInsert(logStartStr)


"""
Writes a column for this timestamp of the log file

Precondition: log start string was added to logColumns
Postcondition: a column string gets written and inserted at the end of logColumns

"""
def writeColumn():
    column = """
                <tr>
                    <td>""" + str(Time) + """</td>"""

    column += """
                    <td>|"""
    for w in range(workForce.tableLength()):
        column += str(workForce.tableRetrieve(w)[0].credits) + " "
    column += "</td>"

    for u in range(users.tableLength()):
        column += """
                    <td>""" + "x" + "</td>"

    # nieuwe bestellingen
    column += """
                    <td>"""
    for no in range(newOrders.tableLength()):
        order = newOrders.tableRetrieve(no)[0]
        column += str(order.chocolademelk.credits)
    column += "</td>"

    # wachtende bestellingen
    column += """
                    <td>"""
    for o in range(orders.tableLength()):
        order = orders.tableRetrieve(o)[0]
        column += str(order.chocolademelk.credits)
    column += "</td>"

    # stocks
    column += """
                    <td>""" + str(Stock.getAmountChocoladeshotWit()) + """</td>
                    <td>""" + str(Stock.getAmountChocoladeshotMelk()) + """</td>
                    <td>""" + str(Stock.getAmountChocoladeshotBruin()) + """</td>
                    <td>""" + str(Stock.getAmountChocoladeshotZwart()) + """</td>
                    <td>""" + str(Stock.getAmountHoning()) + """</td>
                    <td>""" + str(Stock.getAmountMarshmallow()) + """</td>
                    <td>""" + str(Stock.getAmountChilipeper()) + """</td>
                </tr>"""

    logColums.tableInsert(column)


# read input file:
input = open("input")
init = False
gestart = False
for line in input:
    words = line.split()
    for i in range(len(words)):
        word = words[i]
        if word == "#":
            break  # go to nextline
        if word == "init":
            init = True
            gestart = False
            break
        elif word == "start":
            if (debugPrint):
                print("Start")
            startOutputLogString()
            TimeUpdate()
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
                    Stock.add_chocoladeshot(soort, aantal, jaar, maand, dag)
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
                    Stock.add_honing(aantal, jaar, maand, dag)

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
                    Stock.add_marshmallow(aantal, jaar, maand, dag)

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
                    Stock.add_chilipeper(aantal, jaar, maand, dag)

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
                    user = Gebruiker(voornaam, achternaam, email)
                    users.tableInsert(user)

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
                        print("voeg werknemer toe: ", voornaam, achternaam + ",", "credits:", credits)
                    workForce.push(Werknemer(voornaam, achternaam, credits))

                else:
                    print("Error: incorrect command at line: ", line)
            break

        if gestart == True:
            # nu bestellingen, stock, ...
            # tijd kan nu veranderen
            # het eerste 'woord' zal altijd het tijdstip zijn van waarop de instructie gebeurt, als
            # dit tijdstip kleiner is als time, dan is er een error

            tijdstip = int(words[0])
            newWords = words[1:]  # words zonder tijdstip
            word = newWords[i]
            if int(tijdstip) >= Time:
                if debugPrint:
                    print("tijd: ", Time)

                if word == "bestel":
                    ID = newWords[i + 1]
                    # check if user with UID exists
                    user = None
                    for i in range(users.tableLength()):
                        if users.tableRetrieve(i)[0].id == ID:
                            user = users.tableRetrieve(i)[0]
                            break
                        else:
                            continue
                    if (user == None):
                        print("Error: bestelling")
                        continue

                    # gather information
                    Ingredienten = MasterWrapper()

                    for k in range(len(newWords) - 7):  # -7 omdat 2(tijdstip, bestel) + 5(time/date)
                        ingr = newWords[2 + k]
                        if type(ingr) == str:
                            Ingredienten.tableInsert(ingr)
                        else:
                            break  # if i

                    minuut = newWords[-1]
                    uur = newWords[-2]
                    dag = newWords[-3]
                    maand = newWords[-4]
                    jaar = newWords[-5]

                    timestamp = [jaar, maand, dag, uur, minuut]

                    # create bestelling
                    if debugPrint:
                        print("\tBestelling: ", ID, Ingredienten, "\t\t datum:", dag, maand, jaar + ",", " tijdstip: ",
                              uur, ":", minuut)
                    melk = Chocolademelk(Ingredienten, Stock)
                    placeOrder(melk, user)

                elif word == "stock":
                    word = newWords[i + 1]
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
                            Stock.add_chocoladeshot(soort, aantal, jaar, maand, dag)
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
                            Stock.add_honing(aantal, dag, maand, jaar)

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
                            Stock.add_marshmallow(aantal, dag, maand, jaar)

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
                            Stock.add_chilipeper(aantal, dag, maand, jaar)

                        else:
                            print("Error: incorrect command at line: ", line)

                if (tijdstip != Time):
                    Time = tijdstip
                    TimeUpdate()

                if word == "log":
                    # output
                    log = open("log" + str(Time) + ".html", "w")
                    for i in range(logColums.tableLength()):
                        log.write(logColums.tableRetrieve(i)[0])
                    log.write("""
		</table>
	</body>
</html>""")
                    log.close()

            else:
                print("Error: incorrect time at instruction: ", line)
            break

input.close()
