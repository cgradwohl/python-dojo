class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Tree
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.left = node2
node1.right = node6

node2.left = node3
node2.right = node4

node3.right = node5


def dfs(root, target):
    if root is None or root.value == target:
        return root

    left = dfs(root.left, target)
    if left is not None:
        return left

    right = dfs(root.right, target)
    return right


result = dfs(node1, 4)
print("%s was found." % (result.value if result is not None else "No target"))
