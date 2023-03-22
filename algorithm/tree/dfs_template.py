# 전위 순회 (Preorder)
def preorder(cur_node):
  visited = []
  if cur_node is None:
    return

  visited.append(cur_node)
  preorder(cur_node.left)
  preorder(cur_node.right)

# 중위 순회 (Inorder)
def inorder(cur_node):
  visited = []
  if cur_node is None:
    return

  inorder(cur_node.left)
  visited.append(cur_node)
  inorder(cur_node.right)

# 후위 순회 (PostOrder)
def postorder(cur_node):
  visited = []
  if cur_node is None:
    return

  postorder(cur_node.left)
  postorder(cur_node.right)
  visited.append(cur_node)