from node import Node
from bst import BST

def insert(T: BST, x: Node):
  parent = None
  curr = T.root
  while curr is not None:
    parent = curr
    if x.value <=curr.value:
      curr = curr.left
    else:
      curr = curr.right
  
  if parent is None:
    T.root = x
  elif parent.value >= x.value:
    parent.left = x
  else:
    parent.right = x
