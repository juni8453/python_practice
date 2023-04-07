n = input()
numbers = list(map(int, input().split())) # 사칙연산 할 숫자들
operators = list(map(int, input().split())) # 연산자 목록

# operators = [0, 0, 1, 0]
# '+' : 0 개
# '-' : 0 개
# '*' : 1 개
# '/' : 0 개

max_answer = -1e9
min_answer = 1e9

def dfs(depth, result):
  global n
  global max_answer
  global min_answer

  # base case
  if depth == int(n):
    max_answer = max(max_answer, result)
    min_answer = min(min_answer, result)
    return

  for i in range(4):
    if operators[i] != 0:

      operators[i] -= 1

      if i == 0:
        dfs(depth + 1, result + numbers[depth])

      elif i == 1:
        dfs(depth + 1, result - numbers[depth])

      elif i == 2:
        dfs(depth + 1, result * numbers[depth])

      elif i == 3:
        dfs(depth + 1, int(result / numbers[depth]))

      operators[i] += 1

dfs(1, numbers[0])

print(max_answer)
print(min_answer)
