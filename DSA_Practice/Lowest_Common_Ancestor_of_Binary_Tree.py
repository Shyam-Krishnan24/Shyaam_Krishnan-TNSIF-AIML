
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    return right

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)

answer = lca(root, root.left, root.right)
print(answer.data)
