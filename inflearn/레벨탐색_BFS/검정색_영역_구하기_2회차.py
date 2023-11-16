from collections import deque

# 북, 동, 남, 서 방향 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(n, x, y, board, visited, queue):
    queue.append((x, y))
    visited[x][y] = True

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
    answer = 0
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 1:
                bfs(n, i, j, board, visited, queue)
                answer += 1

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
