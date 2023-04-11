n = int(input())
nums = (list(map(int, input().split())))
operator = (list(map(int, input().split())))

# DFS 완전탐색
def dfs(depth, sum):
  global max_result
  global min_result

  # Base case 설정
  if depth == (n - 1):
    max_result = max(max_result, sum)
    min_result = min(min_result, sum)
    return

  else:
    for i in range(4):
      if operator[i] > 0: # 현재 연산자가 있다면

        operator[i] -= 1

        if i == 0: # 더하기
          dfs(depth + 1, sum + nums[depth + 1])

        elif i == 1: # 빼기
          dfs(depth + 1, sum - nums[depth + 1])

        elif i == 2: # 곱하기
          dfs(depth + 1, sum * nums[depth + 1])

        elif i == 3: # 나누기
          dfs(depth + 1, int(sum / nums[depth + 1]))

        operator[i] += 1 # 모든 경우의 수를 구해야하기 때문에 연산자 복구

max_result = -1e9
min_result = 1e9

dfs(0, nums[0])

print(max_result)
print(min_result)
