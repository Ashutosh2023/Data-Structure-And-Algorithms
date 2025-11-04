class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)
sixthNode = Node(6)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode
secondNode.right = sixthNode


# Depth First Traversal : Use Stack
def depthFirstTraversal(root: Node):
    if not root:
        return []
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

# print(depthFirstTraversal(firstNode))

# def depthFirstTraversalRecur(root: Node):
#     if not root:
#         return
#     print(root.data)
#     depthFirstTraversalRecur(root.left)
#     depthFirstTraversalRecur(root.right)

def depthFirstTraversalRecur(root: Node):
    if not root:
        return []
    left_values = depthFirstTraversalRecur(root.left)
    right_values = depthFirstTraversalRecur(root.right)

    return [root.data] + left_values + right_values


result = depthFirstTraversalRecur(firstNode)
# print(result)


# Breadth First Traversal : Use Queue
def breadthFirstTraversal(root: Node):
    if not root:
        return[]
    Queue = [root]
    values = []
    while len(Queue) > 0:
        current = Queue.pop(0)
        values.append(current.data)
        if current.left:
            Queue.append(current.left)
        if current.right:
            Queue.append(current.right)
    return values

print(breadthFirstTraversal(firstNode))


