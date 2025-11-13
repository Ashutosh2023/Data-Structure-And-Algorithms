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

def widthOfBinaryTree(root: Node) -> int:
    if not root:
        return []
    result = []
    Queue = [[root,1]]
    max_width = 0
    while len(Queue) > 0:
        level_size = len(Queue)
        level_nodes = []
        print(Queue[-1][1] - Queue[0][1])
        max_width = max(Queue[-1][1] - Queue[0][1] + 1, max_width)
        for _ in range(level_size):
            temp = Queue.pop(0)
            current = temp[0]
            idx = temp[1] - 1
            level_nodes.append(current.data)
            if current.left:
                Queue.append([current.left,2*idx+1])
            if current.right:
                Queue.append([current.right,2*idx+2])
        result.append(level_nodes)
        
    return max_width

print(widthOfBinaryTree(root))