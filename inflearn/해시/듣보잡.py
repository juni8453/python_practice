import sys
from collections import defaultdict

names_dict = defaultdict(int)
n, m = map(int, sys.stdin.readline().split())
count = 0
answer = []

for _ in range(n + m):
    name = sys.stdin.readline().strip()
    names_dict[name] += 1

for key, value in names_dict.items():
    if value > 1:
        count += 1
        answer.append(key)

print(count)
for a in sorted(answer):
    print(a)

