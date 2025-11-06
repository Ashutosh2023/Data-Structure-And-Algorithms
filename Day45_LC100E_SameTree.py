class Node:
    def __init__(self, data):
        self.val = data
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
def isSameTree(p: Node, q: Node) -> bool:
    if p is None or q is None:
        return p==q
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(root, root))


#approach 2 works only in python because a array won't hold a character "a"
class Solution:
    def preOrderTraversal(self, root: Node):
        if not root:
            return ["a"]
        left_values = self.preOrderTraversal(root.left)
        right_values = self.preOrderTraversal(root.right)

        return [root.val] + left_values + right_values

    def isSameTree(self, p: Node, q: Node) -> bool:
        pTree = self.preOrderTraversal(p)
        qTree = self.preOrderTraversal(q)
        print(pTree, qTree)
        if pTree == qTree:
            return True
        else:
            return False