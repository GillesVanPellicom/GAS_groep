class ChainItemType:
    def __init__(self, value, position, nextptr, prevptr):
        self.value = value
        self.position = position
        self.nextptr = nextptr
        self.prevptr = prevptr

class LinkedChain:
    """
    functies:
    isEmpty,
    getLength,
    insert,
    traverse,
    delete,
    retrieve,
    destroy,
    save, voor inginious
    load  voor inginious
    """

    def __init__(self):
        self.dummyHead = ChainItemType("dummyHead", 0, "dummyHead","dummyHead") #dummyHead heeft geen waarde
        self.curptr = self.dummyHead #staat op dummyhead in het begin
        self.nextptr = None #een next pointer
        self.length = 0 #dummyHead telt niet

    def destroy(self):
        self.dummyHead = ChainItemType("dummyHead", 0, "dummyHead","dummyHead")
        self.curptr = self.dummyHead
        self.nextptr = None
        self.length = 0

    def traverse(self):
        self.curptr = self.curptr.nextptr

    def insert(self, position, item):
        if position <= self.length+1:
            if self.length == 0:
                newItem = ChainItemType(item, 1, self.dummyHead, self.dummyHead)
                self.dummyHead.nextptr = newItem
                self.dummyHead.prevptr = newItem
                self.length = 1
                return True
            elif position == self.length+1:
                """
                voeg een element achteraan in de chain toe
                #stap 1 ga naar het laatste element
                #stap 2 voeg het element in
                """
                while self.curptr.position != position - 1:
                    self.traverse()

                newItem = ChainItemType(item, position, self.dummyHead, self.curptr)
                self.dummyHead.prevptr = newItem
                self.curptr.nextptr = newItem
                self.length += 1
                return True

            else:
                if self.curptr.position != position - 1:
                    currentPosition = self.curptr.position #nodig om niet oneindig lang te zoeken
                    self.traverse()
                    if self.curptr.position != position - 1:
                        while self.curptr.position != position - 1 and self.curptr.position != currentPosition:
                            # position -1 want we willen 1 positie voor degene waar we willen inserten zitten
                            self.traverse()

                if self.curptr.position == position - 1:
                    self.nextptr = self.curptr.nextptr
                    newItem = ChainItemType(item, position, self.nextptr, self.curptr)
                    self.nextptr.prevptr = newItem
                    self.curptr.nextptr = newItem
                    self.length += 1
                    # Nu de positie van elke achter het nieuwe item verhogen:
                    self.traverse() #we zitten in de newItem
                    self.traverse() #nu zitten we 1 verder
                    while self.curptr.value != "dummyHead":
                        self.curptr.position += 1
                        self.traverse()
                    return True
        else:
            return False

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def getLength(self):
        return self.length

    def retrieve(self, position):
        if position <= self.length:
            while self.curptr.position != position:
                self.traverse()
            return (self.curptr.value, True)
        else:
            return (None,False)

    def delete(self,position):
        if position <= self.length:
            pos = position - 1
            if pos < 0:
                return False #betekent dat ze 0 oftewel de dummyHead proberen te verwijderen

            while self.curptr.position != pos:
                self.traverse()
            self.nextptr = self.curptr.nextptr.nextptr
            self.curptr.nextptr = self.nextptr
            self.nextptr.nextptr.prevptr = self.curptr
            self.length -= 1
            self.traverse() #we staan op de 2e volgende(als je de geremovede meetelt)
            while self.curptr.value != "dummyHead":
                self.curptr.position -= 1
                self.traverse()
            return True
        else:
            return False

    def save(self,alldata=False):
        List = []
        while self.curptr.position != 1:
            self.traverse()
        currentPosition = self.curptr.position
        if alldata == False:
            if self.curptr.value != "dummyHead":
                List.append((self.curptr.value))
        else:
            if self.curptr.value != "dummyHead":
                List.append((self.curptr))

        self.traverse()

        if alldata == False:
            while self.curptr.position != currentPosition:
                if self.curptr.value != "dummyHead":
                    List.append(self.curptr.value)
                self.traverse()
        else:
            while self.curptr.position != currentPosition:
                if self.curptr.value != "dummyHead":
                    List.append(self.curptr)
                self.traverse()

        if alldata == False:
            return List
        else:
            for i in range(len(List)):
                print()
                print("Value: ", List[i].value)
                print("Position: ", List[i].position)
                print("nextpointer: ", List[i].nextptr.value)
                print("prevpointer: ", List[i].prevptr.value)
                print()

    def load(self, List):
        self.dummyHead = ChainItemType("dummyHead", 0, "dummyHead", "dummyHead")  # dummyHead heeft geen waarde
        self.curptr = self.dummyHead  # staat op dummyhead in het begin
        self.nextptr = None  # een next pointer
        self.length = 0  # dummyHead telt niet
        for i in range(len(List)):
            self.insert(i+1,List[i])



if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())
    print(l.getLength())
    print(l.retrieve(4)[1])
    print(l.insert(4, 500))
    print(l.isEmpty())
    print(l.insert(1, 500))
    print(l.retrieve(1)[0])
    print(l.retrieve(1)[1])
    print(l.save())
    print(l.insert(1, 600))
    print(l.save())
    l.load([10, -9, 15])
    l.insert(3, 20)
    print(l.delete(0))
    print(l.save())
    print(l.delete(1))
    print(l.save())
