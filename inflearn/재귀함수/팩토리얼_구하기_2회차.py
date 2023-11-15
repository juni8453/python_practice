answer = 0


def dfs(n, sumN):
    global answer
    if n == 1:
        answer = sumN
        return

    # 5 * 1, 4 * 5, 3 * 20 ...
    # n 이 1 씩 줄수록 sumN 을 초기화하고 n 이 1 이 되는 순간 재귀를 멈춘다.
    dfs(n - 1, n * sumN)


def solution(n):
    global answer

    dfs(n, 1)

    return answer


print(solution(5))
