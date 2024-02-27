from node import Node

def post_order_tree_walk_recursive(x: Node):
  if x is not None:
    post_order_tree_walk_recursive(x.left)
    post_order_tree_walk_recursive(x.right)
    print(x.value)

def post_order_tree_walk_iterative(x: Node):
  stack = [x]
  results = []
  while stack:
    node = stack.pop()
    results.append(node.value)
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)

  for i in range(len(results) - 1, -1, -1):
    print(results[i])


root = Node(8)
n_6 = Node(6)
n_4 = Node(4)
n_10 = Node(10)
n_5 = Node(5)

root.left = n_6
root.left.left = n_4
root.right = n_10
root.left.left.right = n_5


# post_order_tree_walk_recursive(root)
post_order_tree_walk_iterative(root)
