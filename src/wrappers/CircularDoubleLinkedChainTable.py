from src.datastructures.CirculaireDubbelgelinkteKetting import *


class CircularDoubleLinkedChainTable:
    chain = None

    def __init__(self):
        self.createTable()

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def createTable(self):
        self.chain = LinkedChain()

    def destroyTable(self):
        if self.chain is not None:
            self.chain.destroy()
            return True
        else:
            return False

    def tableLength(self):
        return self.chain.getLength()

    def tableInsert(self, newItem):
        return self.chain.insert(self.chain.getLength() + 1, newItem)

    def tableDelete(self, searchKey):
        return self.chain.delete(searchKey + 1)

    def tableRetrieve(self, searchKey):
        return self.chain.retrieve(searchKey + 1)

    def traverseTable(self):
        return self.chain.traverse()

    def load(self, input):
        return self.chain.load(input)

    def save(self):
        return self.chain.save()
