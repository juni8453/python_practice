def recursion(n, level):
    if n == 1:
        return level

    if level > 500:
        return -1

    if n % 2 == 0:
        n = n // 2
        return recursion(n, level + 1)

    elif n % 2 != 0:
        n = n * 3 + 1
        return recursion(n, level + 1)

def solution(n):
    answer = recursion(n, 0)

    return answer

print(solution(6))
print(solution(626331))