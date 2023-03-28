def solution(n):
  memo = dict()
  memo[0] = 0
  memo[1] = 1
  memo[2] = 2

  for i in range(3, n + 1):
    if i not in memo:
      memo[i] = memo[i - 1] + memo[i - 2]

  return memo[n]

print(solution(n=3))
print(solution(n=4))
