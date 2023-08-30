# 전위, 중위, 후위
class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
    
    def addLeft(self,Node):
        self.left = Node
    def addRight(self,Node):
        self.right = Node

class BinaryTree:
    def __init__(self,root):
        self.root = root

    def preOrder(self,n):
        print(n.item, ' ',end=' ')
        if n.left:
            self.preOrder(n.left)
        if n.right:
            self.preOrder(n.right)

    def inOrder(self,n):
        if n.left:
            self.inOrder(n.left)
        print(n.item, ' ',end=' ')
        if n.right:
            self.inOrder(n.right)
    
    def postOrder(self,n):
        if n.left:
            self.postOrder(n.left)
        if n.right:
            self.postOrder(n.right)
        print(n.item,' ',end=' ')
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')
a.addLeft(b)
a.addRight(c)
b.addLeft(d)
b.addRight(e)
e.addRight(h)
c.addLeft(f)
c.addRight(g)
g.addLeft(i)

node = BinaryTree(a)
node.preOrder(a)
print()
node.inOrder(a)
print()
