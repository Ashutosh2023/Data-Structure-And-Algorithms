class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


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


def depthFirstTraversalSearch(root: Node, target: int):
    if not root:
        return False
    if root.data == target:
        return True
    
    return depthFirstTraversalSearch(root.left, target) or depthFirstTraversalSearch(root.right, target)

print(depthFirstTraversalSearch(firstNode, 5))

def breadthFirstsearch(root: Node, target: int) -> bool:
    if not root:
        return False
    if root.data == target:
        return True
    Queue = [root]
    while len(Queue) > 0:
        current = Queue.pop(0)
        if current.data == target:
            return True
        if current.left:
            Queue.append(current.left)
        if current.right:
            Queue.append(current.right)
    return False

# print(breadthFirstsearch(firstNode, 5))


