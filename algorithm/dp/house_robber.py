# Bottom Up 방식 풀이
def solution(nums):
  n = len(nums)
  memo = [-1] * n
  memo[0] = nums[0]
  memo[1] = max(nums[0], nums[1])

  for i in range(2, n):
    memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])
  return memo[n - 1]

print(solution(nums=[1, 2, 3, 1]))

# Top Down 방식 풀이
def solution2(nums):
  n = len(nums)
  memo = [-1] * n

  def dfs(n):
    # base case
    if n == 0:
      return nums[0]
    if n == 1:
      return max(nums[n], nums[n - 1])

    # 한 번은 꼭 계산을 해줘야한다.
    if memo[n] == -1:
      memo[n] = max(dfs(n - 1), dfs(n - 2) + nums[n])
      return memo[n]

    return memo[n]

  return dfs(n - 1)

print(solution2(nums=[1, 2, 3, 1]))
print(solution2(nums=[2,7,9,3,1]))