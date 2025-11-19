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


def inOrderTraversal(root: Node):
    if not root:
        return []
    left_values = inOrderTraversal(root.left)
    right_values = inOrderTraversal(root.right)

    return left_values + [root.data] + right_values

print(inOrderTraversal(root))

def getSuccessor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def deleteNode(root: Node, key: int) -> Node:
    if root is None:
        return root
    
    if root.data > key:
        root.left = deleteNode(root.left, key)
    elif root.data < key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        succ = getSuccessor(root)
        root.data = succ.data
        root.right = deleteNode(root.right, succ.data)
    return root

deleteNode(root, 3)


print(inOrderTraversal(root))