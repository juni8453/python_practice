n = input()
data = list(map(int, input().split()))
data.sort()

group = 0
people = 0

# 모인 사람 수가 현재 공포도보다 낮다면 사람이 더 필요하다.
# 모인 사람 수가 현재 공포도보다 크다면 그룹을 결성해준다.
for fear in data:
  people += 1
  if people >= fear:
    group += 1
    people = 0

print(group)