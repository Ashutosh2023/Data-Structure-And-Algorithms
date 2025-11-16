class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create nodes
root = Node(4)
node9 = Node(9)
node0 = Node(0)
node5 = Node(5)
node1 = Node(1)

# Connect nodes to match the image
root.left = node9
root.right = node0

node9.left = node5
node9.right = node1

# Final Tree:
#         (4)
#        /   \
#     (9)     (0)
#     / \
#   (5) (1)


def isLeaf(node: Node) -> bool:
    """Checks if a node is a leaf."""
    return node.left is None and node.right is None

def sumRootToLeafNumbers(root: Node, number: str) -> int:
    if not root:
        return 0
    current = number + str(root.data)
    print(root.data, "::", current)
    if isLeaf(root):
        print(current)
        return int(current)
    leftsum = sumRootToLeafNumbers(root.left, current)
    rightsum = sumRootToLeafNumbers(root.right, current)
    # print(root.data, "::", leftsum, rightsum)
        
    return leftsum + rightsum

def sumNumbers(root: Node):
    string = ""
    result = sumRootToLeafNumbers(root, string)
    print(result)

print(sumNumbers(root))