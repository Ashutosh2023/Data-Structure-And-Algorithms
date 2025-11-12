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


def zigzagLevelOrder(root: Node) -> list[list[int]]:
    if not root:
        return []
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

# print(zigzagLevelOrder(root))

def zigzagLevelOrder2(root: Node) -> list[list[int]]:
    if not root:
        return []
    result = []
    Queue = [root]
    left_to_right  = True
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
        
        if not left_to_right :  #instead of reversing the whole queue just reverse the level nodes and insert
            level_nodes.reverse() 

        result.append(level_nodes)
        left_to_right  = not left_to_right 
    return result

print(zigzagLevelOrder2(root))