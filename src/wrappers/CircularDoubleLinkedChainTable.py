from ..CirculaireDubbelgelinkteKetting import LinkedChain


class CircularDoubleLinkedChainTable:
    chain = None

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def createTable(self):
        self.chain = LinkedChain()

    def destroyTable(self):
        if self.chain is not None:
            self.chain = LinkedChain()
            return True
        else:
            return False

    def tableLength(self):
        return self.chain.isEmpty()

    def tableInsert(self, newItem):
        return self.chain.insert(self.chain.getLength()+1, newItem)


    def tableDelete(self, searchKey):
        return self.chain.delete(searchKey+1)

    def tableRetrieve(self, searchKey):
        return self.chain.retrieve(searchKey+1)

    def traverseTable(self):
        return self.chain.traverse()
