import sys

n = int(sys.stdin.readline())

sp = 1
ep = 1
sum_num = 1
answer = 1

while ep != n:
    if sum_num == n:
        answer += 1
        ep += 1
        sum_num += ep

    elif sum_num > n:
        sum_num -= sp
        sp += 1

    else:
        ep += 1
        sum_num += ep

print(answer)
