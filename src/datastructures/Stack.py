from src.wrappers.MasterWrapper import *


class Stack():
    def __init__(self):
        pass

    stack = MasterWrapper()

    def createStack(self):
        self.stack = MasterWrapper()
        return True

    def destroyStack(self):
        self.stack = None
        return True

    def isEmpty(self):
        return self.stack.tableIsEmpty()

    def push(self, newItem):
        self.stack.tableInsert(newItem)

    def pop(self):
        temp = self.getTop()[0]
        self.stack.tableDelete(self.stack.tableLength()-1)
        return temp

    def getTop(self):
        return self.stack.tableRetrieve(self.stack.tableLength()-1)

    def tableRetrieve(self, searchKey):
        return self.stack.tableRetrieve(searchKey)

    def tableLength(self):
        return self.stack.tableLength()