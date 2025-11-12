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
rightRightLeft = Node(21)

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
#         /           \
#       (6)           (21)


def LevelOrderTraversal(root: Node) -> list[list[int]]:
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
        result.append(level_nodes)
    return result


print(LevelOrderTraversal(root))

def zigzagLevelOrder(root: Node) -> list[list[int]]:
    if not root:
        return False
    result = []
    Queue = [root]
    flag = True
    while len(Queue) > 0:
        level_size = len(Queue)
        level_nodes = []
        Queue = Queue[::-1]
        flag = not flag
        for _ in range(level_size):
            current = Queue.pop(0)
            level_nodes.append(current.data)
            if flag:
                if current.right:
                    Queue.append(current.right)
                if current.left:
                    Queue.append(current.left)
            else:
                if current.left:
                    Queue.append(current.left)
                if current.right:
                    Queue.append(current.right)
        result.append(level_nodes)
    return result

print(zigzagLevelOrder(root))