from node import Node


def dfs(u: Node, target: Node):
  if u is None or u.value == target.value:
    return u
  
  left = dfs(u.left)
  right = dfs(u.right)

  if left is not None:
    return left
  else:
    return right



# NOTE: a better approach to only go right if left returned none.
# in other words, if left found a value(its not None), then return it!
# def dfs(root: Node, target: int) -> Node:
#     """
#     Find the first node with the given target value in a binary tree.

#     :param root: The root node of the binary tree.
#     :param target: The target value to search for.
#     :return: The first node with the target value or None if the target value is not found.
#     """
#     if root is None or root.value == target:
#         return root

#     left = dfs(root.left, target)
#     if left is not None:
#         return left

#     return dfs(root.right, target)
