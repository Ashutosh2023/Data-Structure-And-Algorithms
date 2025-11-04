class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Initialize and allocate memory for tree nodes
root = Node(5)
secondNode = Node(11)
thirdNode = Node(3)
fourthNode = Node(4)
sixthNode = Node(2)
seventhNode = Node(1)

# Connect binary tree nodes
root.left = secondNode
root.right = thirdNode
secondNode.left = fourthNode
secondNode.right = sixthNode
thirdNode.right = seventhNode


def maxRootToLeafSum(root: Node):
    if not root:
        return float('-inf')
    if not root.left and not root.right:
        return root.data
    left_sum = maxRootToLeafSum(root.left)
    right_sum = maxRootToLeafSum(root.right)
    return root.data + max(left_sum, right_sum)

print(maxRootToLeafSum(root))