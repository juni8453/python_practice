def solution(target, coins):
  count = 0

  def dfs(level, updated_sum, start_index):
    nonlocal count
    if updated_sum == target:
      count += 1
      return

    elif updated_sum > target:
      return

    # 최초 dfs() 진입 구간에 왔을 때 중복 탐색 방지를 위해 이미 탐색했던 가지 방향으로 진입하지 못하도록
    # for 범위 갱신
    for coins_idx in range(start_index, len(coins)):
      dfs(level + 1, updated_sum + coins[coins_idx], coins_idx)

  dfs(0, 0, 0)
  return count

print(solution(4, [1, 2, 3]))
print(solution(10, [2, 5, 3, 6]))