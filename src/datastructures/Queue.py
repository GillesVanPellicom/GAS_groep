from src.wrappers.MasterWrapper import *


class Queue():
    def __init__(self):
        self.createQueue()

    queue = MasterWrapper()

    def createQueue(self):
        self.queue = MasterWrapper()
        return True

    def destroyQueue(self):
        self.queue = None
        return True

    def isEmpty(self):
        return self.queue.tableIsEmpty()

    def push(self, newItem):
        self.queue.tableInsert(newItem)

    def pop(self):
        temp = self.queue.tableRetrieve(0)
        self.queue.tableDelete(0)
        return temp[0]

    def getTop(self):
        return self.queue.tableRetrieve(self.queue.tableLength()-1)

    def tableRetrieve(self, searchKey):
        return self.queue.tableRetrieve(searchKey)

    def tableLength(self):
        return self.queue.tableLength()

