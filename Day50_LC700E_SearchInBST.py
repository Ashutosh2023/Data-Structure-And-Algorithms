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

def searchInBST(root: Node, val: int) -> Node:
    if not root:
        return None
    if root.data == val:
        return root
    if root.data > val and root.left:
        return searchInBST(root.left, val)
    elif root.data < val and root.right:
        return searchInBST(root.right, val)
    else:
        return None


result = searchInBST(root, 4)
if result:
    print(result.data)
else:
    print(None)