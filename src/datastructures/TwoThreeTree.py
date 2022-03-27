# 2-3-boom (Two-Three-Tree)

class twoThreeTreeItemType:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class Node:
    def __init__(self, item1, item2, temp = None):  # temp staat hiertussen voor te debuggen
        self.item1 = item1
        self.item2 = item2
        self.tempItem3 = temp  # self temporary derde item (voor dat de Node split)
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.prev = None


def createTreeItem(key, val):  # enkel voor inginious
    newItem = twoThreeTreeItemType(key, val)
    return newItem


class TwoThreeTree:
    # IK WERK NIET MEER MET DICTIONARYS MAAR MET ITEMS DIE NAAR ELKAAR WIJZEN
    def __init__(self):
        self.size = 0  # standaard 0, == aantal items -> NIET AANTAL NODES
        self.headPtr = None  # zal altijd pointen naar het eerste element in de boom
        self.height = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def SplitNode(self, oldNode):
        leftNode = Node(oldNode.item1, None)
        rightNode = Node(oldNode.tempItem3, None)

        oldNode.item1 = oldNode.item2
        oldNode.item2 = None
        oldNode.tempItem3 = None

        oldNode.child1 = leftNode
        oldNode.child2 = rightNode

        leftNode.prev = oldNode
        rightNode.prev = oldNode

        # NODE SUCCESFULLY SPLIT

        if oldNode.prev != None:
            # join the oldNode with its parent
            # oldnode should not exist after this, leftnode and rightnode should be in the correct child location
            parent = oldNode.prev
            if parent.item2 == None:
                if oldNode.item1.key < parent.item1.key:
                    parent.item2 = parent.item1
                    parent.item1 = oldNode.item1
                    # Now fix children
                    if parent.child1.item1.key == oldNode.item1.key:  # was left child
                        parent.child3 = parent.child2  # shift parents old right child
                        parent.child1 = leftNode
                        leftNode.prev = parent
                        parent.child2 = rightNode
                        rightNode.prev = parent
                    else:
                        print(
                            "ERROR: in function SplitNode, unexpected node location, expected the oldnode to be the left child")
                else:
                    parent.item2 = oldNode.item1
                    if parent.child2.item1.key == oldNode.item1.key:  # was right child
                        # parent leftchild stays leftchild
                        parent.child2 = leftNode
                        leftNode.prev = parent
                        parent.child3 = rightNode
                        rightNode.prev = parent
                    else:
                        print(
                            "ERROR: in function SplitNode, unexpected node location, expected the oldnode to be the right child")

            else:  # item2 of parent is filled
                if oldNode.item1.key < parent.item1.key:  # is left child
                    parent.tempItem3 = parent.item2
                    parent.item2 = parent.item1
                    parent.item1 = oldNode.item1

                    # skip the step where it temporarily becomes a 4 node before it splits again:
                    # -> to do this we will firstly split the 3 node  but not add it up until the parent is also split
                    # this is best visualized with a drawing
                    # step 1: split the node
                    # oldnode is already split

                    # step 2: split the parent
                    # make the new nodes for the other 2 values of parent that are split
                    parentRightChild = Node(parent.tempItem3, None)
                    parentRightChild.child1 = parent.child2
                    parentRightChild.child1.prev = parentRightChild
                    parentRightChild.child2 = parent.child3
                    parentRightChild.child2.prev = parentRightChild
                    parentRightChild.prev = parent
                    oldNode.prev = parent
                    # oldnode = left child, this means we don't need to create that node
                    parent.child1 = oldNode
                    parent.child2 = parentRightChild
                    parent.child3 = None

                    # (step 3: reset parent items (because the items are its children now))
                    parent.item1 = parent.item2
                    parent.item2 = None
                    parent.item3 = None


                elif oldNode.item1.key < parent.item2.key:  # is middle child

                    """
                    Special case:
                    oldNode will become the parent of parent, BUT the children will be distributed:
                    oldNode's leftchild will become the right child of parent.leftchild
                    oldNode's rightchild will become the left child of parent.rightchild

                    oldNode's leftchild is now Node(parent.item1, None) -> ParentNewLeft
                    oldNode's rightchild is now Node(parent.item2, None)-> ParentNewRight
                    """

                    # step 1: split parent
                    ParentNewLeft = Node(parent.item1, None)
                    ParentNewRight = Node(parent.item2, None)

                    ParentNewLeft.child1 = parent.child1
                    ParentNewLeft.child1.prev = ParentNewLeft
                    ParentNewLeft.child2 = oldNode.child1
                    ParentNewLeft.child2.prev = ParentNewLeft

                    ParentNewRight.child1 = oldNode.child2
                    ParentNewRight.child1.prev = ParentNewRight
                    ParentNewRight.child2 = parent.child3
                    ParentNewRight.child2.prev = ParentNewRight

                    oldNode.child1 = ParentNewLeft
                    oldNode.child2 = ParentNewRight
                    oldNode.prev = parent.prev
                    oldNode.child3 = None

                    ParentNewRight.prev = oldNode
                    ParentNewLeft.prev = oldNode

                    # there shouldn't be any connection to (old)parent anymore

                else:  # is right child
                    # works as the opposite of "is left child"
                    parent.tempItem3 = oldNode

                    parentLeftChild = Node(parent.item1, None)
                    parentLeftChild.child1 = parent.child1
                    parentLeftChild.child1.prev = parentLeftChild
                    parentLeftChild.child2 = parent.child2
                    parentLeftChild.child2.prev = parentLeftChild
                    parentLeftChild.prev = parent
                    oldNode.prev = parent
                    # oldNode is parentRightChild
                    parent.child1 = parentLeftChild
                    parent.child2 = oldNode
                    parent.child3 = None

                    # (step 3: reset parent items (because the items are its children now))
                    parent.item1 = parent.item2
                    parent.item2 = None
                    parent.item3 = None

    def insertItem(self, treeItem):
        if self.headPtr == None:
            node = Node(treeItem, None)
            self.headPtr = node
            self.size += 1
            return True #gelukt
        else:
            def addItem(currentNode, item):
                """
                Blijft door de nodes loopen tot het de correcte Node vind om in te gaan
                """
                if treeItem.key < currentNode.item1.key:
                    # first check if the node has children, if it does -> move to children
                    # check if node is full
                    # if node is not full:
                    # shift item1 to item2, insert newItem into item1
                    # if node is full:
                    # place the new item in the correct place in the node so there are 3 items from small to large:
                    # call function SplitNode

                    if currentNode.child1 == None and currentNode.child2 == None:
                        # does not have children, add to this node in the correct place
                        if currentNode.item2 == None:  # not full
                            currentNode.item2 = currentNode.item1
                            currentNode.item1 = item
                        else:  # node = full
                            # shift alle items en plaats newitem in item1
                            currentNode.tempItem3 = currentNode.item2
                            currentNode.item2 = currentNode.item1
                            currentNode.item1 = item
                            # nu staan ze correct gerangschikt
                            if currentNode.item1 != None and currentNode.item2 != None and currentNode.tempItem3 != None:
                                self.SplitNode(currentNode)
                            # call splitnode
                    else:
                        addItem(currentNode.child1, treeItem)

                elif treeItem.key > currentNode.item1.key:
                    if currentNode.item2 == None or treeItem.key < currentNode.item2.key:
                        if currentNode.child1 == None and currentNode.child2 == None:
                            # does not have children, add to this node in the correct place
                            # shift alle items en plaats newitem in item2
                            currentNode.tempItem3 = currentNode.item2
                            currentNode.item2 = item
                            # nu staan ze correct gerangschikt
                            if currentNode.item1 != None and currentNode.item2 != None and currentNode.tempItem3 != None:
                                self.SplitNode(currentNode)
                            # call splitnode
                        else:
                            addItem(currentNode.child2, treeItem)

                    elif currentNode.item2 != None and treeItem.key > currentNode.item2.key:
                        if currentNode.child1 == None and currentNode.child2 == None:
                            # does not have children, add to this node in the correct place
                            # shift alle items en plaats newitem in item2
                            currentNode.tempItem3 = item
                            # nu staan ze correct gerangschikt
                            if currentNode.item1 != None and currentNode.item2 != None and currentNode.tempItem3 != None:
                                self.SplitNode(currentNode)
                            else:
                                print("Error: in insert item (2-3) tree expected overfull Node")
                            # call splitnode
                        else:
                            addItem(currentNode.child3, treeItem)
                    else:
                        print("ERROR in insert item 2-3Tree")

            self.size += 1 # everytime insert is called an item is added
            addItem(self.headPtr, treeItem)
            return True # gelukt

    def retrieveItem(self, key):
        """
        retrieve using key, output the value
        :param key:
        :return:
        """
        def search(Node,key):
            if key == Node.item1.key:
                return(Node.item1.val, True)
            if Node.item2 != None:
                if key == Node.item2.key:
                    return(Node.item2.val, True)
            if Node.child1 != None:     # has children
                if key<Node.item1.key:
                    return search(Node.child1,key)
                elif key>Node.item1.key:
                    if Node.item2 == None:
                        return search(Node.child2,key)
                    else:
                        if key<Node.item2.key:
                            return search(Node.child2,key)
                        else:
                            return search(Node.child3,key)
            else:                      # has no children
                return(None,False)

        return search(self.headPtr, key)

    def inorderTraverse(self, functie):  # functie is bijvoorbeeld "print"
        values = []
        def traverse(Node):
            if Node.child1 != None:
                traverse(Node.child1)
                nodeVal = []
                nodeVal.append(Node.item1.val)
                if Node.item2 != None:
                    nodeVal.append(Node.item2.val)
                values.append(nodeVal)
                traverse(Node.child2)
                if Node.item2 != None:
                    # is 3 node
                    traverse(Node.child3)
            else:
                nodeVal = []
                nodeVal.append(Node.item1.val)
                if Node.item2 != None:
                    nodeVal.append(Node.item2.val)
                values.append(nodeVal)

        traverse(self.headPtr)
        if functie != None:
            for i in range(len(values)):
               functie(values[i][0])
               if len(values[i]) == 2:
                   functie(values[i][1])
        """
        functie(values[0][0])
        if len(values[0]) == 2:
            functie(values[0][1])
        """

        return values

    def deleteItem(self, key):

        def searchToDelete(Node,key):
            if key == Node.item1.key:
                return Node
            if Node.item2 != None:
                if key == Node.item2.key:
                    return Node
            if Node.child1 != None: # has children
                if key<Node.item1.key:
                    return searchToDelete(Node.child1,key)
                elif key>Node.item1.key:
                    if Node.item2 == None:
                        return searchToDelete(Node.child2,key)
                    else:
                        if key<Node.item2.key:
                            return searchToDelete(Node.child2,key)
                        else:
                            return searchToDelete(Node.child3,key)
            else:                   # has no children
                return False

        toBeDeleted = searchToDelete(self.headPtr, key) # returns the node in which the item sits
        # the item could be either item1 or item2
        if toBeDeleted == False:
            return False

        # find inorder successor
        if toBeDeleted.child1 != None:  # only if it is not a leaf
            values = self.inorderTraverse(None) # lijst van alle nodes in inorder, eerstvolgende node is successor
            for i in range(len(values)):
                # get inorder successor -> next item from the key
                # example: values: 1, 2 ,4, 6, 7; toBeDeletedKey == 6, succ = 7
                if len(values[i]) == 1:
                    if values[i][0] != key:
                        continue
                    else:
                        if len(values) > i + 1:
                            inorderSuc = values[i + 1]
                            break
                        else:
                            inorderSuc = values[i]  # set to itself, is al een blad
                            break
                else:
                    if values[i][0] != key and values[i][1] != key:
                        continue
                    else:
                        if len(values) > i + 1:
                            inorderSuc = values[i + 1]
                            break
                        else:
                            inorderSuc = values[i]  # set to itself, is al een blad
                            break

            # swap with inorderSuc
            successor = searchToDelete(self.headPtr, inorderSuc[0]) # no need to check if its a 3 node, always swap with item1 (smallest)
            tempVal = successor.item1
            if toBeDeleted.item1.key == key:
                successor.item1 = toBeDeleted.item1
                toBeDeleted.item1 = tempVal
                toBeDeleted = successor
            else:
                successor.item1 = toBeDeleted.item2
                toBeDeleted.item2 = tempVal
                toBeDeleted = successor
            # swap done

        def AddItemtoNode(node, item):
            if node.item2 == None:
                # is 2 node
                if node.item1.key < item.key:
                    node.item2 = item
                    return True
                else:
                    node.item2 = node.item1
                    node.item1 = item
                    return True
            else:
                # is 3 node
                if node.item1.key < item.key:
                    if node.item2.key < item.key:
                        node.tempItem3 = item
                        self.SplitNode(node)
                        return True
                    else:
                        node.tempItem3 = node.item2 #shift one
                        node.item2 = item
                        self.SplitNode(node)
                        return True
                else:
                    node.tempItem3 = node.item2
                    node.item2 = node.item1
                    node.item1 = item
                    self.SplitNode(node)
                    return True

        def gevalCheck(node):
            # node is toBeDeleted
            parent = node.prev
            if parent == None and toBeDeleted.item2 == None:      # node is the only node in the tree
                self.headPtr = None # delete node from tree -> tree = empty
                self.size = 0
                return True

            if toBeDeleted.item2 != None:
                # toBeDeleted is a leaf AND is a 3 node -> delete one of the items
                if toBeDeleted.item1.key == key:
                    toBeDeleted.item1 = toBeDeleted.item2
                    toBeDeleted.item2 = None
                    return True
                else:
                    toBeDeleted.item2 = None
                    return True
                # done

            # START REAL CHECK:

            if parent.item2 != None:
                # parent is 3node
                # find out which dubbelGeval to use
                if parent.child1.item1.key == node.item1.key:
                    dubbelGeval1(node)
                    return True
                elif parent.child2.item1.key == node.item1.key:
                    dubbelGeval2(node)
                    return True
                elif parent.child3.item1.key == node.item1.key:
                    dubbelGeval3(node)
                    return True
            else:
                # parent is 2 node
                if parent.child1.item1.key == node.item1.key:
                    # left child = to be deleted
                    Geval1(node)
                    return True
                elif parent.child2.item1.key == node.item1.key:
                    # right child = to be deleted
                    Geval2(node)
                    return True
                else:   # none of the childrenn = tobedeleted
                    print("Error")
                    return False

        def dubbelGeval1(node):
            # geval1: parent is 3node, left child to be deleted
            # merge parent.item1 met child2, (child2.item2 = child2.item1, child2.item1 = parent.item1)
            # parent.child1 = parent.child2, parent.child2 = parent.child3
            parent = node.prev
            AddItemtoNode(parent.child2, parent.item1)
            parent.item1 = parent.item2
            parent.item2 = None
            parent.child1 = parent.child2
            parent.child2 = parent.child3
            parent.child3 = None
            return True

        def dubbelGeval2(node):
            # geval2: parent is 3node, middle child to be deleted
            # merge parent.item1 met child1
            # parent.child2 = parent.child3
            parent = node.prev
            AddItemtoNode(parent.child1, parent.item1)
            parent.item1 = parent.item2
            parent.item2 = None
            parent.child2 = parent.child3
            parent.child3 = None
            return True

        def dubbelGeval3(node):
            # geval3: parent is 3node, right child to be deleted
            # merge parent.item2 met child2 ( child2.item2 = parent.item2 )
            #
            parent = node.prev
            AddItemtoNode(parent.child2, parent.item2)
            parent.item2 = None
            parent.child3 = None
            return True

        def Geval1Step2(node):
            parent = node.prev
            grandparents = parent.prev
            if grandparents == None:
                return True

            if grandparents.item2 == None:  # grandparents = 2 node
                # find sibling
                if grandparents.child1.item1 == None:
                    sibling = grandparents.child2
                    par = "leftchild"   # parent is the leftchild
                else:
                    sibling = grandparents.child1
                    par = "rightchild"  # parent is the rightchild

                if sibling.item2 == None:
                                                                            # COULD NEED A PARENT OF GRANDPARENT CHECK
                    #if grandparents 2 node, sibling of parent is 2 node:
                    # add grandparents to sibling of parent,
                    # add node(merged) to child3 of new parent sibling(3node now)
                    if par == "leftchild":
                        # parent is leftchild
                        AddItemtoNode(sibling, grandparents.item1)
                        sibling.child3 = sibling.child2
                        sibling.child2 = sibling.child1
                        sibling.child1 = node
                        node.prev = sibling
                        sibling.prev = grandparents.prev
                        if sibling.prev == None:
                            self.headPtr = sibling
                        return True
                    else:
                        # parent is rightchild
                        AddItemtoNode(sibling, grandparents.item1)
                        sibling.child3 = node
                        node.prev = sibling
                        sibling.prev = grandparents.prev
                        if sibling.prev == None:
                            self.headPtr = sibling
                        return True
                    # done

                else:
                    #if grandparents 2 node, sibling of parent is 3 node:
                    # rotate
                    # new grandparents is middle item of old parents sibling
                    # new parent = right child of grandparents
                    # new parent sibling = left child of grandparents
                    # add node(merged) to parent child2 (empty at first)
                    if par == "leftchild":
                        # parent is leftchild
                        parent.item1 = grandparents.item1
                        grandparents.item1 = sibling.item1
                        sibling.item1 = sibling.item2
                        sibling.item2 = None    # circle done
                        parent.child1 = node    # shift
                        parent.child2 = sibling.child1
                        sibling.child1 = sibling.child2
                        sibling.child2 = sibling.child3
                        sibling.child3 = None
                        return True
                    else:
                        # parent is rightchild
                        parent.item1 = grandparents.item1
                        grandparents.item1 = sibling.item2
                        sibling.item2 = None
                        parent.child1 = sibling.child3
                        sibling.child3.prev = parent
                        return True
                    # done
            else:
                # grandparents = 3 node
                # find sibling
                if grandparents.child1.item1 == None:
                    sibling = grandparents.child2   # sibling is middle child
                    par = "leftchild"  # parent is the leftchild
                elif grandparents.child3.item1 == None:
                    sibling = grandparents.child2   # sibling is middle child
                    par = "rightchild"  # parent is the rightchild
                elif grandparents.child2.item1 == None:
                    sibling = grandparents.child1
                    par = "middlechild"
                else:
                    return False

                if sibling.item2 == None:
                    # sibling is 2 node
                    if par == "rightchild":
                        #if grandparents 3 node, parent is right child of gp, sibling of parent(middle child of grandparents) is 2 node:
                        # add grandparents.item2 to sibling of parent,
                        # add node(merged) to child3 of new parent sibling(3node now)
                        sibling.item2 = grandparents.item2
                        grandparents.item2 = None
                        sibling.child3 = node
                        node.prev = sibling
                        return True
                        # done
                    elif par == "middlechild":
                        # parent is mid child of gp
                        # add grandparents.item1 to sibling of parent(left child of gp),
                        # add node to child3 of new parent sibling
                        sibling.item2 = grandparents.item1
                        grandparents.item1 = grandparents.item2
                        grandparents.item2 = None
                        sibling.child3 = node
                        grandparents.child2 = grandparents.child3
                        node.prev = sibling
                        return True
                        # done
                    elif par == "leftchild":
                        # parent is left child of gp
                        # add gp.item1 to sibling of parent(mid child of gp),
                        # add node to child1 of new parent sibling
                        sibling.item2 = sibling.item1
                        sibling.item1 = grandparents.item1
                        grandparents.item1 = grandparents.item2
                        grandparents.item2 = None
                        grandparents.child1 = grandparents.child2
                        grandparents.child2 = grandparents.child3
                        sibling.child3 = sibling.child2
                        sibling.child2 = sibling.child1
                        sibling.child1 = node
                        node.prev = sibling
                        return True
                        # done
                    else:
                        print("what, how?")
                        return False
                else:
                    # sibling is 3 node
                    if par == "rightchild":
                        # if grandparents 3 node, parent is right child of gp, sibling of parent(middle child of grandparents) is 3 node:
                        # gp.item2 is new parent of node (node is right child)
                        # new parent.child1 = child3 of old sibling
                        # gp.item2 = child2(mid).item2
                        # they redistributed in a circle (turning right)
                        parent.item1 = grandparents.item2
                        grandparents.item2 = sibling.item2
                        sibling.item2 = None
                        parent.child1 = sibling.child3
                        parent.child1.prev = parent
                        sibling.child3 = None
                        return True
                        # done
                    elif par == "middlechild":
                        # parent is mid child of gp
                        # add grandparents.item1 to sibling of parent(left child of gp),
                        # add node to child3 of new parent sibling
                        parent.item1 = grandparents.item1
                        grandparents.item1 = sibling.item2
                        sibling.item2 = None
                        parent.child1 = sibling.child3
                        parent.child1.prev = parent
                        sibling.child3 = None
                        return True
                        # done
                    elif par == "leftchild":
                        # gp.item1 is new parent of node (node is left child)
                        # new parent.child2 = child1 of old sibling
                        # gp.item1 = child2(mid).item1
                        # they redistributed in a circle (turning left)
                        parent.item1 = grandparents.item1
                        grandparents.item1 = sibling.item1
                        sibling.item1 = sibling.item2
                        sibling.item2 = None
                        parent.child1 = node    # shift from right child to left
                        parent.child2 = sibling.child1
                        parent.child2.prev = parent
                        sibling.child1 = sibling.child2
                        sibling.child2 = sibling.child3
                        sibling.child3 = None
                        return True
                        # done
                    else:
                        print("what, how?")
                        return False
        def Geval1(node):
            # geval1: parent is 2node, left child to be deleted
            # merge parent(.item1) met right child
            # geval1Step2
            parent = node.prev
            if parent.child2.item2 == None:
                # sibling is 2 node
                parent.child1 = None    # to be deleted
                parent.child2.item2 = parent.child2.item1
                parent.child2.item1 = parent.item1
                parent.item1 = None     # empty parent
                Geval1Step2(parent.child2)
                return True
            else:
                # sibling is 3 node
                parent.child1.item1 = parent.item1  # to be deleted.item1 = parent.item1
                parent.item1 = parent.child2.item1
                parent.child2.item1 = parent.child2.item2
                parent.child2.item2 = None
                # no need to fix children, should only delete at the lowest level
                return True



        def Geval2(node):
            # geval2: parent is 2node, right child to be deleted
            # merge parent(.item1) met right child
            # geval1Step2
            parent = node.prev
            if parent.child2.item2 == None:
                # sibling is 2 node
                # parent.child2 is to be deleted, instead of making a mirrored copy of geval1Step2, swap the deleted child with the sibling
                parent.child2.item1 = parent.child1.item1 # set deleted child to sibling
                parent.child1 = None    # delete sibling
                parent.child2.item2 = parent.child2.item1
                parent.child2.item1 = parent.item1
                parent.item1 = None
                Geval1Step2(parent.child2)
                #because we used geval1's step 2
                #we need to swap parent.child2, items
                tempval = parent.child2.item1
                parent.child2.item1 = parent.child2.item2
                parent.child2.item2 = tempval
                # swap done
                return True
            else:
                # sibling is 3 node
                parent.child1.item1 = parent.item1  # to be deleted.item1 = parent.item1
                parent.item1 = parent.child2.item1
                parent.child2.item1 = parent.child2.item2
                parent.child2.item2 = None
                # no need to fix children, should only delete at the lowest level
                return True

        return gevalCheck(toBeDeleted)


    def updateHeight(self):
        """
        since it's a 2-3 tree it should ALWAYS be balanced, which makes it easy to count the height
        :return:
        """
        def runThrough(Node):
            if Node.child1 == None and Node.child2 == None:
                return 0
            else:
                return 1 + runThrough(Node.child1)


        self.height = runThrough(self.headPtr)

    def save(self):
        d = dict()

        def runTroughSave(Node,dicti):
            if Node != None:
                doubleNode = False
                l = list()
                l.append(Node.item1.val)
                if Node.item2 != None:
                    l.append(Node.item2.val)
                    doubleNode = True
                dicti["root"] = l

                if Node.child1 != None:
                    if doubleNode == False:
                        childr = list()
                        c1 = dict()
                        runTroughSave(Node.child1, c1)
                        childr.append(c1)
                        c2 = dict()
                        runTroughSave(Node.child2, c2)
                        childr.append(c2)

                        dicti["children"] = childr
                    else:
                        childr = list()
                        c1 = dict()
                        runTroughSave(Node.child1, c1)
                        childr.append(c1)
                        c2 = dict()
                        runTroughSave(Node.child2, c2)
                        childr.append(c2)
                        c3 = dict()
                        runTroughSave(Node.child3, c3)
                        childr.append(c3)

                        dicti["children"] = childr


        runTroughSave(self.headPtr,d)
        return d

    def load(self, Tree):
        """
        this feature is only for Inginious, so the key == the value
        """
        def runThroughLoad(tree, ptr):
            """
            tree == dictionary
            """
            if ptr == None:
                doubleNode = False
                Item = createTreeItem(tree["root"][0], tree["root"][0])
                Item2 = None
                tempItem3 = None
                if len(tree["root"]) == 2:
                    doubleNode = True
                    Item2 = createTreeItem(tree["root"][1], tree["root"][1])
                elif len(tree["root"]) == 3:
                    doubleNode = True
                    Item2 = createTreeItem(tree["root"][1], tree["root"][1])
                    tempItem3 = createTreeItem(tree["root"][2], tree["root"][2])
                parentNode = Node(Item, Item2, tempItem3)
                ptr = parentNode
                self.size += 1
            if "children" in tree:
                child1Ptr = None
                child2Ptr = None
                #search left first
                child1Ptr = runThroughLoad(tree["children"][0], child1Ptr)
                #search right
                child2Ptr = runThroughLoad(tree["children"][1], child2Ptr)
                #add children to parent
                # we will NOT add in old way because the child could instantly be a 3 node
                if doubleNode == False:
                    ptr.child1 = child1Ptr
                    child1Ptr.prev = ptr
                    ptr.child2 = child2Ptr
                    child2Ptr.prev = ptr
                else:
                    # there will actually be a third child
                    child3Ptr = None
                    child3Ptr = runThroughLoad(tree["children"][2], child3Ptr)
                    ptr.child1 = child1Ptr
                    child1Ptr.prev = ptr
                    ptr.child2 = child2Ptr
                    child2Ptr.prev = ptr
                    ptr.child3 = child3Ptr
                    child3Ptr.prev = ptr

            return ptr
        self.size = 0
        self.headPtr = runThroughLoad(Tree, None)
        self.updateHeight()

if __name__ == "__main__":
    t = TwoThreeTree()
    t.load({'root': [5], 'children': [{'root': [2], 'children': [{'root': [1]}, {'root': [3, 4]}]}, {'root': [12], 'children': [{'root': [10]}, {'root': [15]}]}]})
    print(len(t.inorderTraverse(None)))
    print(t.save())