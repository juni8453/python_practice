n, m = map(int, input().split())

answer = -1e9

for i in range(n):
  line = list(map(int, input().split()))
  line_min = min(line)
  answer = max(line_min, answer)

print(answer)