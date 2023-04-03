def solution(target, coins):
  count = 0

  def dfs(level, sum):
    nonlocal count
    if sum == target:
      count += 1
      return

    elif sum > target:
      return

    for coins_idx in range(len(coins)):
      dfs(level + 1, sum + coins[coins_idx])

  dfs(0, 0)

  return count
print(solution(target=4, coins=[1, 2, 3]))
print(solution(target=10, coins=[2, 5, 3, 6]))

