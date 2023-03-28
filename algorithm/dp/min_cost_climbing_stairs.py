def solution(cost):
  n = len(cost)
  memo = dict()

  def dp(n):
    if n == 0 or n == 1:
      return 0

    if n not in memo:
      memo[n] = min(cost[n - 1] + dp(n - 1) , cost[n - 2] + dp(n - 2))
    return memo[n]

  return dp(n)

print(solution(cost=[10,15,20,17,1]))