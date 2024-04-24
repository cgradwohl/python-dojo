class Node:
    def __init__(self, value, children=[]):
        self.children = children
        self.value = value


def allPaths(root):
    def dfs_with_states(root, path, result):
        if all(child is None for child in root.children):
            path.append(root.value)
            result.append(path)
            return
        for child in root.children:
            if child is not None:
                new_path = path + [str(root.value)]
                dfs_with_states(child, new_path, result)

    r = []
    dfs_with_states(root, [], r)
    return r


# tree
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node6 = Node(6)

node1.children = [node2, node4, node6]
node2.children = [node3]

print(allPaths(node1))
