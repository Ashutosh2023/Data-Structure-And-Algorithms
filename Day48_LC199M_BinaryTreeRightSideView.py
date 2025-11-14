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


def rightSideview(root: Node) -> list[int]:
    if not root:
        return []
    result = []
    Queue = [root]
    while len(Queue) > 0:
        level_size = len(Queue)
        level_nodes = []
        for _ in range(level_size):
            current = Queue.pop(0)
            level_nodes.append(current.data)
            if current.left:
                Queue.append(current.left)
            if current.right:
                Queue.append(current.right)
        result.append(level_nodes[-1])
    return result
    

print(rightSideview(root))