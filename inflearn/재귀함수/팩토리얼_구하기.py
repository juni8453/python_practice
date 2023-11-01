global answer

def DFS(n, sumN):
    global answer

    # 종료 조건에 도달해서 지금까지 계산했던 매개변수 값을 전역변수에 담고 return (종료)
    if n == 1:
        answer = sumN
        return

    sumN *= n
    DFS(n - 1, sumN)

def solution(n):
    global answer

    sumN = 1
    DFS(n, sumN)

    return answer

print(solution(5))