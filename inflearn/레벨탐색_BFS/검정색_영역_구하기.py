from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, board, visited, n):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def solution(board):
    n = len(board)
    answer = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 1:
                bfs(i, j, board, visited, n)
                answer += 1  # bfs() 종료 후 검은 영역 개수 증가

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

print(solution([
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0]
]))
