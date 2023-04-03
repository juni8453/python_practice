n, m, k = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
data.sort()
first = data[-1]
second = data[-2]

while 1:
  for _ in range(k):
    if m == 0: break
    m -= 1
    answer += first
  if m == 0: break
  m -= 1
  answer += second

print(answer)