import sys

n = int(sys.stdin.readline())
number = list(sys.stdin.readline().rstrip())
answer = 0

for num in number:
    answer += int(num)

print(answer)