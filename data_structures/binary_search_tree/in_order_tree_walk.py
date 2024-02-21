class Node:
  def __init__(self, value):
    self.left = self.right = None
    self.value = value

def in_order_tree_walk_recursive(x: Node):
  if x is not None:
    in_order_tree_walk_recursive(x.left)
    print(x.value)
    in_order_tree_walk_recursive(x.right)

def in_order_tree_walk_iterative(x: Node):
  stack = []
  current = x

  while stack or current is not None:
    while current is not None:
      stack.append(current)
      current = current.left
    
    node = stack.pop()
    print(node.value)
    current = node.right


root = Node(8)
n_6 = Node(6)
n_4 = Node(4)
n_10 = Node(10)
n_5 = Node(5)

root.left = n_6
root.left.left = n_4
root.right = n_10
root.left.left.right = n_5

# in_order_tree_walk_recursive(root)
in_order_tree_walk_iterative(root)
