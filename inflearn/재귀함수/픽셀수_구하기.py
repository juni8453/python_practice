dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0


def dfs(x, y, n, visited, board):
    global count
    visited[x][y] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == 1:
                dfs(nx, ny, n, visited, board)


def solution(board):
    global count
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = []

    for i in range(len(board)):
        for j in range(len(board)):
            if not visited[i][j] and board[i][j] == 1:
                count = 0 # 다음 영역 픽셀 수를 구하기 전 초기화 필요
                dfs(i, j, n, visited, board)
                answer.append(count)

    return answer


print(solution([
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0]
]))

print(solution([
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0]
]))

print(solution([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0]
]))
