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


def LCA(root: Node, p: Node, q: Node)-> Node:
    if root is None:
        return None
    print(root.data, "::", end=" ")
    if root.data > p.data and root.data > q.data:
        print("left")
        return LCA(root.left, p, q)
    if root.data < p.data and root.data < q.data:
        print("right")
        return LCA(root.right, p, q)
    return root

result: Node = LCA(root, leftLeft, leftRightLeft)
print(result.data)