class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create nodes
root = Node(8)

root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right = Node(14)
root.right.right.left = Node(13)

# BST created:
#           (8)
#         /     \
#       (3)     (10)
#      /   \        \
#    (1)   (6)      (14)
#          / \      /
#        (4) (7)  (13)

def checkBST(node: Node, min_val: int, max_val: int)-> bool:
    if node is None:
        return True
    
    if node.data < min_val or node.data >max_val:
        return False

    return checkBST(node.left, min_val, node.data -1) and checkBST(node.right, node.data + 1, max_val)

def isValidBST(root: Node) -> int:
    return checkBST(root, float('-inf'), float('inf'))


print(isValidBST(root))