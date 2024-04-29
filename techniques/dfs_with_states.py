class Node:
    def __init__(self, value, children=[]):
        self.children = children
        self.value = value


def allPaths(node, path=[], result=[]):
    if all(c is None for c in node.children):
        result.append("->".join(path) + "->" + str(node.value))
        return

    for child in node.children:
        if child is not None:
            new_path = [*path, str(node.value)]
            allPaths(child, new_path, result)

    return result

    # tree
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node6 = Node(6)

node1.children = [node2, node4, node6]
node2.children = [node3]

print(allPaths(node1))
