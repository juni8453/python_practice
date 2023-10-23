import sys
from collections import defaultdict

candidate_names = defaultdict(int)
possible_names = defaultdict(int)
n = int(sys.stdin.readline())
answer = ''

for _ in range(n):
    name = sys.stdin.readline().strip()
    candidate_names[name] += 1

for _ in range(n - 1):
    name = sys.stdin.readline().strip()
    possible_names[name] += 1

for p_key, p_value in possible_names.items():
    if p_key in candidate_names.keys():
        candidate_names[p_key] -= p_value

for c_key, c_value in candidate_names.items():
    if c_value >= 1:
        answer = c_key

print(answer)