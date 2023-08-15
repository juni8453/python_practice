import sys

# 1. 최대값을 고른다 = M
# 2. 모든 점수를 (점수/M*100) 으로 수정

n = int(sys.stdin.readline())
ranks = list(map(int, sys.stdin.readline().split()))
new_ranks = []

M = max(ranks)

for cur_rank in ranks:
    new_rank = cur_rank / M * 100
    new_ranks.append(new_rank)

sum = 0
for new_rank in new_ranks:
    sum += new_rank

answer = sum / n
print(answer)