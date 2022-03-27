from src.datastructures.TwoThreeTree import *


class TwoThreeTreeTable():
    tree = None

    def __init__(self):
        self.tree = TwoThreeTree()

    def tableIsEmpty(self):
        return self.tree.isEmpty()

    def tableInsert(self, item):
        return self.tree.insertItem(twoThreeTreeItemType(self.tableLength(), item))

    def tableRetrieve(self, key):
        return self.tree.retrieveItem(key)

    def traverseTable(self, functie):
        return self.tree.inorderTraverse(functie)

    def createTable(self):
        self.tree = TwoThreeTree()

    def destroyTable(self):
        if self.tree is not None:
            self.tree = None
            return True
        else:
            return False

    def tableLength(self):
        values = self.tree.inorderTraverse(None)
        amount = 0
        for i in range(len(values)):
            amount += len(values[i])
        return amount

    def save(self):
        return self.tree.save()

    def load(self, tree):
        return self.tree.load(tree)

    def tableDelete(self, key):
        return self.tree.deleteItem(key)

if __name__ == "__main__":
    t = TwoThreeTreeTable()
    print(t.tableIsEmpty())
    print(t.tableInsert(createTreeItem(8, 8)))
    print(t.tableInsert(createTreeItem(5, 5)))
    print(t.tableIsEmpty())
    print(t.tableRetrieve(5)[0])
    print(t.tableRetrieve(5)[1])
    t.traverseTable(print)
    print(t.save())
    t.load({'root': [10], 'children': [{'root': [5]}, {'root': [11]}]})
    t.tableInsert(createTreeItem(15, 15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())
