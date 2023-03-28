def solution(m, n):
  memo = [[-1] * n for _ in range(m)]

  def dp(r, c):
    for i in range(r):
      memo[i][0] = 1
    for i in range(c):
      memo[0][i] = 1

    for i in range(1, r):
      for j in range(1, c):
        memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

    return memo[r - 1][c - 1]
  return dp(m, n)

print(solution(3, 7))
print(solution(3, 3))

