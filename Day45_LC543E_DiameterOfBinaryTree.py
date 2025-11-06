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
def longestPath(root: Node) -> tuple[int, int]:
    if not root:
        return (0,0)
    leftLongest, leftDepth = longestPath(root.left)
    rightLongest, rightDepth = longestPath(root.right)
    currentLongestPath = max(leftDepth + rightDepth, leftLongest, rightLongest)
    return (currentLongestPath, (1 + max(leftDepth, rightDepth)))

a, b = longestPath(root)
print(a, b)