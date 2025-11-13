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
rightRightLeft = Node(23)

# Connect nodes to form the tree
root.left = leftChild
root.right = rightChild

leftChild.left = leftLeft
leftChild.right = leftRight

leftRight.left = leftRightLeft

rightChild.right = rightRight

rightRight.left = rightRightLeft

#           Root
#           (10)
#          /    \
#       (5)      (15)
#      /  \         \
#   (2)   (7)       (20)
#         /          /
#       (6)        (23)

def isLeaf(node: Node) -> bool:
    """Checks if a node is a leaf."""
    return node.left is None and node.right is None

def leftBoundary(root: Node, result: list[int]):
    current = root.left

    while current:
        if not isLeaf(current):
            result.append(current.data)

        if current.left:
            current = current.left
        else:
            current = current.right

def leafNodes(root: Node, result: list[int]):
    if root is None:
        return
    current: Node = root
    if isLeaf(current):
        result.append(current.data)
        return
    leafNodes(current.left, result)
    leafNodes(current.right, result)

def rightBoundary(root: Node, result: list[int]):
    current: Node = root.right
    temp = []
    while current:
        if not isLeaf(current):
            temp.append(current.data)
        
        if current.right:
            current = current.right
        else:
            current = current.left
    temp.reverse()
    result.extend(temp)

def BoundaryTraversalOfBTree(root: Node) -> list[int]:
    result = []
    if root is None:
        return []

    if not isLeaf(root):
        result.append(root.data)

    leftBoundary(root, result)
    leafNodes(root, result)
    rightBoundary(root, result)
    print(result)



BoundaryTraversalOfBTree(root)