n = input()
data = list(map(int, input().split()))
answer = 0

# [1, 1, 2, 3, 9]
data.sort()

# 만들어야 하는 돈 1부터 확인
target = 1

for i in data:
  if target < i:
    break
  target += i

print(target)