from node import Node

def pre_order_tree_walk_recursive(x: Node):
  if x is not None:
    print(x.value)
    pre_order_tree_walk_recursive(x.left)
    pre_order_tree_walk_recursive(x.right)
  
# def pre_order_tree_walk_iterative(x: Node):
#   stack = []
#   current = x

#   while stack or current is not None:
#     while current is not None:
#       if current.right is not None:
#         stack.append(current.right)
#       print(current.value)
#       current = current.left

#     current = stack.pop() if stack else None

def pre_order_tree_walk_iterative(x: Node):
  stack = [x]
  while stack:
    node = stack.pop()
    print(node.value)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)



root = Node(8)
n_6 = Node(6)
n_4 = Node(4)
n_10 = Node(10)
n_5 = Node(5)

root.left = n_6
root.left.left = n_4
root.right = n_10
root.left.left.right = n_5

# pre_order_tree_walk_recursive(root)
pre_order_tree_walk_iterative(root)
