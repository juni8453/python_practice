import sys

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nums.append([x, y])

nums.sort(key=lambda num: (num[0], num[1]))

for num in nums:
    print(f'{num[0]} {num[1]}')
