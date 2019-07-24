class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        # We're assuming a value will be passed into define the binary tree and then  Setting the class var self.root = to a node of that. Converting whatever data is passed 
        # in and storing that into a node and setting that as the root of the tree.
        self.root = Nose(root)


#          1             r00t of tree
#       /     \
#       2      3
#     /  \    / \ 
#    4    5


tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)