class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def lca(self, root, p, q):
    if root is None:
      return None

    left = self.lca(root.left, p, q)
    right = self.lca(root.right, p, q)

    if root == p or root == q:
      return root
    elif left and right:
      return root

    # left 값이 있다면 left, right 값이 있다면 right 값 반환
    return left or right

print(Solution().lca(root=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p=6, q=4))
