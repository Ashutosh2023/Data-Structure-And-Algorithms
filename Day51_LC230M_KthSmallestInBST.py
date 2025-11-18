class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create nodes
root = Node(8)

root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right = Node(14)
root.right.right.left = Node(13)

# BST:
#           (8)
#         /     \
#       (3)     (10)
#      /   \        \
#    (1)   (6)      (14)
#          / \      /
#        (4) (7)  (13)


# def kthSmallest(root: Node, K: int) -> int:
#     pass

# print(kthSmallest(root, 3))

# def kthSmallest(root: Node, k: int):
#     if not root:
#         return -1
#     result = []
#     current : Node = root
#     stack = []
#     while True:
#         if current:
#             stack.append(current)
#             current = current.left
#         else:
#             if len(stack) == 0:
#                 break
#             current = stack.pop()
#             if len(result) == k-1:
#                 return current.data
#             result.append(current.data)
#             current = current.right

#     return result[k-1]

# print(kthSmallest(root, 5))

def kthSmallestRecur(root: Node, cnt: int, k: int) -> int:
    if not root:
        return -1
    left = kthSmallestRecur(root.left, cnt, k)
    if left != -1:
        return left
    cnt[0] += 1

    if cnt[0] == k:
        return root.data
    
    right = kthSmallestRecur(root.right, cnt, k)
    return right

def kthSmallest(root: Node, k: int):
    cnt = [0]                  #use list to pass by reference instead of a int variable
    return kthSmallestRecur(root, cnt, k)

print(kthSmallest(root, 2))
print(kthSmallest(root, 3))
print(kthSmallest(root, 4))