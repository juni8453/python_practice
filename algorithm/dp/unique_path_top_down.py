def solution(m, n):
  memo = [[-1] * n for _ in range(m)]

  # Top Down 방식 (재귀)
  def dfs(r, c):
    path = 0

    if r == 0 and c == 0:
      memo[r][c] = 1
      return memo[r][c]

    if memo[r][c] == -1:
      if r - 1 >= 0:
        path += dfs(r - 1, c)
      if c - 1 >= 0:
        path += dfs(r, c - 1)
    return path

  return dfs(m - 1, n - 1)

print(solution(2, 2))
print(solution(3, 7))
