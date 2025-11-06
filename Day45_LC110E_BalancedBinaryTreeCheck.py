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
def maxDepthAndBalance(root: Node)-> tuple[bool, int]:
    if root is None:
        return (True, 0)
    left_Balance, left_depth = maxDepthAndBalance(root.left)
    right_Balance, right_depth = maxDepthAndBalance(root.right)
    currentBalance = left_Balance and right_Balance and (abs(left_depth - right_depth) <= 1)
    currentDepth = max(left_depth, right_depth) + 1
    return (currentBalance, currentDepth)

def maxDepth(root: Node) -> bool:
    balance, depth = maxDepthAndBalance(root)
    return balance

# print(maxDepthAndBalance(root))

# Approach 2 return a flag can be -1 as depth won't be negative value 
class Solution:
    def isBalanced(self, root: Node) -> bool:
        """
        Checks if the entire tree is height-balanced.
        Calls the helper function and checks if the returned height is not -1.
        """
        return self._check_height(root) != -1

    def _check_height(self, root: Node) -> int:
        """
        Helper function that recursively calculates the height of the subtree.
        Returns the height if balanced, and returns -1 if unbalanced.
        """
        # Base Case: An empty tree has a height of 0 and is balanced.
        if root is None:
            return 0

        # Recursively get the height of the left subtree.
        left_height = self._check_height(root.left)
        
        # If the left subtree is already found to be unbalanced, pass the signal up.
        if left_height == -1:
            return -1

        # Recursively get the height of the right subtree.
        right_height = self._check_height(root.right)
        
        # If the right subtree is already found to be unbalanced, pass the signal up.
        if right_height == -1:
            return -1

        # Check the balance condition for the current node.
        # The absolute difference in height must not be greater than 1.
        if abs(left_height - right_height) > 1:
            return -1  # Signal unbalanced

        # If balanced, return the actual height of the current subtree.
        # Height is 1 (for the current node) + the maximum height of its children.
        return 1 + max(left_height, right_height)
    
print(Solution().isBalanced(root))