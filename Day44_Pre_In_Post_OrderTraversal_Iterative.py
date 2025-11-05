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



# Depth First // PreOrder Traversal (Root::Left::Right) :
def preOrderTraversal(root: Node):
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
# InOrder Traversal (Left::Root::Right) :
def inOrderTraversal(root: Node):
    if not root:
        return []
    result = []
    current : Node = root
    stack = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) == 0:
                break
            current = stack.pop()
            result.append(current.data)
            current = current.right

    return result
# PostOrder Traversal (Left::Right::Root) :
def postOrderTraversal(root: Node): 
    if not root:
        return []
    result = []
    current : Node = root
    stack : list[Node] = []
    while current or len(stack):
        if current:
            stack.append(current)
            current = current.left  # takes you to the last left leaf node
        else:
            temp = stack[-1].right   # since left is none then check right, if right is there can check it's left
            if temp is None: #if right is also none then it is a leaf node
                temp = stack.pop()   # insert that leaf node in the result can be left node or right node
                result.append(temp.data)
                while len(stack) and temp == stack[-1].right: #if the last node popped was on the right then the top on stack must be it's root node
                    temp = stack.pop()                  # check if the temp (which was just popped on the right) is same as the stack top item right
                    result.append(temp.data)     #if true while condition then insert the parent node
            else:
                current = temp  #after inserting left if right is present then repeat the same process considering the right node as parent node
    return result


print(preOrderTraversal(root))
print(inOrderTraversal(root))
print(postOrderTraversal(root))