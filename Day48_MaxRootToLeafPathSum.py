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
leftRight = Node(70)
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
#   (2)   (70)       (20)
#         /
#       (6)


def maxRootToLeafSum(root: Node):
    if not root:
        return float('-inf')
    if not root.left and not root.right:
        return root.data
    left_sum = maxRootToLeafSum(root.left)
    right_sum = maxRootToLeafSum(root.right)
    return root.data + max(left_sum, right_sum)

print(maxRootToLeafSum(root))