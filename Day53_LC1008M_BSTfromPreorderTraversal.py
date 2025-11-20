class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bstFromPreorder(preorder: list[int], idx: list[int], upperbound) -> Node:
    if idx[0] >= len(preorder) or preorder[idx[0]] > upperbound:
        return None
    root = Node(preorder[idx[0]])
    idx[0] += 1
    root.left = bstFromPreorder(preorder, idx, root.data)
    root.right = bstFromPreorder(preorder, idx, upperbound)

    return root

preorder = [8,5,1,7,10,12]
idx = [0]
roott = bstFromPreorder(preorder, idx, float('inf'))

def preOrderTraversal(root: Node):
    if not root:
        return []
    left_values = preOrderTraversal(root.left)
    right_values = preOrderTraversal(root.right)

    return [root.data] + left_values + right_values

print(preOrderTraversal(roott))