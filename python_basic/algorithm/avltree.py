# %%
class AVLTree:
    class AVLNode:
        def __init__(self, item, height=0, left=None, right=None):
            self.item = item
            self.height = height
            self.left = left
            self.right = right
            self.parent = None

        def getItem(self):
            return self.item
        def setItem(self, newitem):
            self.item = newitem
        def getHeight(self):
            return self.height
        def setHeight(self, newheight):
            self.height = newheight
        def getLeft(self):
            return self.left
        def setLeft(self, newleft):
            self.left = newleft
        def getRight(self):
            return self.right
        def setRight(self, newright):
            self.right = newright
        def getParent(self):
            return self.parent
        def setParent(self, newParent):
            self.parent = newParent

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item, self.height

            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "AVLTree.AVLNode(" + repr(self.item) + ",height=" + repr(
                self.height) + ",left=" + repr(self.left) + ",right=" + repr(
                    self.right) + ")"

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def __getHeight(node):
        if node == None:
            return -1
        else:
            return node.getHeight()

    def find(self, item):
        def __find(root, item):
            if root == None:
                return False
            if item == root.getItem():
                return True
            if item < root.getItem():
                return __find(root.getLeft(), item)
            else:
                return __find(root.getRight(), item)

        return __find(self.root, item)

    def __rotateLeft(node):
        child = node.getRight()
        node.setRight(child.getLeft())
        child.setLeft(node)
        child.setParent(node.getParent())
        node.setParent(child)

        parent = node.getParent()
        if parent.getLeft() == node:
            parent.setLeft(child)
        elif parent.getRight() == node:
            parent.setRight(child)

        node.setHeight(max(AVLTree.__getHeight(node.getLeft()), AVLTree.__getHeight(node.getRight())) + 1)
        child.setHeight(max(AVLTree.__getHeight(child.getLeft()), AVLTree.__getHeight(child.getRight())) + 1)
        return child

    def __rotateRight(node):
        child = node.getLeft()
        node.setLeft(child.getRight())
        child.setRight(node)
        child.setParent(node.getParent())
        node.setParent(child)

        node.setHeight(max(AVLTree.__getHeight(node.getLeft()), AVLTree.__getHeight(node.getRight())) + 1)
        child.setHeight(max(AVLTree.__getHeight(child.getLeft()), AVLTree.__getHeight(child.getRight())) + 1)
        return child

    def __rotateLeftRight(node):
        # FIXME
        node = AVLTree.__rotateLeft(node.getLeft())
        return AVLTree.__rotateRight(node.getParent())
    
    def __rotateRightLeft(node):
        node = AVLTree.__rotateRight(node.getRight()).getParent()
        return AVLTree.__rotateLeft(node)

    def __rebalance(subtree):
        difference = AVLTree.__getHeight(subtree.getLeft()) - AVLTree.__getHeight(subtree.getRight())
        if difference <= 1 and difference >= -1:
            return subtree
        elif difference >= 2:
            if AVLTree.__getHeight(subtree.getLeft().getLeft()) > AVLTree.__getHeight(subtree.getLeft().getRight()):
                subtree = AVLTree.__rotateRight(subtree)
            else:
                subtree = AVLTree.__rotateLeftRight(subtree)
        elif difference <= -2:
            if AVLTree.__getHeight(subtree.getRight().getLeft()) > AVLTree.__getHeight(subtree.getRight().getRight()):
                subtree = AVLTree.__rotateRightLeft(subtree)
            else:
                subtree = AVLTree.__rotateLeft(subtree)
        subtree.setHeight(max(AVLTree.__getHeight(subtree.getLeft()), AVLTree.__getHeight(subtree.getRight())) + 1)
        return subtree

    def insert(self, item):
        if self.root == None:
            self.root = AVLTree.AVLNode(item)
        else:
            self.root = AVLTree.__insert(self.root, item)

    def __insert(subtree, item, parent=None):
        if item < subtree.getItem():
            if subtree.getLeft() != None:
                AVLTree.__insert(subtree.getLeft(), item, subtree)
                subtree.setHeight(max(AVLTree.__getHeight(subtree.getLeft()), AVLTree.__getHeight(subtree.getRight())) + 1)
                subtree = AVLTree.__rebalance(subtree)
            else:
                newTree = AVLTree.AVLNode(item)
                newTree.setParent(subtree)
                subtree.setLeft(newTree)
        elif item > subtree.getItem():
            if subtree.getRight() != None:
                AVLTree.__insert(subtree.getRight(), item, subtree)
                subtree.setHeight(max(AVLTree.__getHeight(subtree.getLeft()), AVLTree.__getHeight(subtree.getRight())) + 1)
                subtree = AVLTree.__rebalance(subtree)
            else:
                newTree = AVLTree.AVLNode(item)
                newTree.setParent(subtree)
                subtree.setRight(newTree)
        subtree.setHeight(max(AVLTree.__getHeight(subtree.getLeft()), AVLTree.__getHeight(subtree.getRight())) + 1)
        return subtree

    def delete(self, item):
        self.root = AVLTree.__delete(self.root, item)

    def __delete(subtree, item):
        if subtree == None:
            return
        if item < subtree.getItem():
            AVLTree.__delete(subtree.getLeft(), item)
            subtree = AVLTree.__rebalance(subtree)
        elif item > subtree.getItem():
            AVLTree.__delete(subtree.getRight(), item)
            subtree = AVLTree.__rebalance(subtree)
        
        elif item == subtree.getItem():
            if subtree.getLeft() == None and subtree.getRight() == None:
                # subtree is a leave
                parent = subtree.getParent()
                if parent.getLeft() == subtree:
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
                subtree = None
            elif subtree.getLeft() != None and subtree.getRight() == None:
                # subtree has two children
                child = subtree.getLeft()
                while child.getRight() != None:
                    child = child.getRight()
                subtree.setItem(child.getItem())
                AVLTree.__delete(subtree.getLeft(), child.getItem())
                subtree = AVLTree.__rebalance(subtree)
            else:
                # subtree has one child
                parent = subtree.getParent()
                if parent.getLeft() == subtree:
                    if subtree.getLeft() == None:
                        parent.setLeft(subtree.getRight())
                    else:
                        parent.setLeft(subtree.getLeft())
                else:
                    if subtree.getLeft() == None:
                        parent.setRight(subtree.getRight())
                    else:
                        parent.setRight(subtree.getLeft())                        
        if subtree != None:
            return AVLTree.__rebalance(subtree)
        return subtree

# %%
tree = AVLTree()
for x in [8,4,2,1,6,3,7,19,24]:
    tree.insert(x)
for x in tree:
    print(x)
tree.delete(8)
for x in tree:
    print(x)




# %%
