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

def maxPathSum(root: Node, maxSum: int) -> tuple[int, int]:
    if not root:
        return (0, float('-inf'))   # gain = 0, max sum = -∞
    leftMaxGainPathSum, left_max = maxPathSum(root.left, maxSum)
    rightMaxGainPathSum, right_max = maxPathSum(root.right, maxSum)
    
    # Negative gains should be treated as 0
    leftMaxGainPathSum = max(0, leftMaxGainPathSum)
    rightMaxGainPathSum = max(0, rightMaxGainPathSum)
    
    current_path = root.data + leftMaxGainPathSum + rightMaxGainPathSum
    max_sum = max(current_path, left_max, right_max)
    
    gain_to_parent = root.data + max(leftMaxGainPathSum, rightMaxGainPathSum)
    
    return (gain_to_parent, max_sum)

print(maxPathSum(root, 0))

# def longestPath(root: Node) -> tuple[int, int]:
#     if not root:
#         return (0,0)
#     leftLongest, leftDepth = longestPath(root.left)
#     rightLongest, rightDepth = longestPath(root.right)
#     currentLongestPath = max(leftDepth + rightDepth, leftLongest, rightLongest)
#     return (currentLongestPath, (1 + max(leftDepth, rightDepth)))

# a, b = longestPath(root)
# print(a, b)