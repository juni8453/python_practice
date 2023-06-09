from collections import deque

def bfs(root):
  visited = []
  if root is None:
    return []

  q = deque()
  q.append(root)

  while q:
    cur_node = q.popleft()
    visited.append(cur_node) # 필수는 아님(문제마다 다름)

    if cur_node.left:
      q.append(cur_node.left)
    if cur_node.right:
      q.append(cur_node.right)

    return visited

print(bfs())
