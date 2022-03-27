from src.wrappers.CircularDoubleLinkedChainTable import *


class MasterWrapper:
    # FIXME !!!
    data = CircularDoubleLinkedChainTable()
    def __init__(self):
        self.createTable()

    def tableIsEmpty(self):
        return self.data.tableIsEmpty()

    def createTable(self):
        # FIXME !!!
        self.data = CircularDoubleLinkedChainTable()

    def destroyTable(self):
        return self.data.destroyTable()

    def tableLength(self):
        return self.data.tableLength()

    def tableInsert(self, newItem):
        return self.data.tableInsert(newItem)

    def tableDelete(self, searchKey):
        return self.data.tableDelete(searchKey)

    def tableRetrieve(self, searchKey):
        return self.data.tableRetrieve(searchKey)

    def traverseTable(self):
        return self.data.traverseTable()

    def load(self, input):
        return self.data.load(input)

    def save(self):
        return self.data.save()