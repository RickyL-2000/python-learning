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

        child.setHeight(max(AVLTree.__getHeight(child.getLeft()), AVLTree.__getHeight(child.getRight())) + 1)
        node.setHeight(max(AVLTree.__getHeight(node.getLeft()), AVLTree.__getHeight(node.getRight())) + 1)
        node = child

    def __rotateRight(node):
        child = node.getLeft()
        node.setLeft(child.getRight())
        child.setRight(node)

        child.setHeight(max(AVLTree.__getHeight(child.getLeft()), AVLTree.__getHeight(child.getRight())) + 1)
        node.setHeight(max(AVLTree.__getHeight(node.getLeft()), AVLTree.__getHeight(node.getRight())) + 1)
        node = child

    def __rotateLeftRight(node):
        AVLTree.__rotateLeft(node.getLeft())
        AVLTree.__rotateRight(node)
    
    def __rotateRightLeft(node):
        AVLTree.__rotateRight(node.getRight())
        AVLTree.__rotateLeft(node)

    def __rebalance(subtree):
        difference = AVLTree.__getHeight(subtree.getLeft()) - AVLTree.__getHeight(subtree.getRight())
        if difference <= 1 and difference >= -1:
            return
        elif difference >= 2:
            if AVLTree.__getHeight(subtree.getLeft().getLeft()) > AVLTree.__getHeight(subtree.getLeft().getRight()):
                AVLTree.__rotateRight(subtree)
            else:
                AVLTree.__rotateLeftRight(subtree)
        elif difference <= -2:
            if AVLTree.__getHeight(subtree.getRight().getLeft()) > AVLTree.__getHeight(subtree.getRight().getRight()):
                AVLTree.__rotateRightLeft(subtree)
            else:
                AVLTree.__rotateLeft(subtree)
        subtree.setHeight(max(AVLTree.__getHeight(subtree.getLeft()), AVLTree.__getHeight(subtree.getRight())) + 1)

    def insert(self, item):
        def __insert(subtree, item, parent=None):
            if subtree == None:
                subtree = AVLTree.AVLNode(item)
                subtree.setParent(parent)
            elif item < subtree.getItem():
                __insert(subtree.getLeft(), item, subtree) # FIXME: 要不要写parent=subtree?
                AVLTree.__rebalance(subtree)
            elif item > subtree.getItem():
                __insert(subtree.getRight(), item, subtree)
                AVLTree.__rebalance(subtree)
            subtree.setHeight(max(AVLTree.__getHeight(subtree.getLeft()), AVLTree.__getHeight(subtree.getRight())) + 1)
        
        __insert(self.root, item)
    
    def delete(self, item):
        def __delete(subtree, item):
            if subtree == None:
                return
            if item < subtree.getItem():
                __delete(subtree.getLeft(), item)
                AVLTree.__rebalance(subtree)
            elif item > subtree.getItem():
                __delete(subtree.getRight(), item)
                AVLTree.__rebalance(subtree)
            
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
                    __delete(subtree.getLeft(), child.getItem())
                    AVLTree.__rebalance(subtree)
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
                AVLTree.__rebalance(subtree)

# %%
tree = AVLTree()
for x in [8,4,2,1,6,3,7,19,24]:
    tree.insert(x)
for x in tree:
    print(x)





# %%
