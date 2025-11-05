class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create nodes
root = Node(10)
leftChild = Node(5)
rightChild = Node(15)
leftLeft = Node(2)
leftRight = Node(7)
leftRightLeft = Node(6)
rightRight = Node(20)

# Connect nodes to form the tree
root.left = leftChild
root.right = rightChild

leftChild.left = leftLeft
leftChild.right = leftRight

leftRight.left = leftRightLeft

rightChild.right = rightRight


#           Root
#           (10)
#          /    \
#       (5)      (15)
#      /  \         \
#   (2)   (7)       (20)
#         /
#       (6)



# Depth First // PreOrder Traversal (Root::Left::Right) :
def preOrderTraversal(root: Node):
    if not root:
        return []
    left_values = preOrderTraversal(root.left)
    right_values = preOrderTraversal(root.right)

    return [root.data] + left_values + right_values
# InOrder Traversal (Left::Root::Right) :
def inOrderTraversal(root: Node):
    if not root:
        return []
    left_values = inOrderTraversal(root.left)
    right_values = inOrderTraversal(root.right)

    return left_values + [root.data] + right_values
# PostOrder Traversal (Left::Right::Root) :
def postOrderTraversal(root: Node):
    if not root:
        return []
    left_values = postOrderTraversal(root.left)
    right_values = postOrderTraversal(root.right)

    return left_values + right_values + [root.data]


print(preOrderTraversal(root))
print(inOrderTraversal(root))
print(postOrderTraversal(root))