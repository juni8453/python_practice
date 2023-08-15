import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# 문제에서 인덱스 범위가 아닌 통상적인 범위를 질의 했으므로 범위를 맞추기 위해 0 삽입
prefix_sum = [0]
temp = 0

for num in numbers:
    temp = temp + num
    prefix_sum.append(temp)

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(prefix_sum[y] - prefix_sum[x - 1])

