from node import Node
from bst import BST
from insert import insert

def search_iterative(r: Node, x: int):
  while r is not None and r.value != x:
    if x < r.value:
      r = r.left
    else:
      r = r.right
  return r


def search_recursive(r: Node, x: int):
  if r == None or r.value == x:
    return r
  if x < r.value:
    return search_recursive(r.left, x)
  else:
    return search_recursive(r.right, x)

tree = BST()
insert(tree, Node(8))
insert(tree, Node(6))
insert(tree, Node(2))
insert(tree, Node(7))
insert(tree, Node(17))
insert(tree, Node(11))
insert(tree, Node(21))
insert(tree, Node(19))
insert(tree, Node(20))

# result = search_iterative(tree.root, 17)
result = search_recursive(tree.root, 20)
print(result.value)
