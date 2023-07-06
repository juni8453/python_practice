import sys


def dfs(n):
    # 값 갱신을 위해 global 예약어 사용
    global answer

    # Queen 을 놓을 수 있는 경로로 끝까지 탐색된 경우
    if n == N:
        answer += 1
        return

    # 하나의 행 를 기준으로 해당 행의 열을 하나씩 확인
    for j in range(N):
        # 위, 왼쪽 대각, 오른쪽 대각에 Queen 이 없는 경우
        if v1[j] == v2[n + j] == v3[n - j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j] = 0


answer = 0
N = int(sys.stdin.readline())

v1 = [0] * N
v2 = [0] * (2 * N - 1)
v3 = [0] * (2 * N - 1)

# dfs(헹 탐색)
dfs(0)
print(answer)