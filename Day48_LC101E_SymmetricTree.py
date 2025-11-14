class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create nodes
root = Node(10)

# Left subtree
leftChild = Node(5)
leftLeft = Node(2)
leftRight = Node(7)
leftRightRight = Node(6)

# Right subtree (mirror of left)
rightChild = Node(5)
rightLeft = Node(7)
rightRight = Node(2)
rightLeftLeft = Node(6)

# Connect nodes to form the symmetric tree
root.left = leftChild
root.right = rightChild

# Left subtree connections
leftChild.left = leftLeft
leftChild.right = leftRight
leftRight.right = leftRightRight

# Right subtree connections (mirrored)
rightChild.left = rightLeft
rightChild.right = rightRight
rightLeft.left = rightLeftLeft


#           Root
#            (10)
#           /    \
#        (5)     (5)
#       /  \     /  \
#    (2)   (7) (7)   (2)
#          \         \
#          (6)       (6)



def rightSideview(root: Node) -> list[int]:
    if not root:
        return []
    result : bool = True
    Queue = [root]
    while len(Queue) > 0:
        level_size = len(Queue)
        level_nodes = []
        for _ in range(level_size):
            current = Queue.pop(0)
            if current == None:
                level_nodes.append(current)
                continue
            level_nodes.append(current.data)
            Queue.append(current.left)
            Queue.append(current.right)
        result = level_nodes == list(reversed(level_nodes)) and result
        print(level_nodes, result)
    return result
    

print(rightSideview(root))