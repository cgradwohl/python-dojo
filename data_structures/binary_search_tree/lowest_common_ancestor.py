class Node:
  def __init__(self, value):
    self.left = self.right = None
    self.value = value


def LCA(x: Node, u: Node, v: Node):
  current = x
  if u.value > v.value:
    temp = u
    u = v
    v = temp
  
  while current:
    if u.value <= current.value and current.value <= v.value:
      return current
    elif u.value > current.value:
      current = current.right
    elif v.value < current.value:
      current = current.left
  return None

def lca_binary_search_tree(root: Node, p: Node, q: Node) -> Node:
  while root:
      if p.value < root.value and q.value < root.value:
          root = root.left
      elif p.value > root.value and q.value > root.value:
          root = root.right
      else:
          return root
  return None

def lca_binary_tree(root: Node, p: Node, q: Node) -> Node:
  if root is None or root == p or root == q:
      return root

  left = lca_binary_tree(root.left, p, q)
  right = lca_binary_tree(root.right, p, q)

  if left and right:
      return root
  return left if left else right
