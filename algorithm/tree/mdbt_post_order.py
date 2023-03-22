def maxDepth(cur_node):
  # Base Case
  if cur_node is None:
    return 0

  # 재귀 호출 후 Depth 값 반환
  left_depth = maxDepth(cur_node.left)
  right_depth = maxDepth(cur_node.rigth)

  # 반환받은 Depth 값 비교 후 더 큰 값에 + 1
  return max(left_depth, right_depth) + 1