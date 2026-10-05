
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

queue = [root]
result = []

while queue:
    level = []
    for i in range(len(queue)):
        node = queue.pop(0)
        level.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(level)
print(result)
