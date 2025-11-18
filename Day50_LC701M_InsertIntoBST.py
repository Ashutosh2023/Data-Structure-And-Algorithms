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

# BST:
#           (8)
#         /     \
#       (3)     (10)
#      /   \        \
#    (1)   (6)      (14)
#          / \      /
#        (4) (7)  (13)


def insertIntoBST(root: Node, val: int) -> Node:
    if not root:
        return Node(val)
    if root.data < val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    return root

insertIntoBST(root, 15)

def preOrderTraversal(root: Node):
    if not root:
        return []
    left_values = preOrderTraversal(root.left)
    right_values = preOrderTraversal(root.right)

    return [root.data] + left_values + right_values
print(preOrderTraversal(root))