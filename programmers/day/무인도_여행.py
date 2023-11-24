from collections import deque

# 북, 동, 남, 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def search(queue, visited, board, n, m):
    sum_meet = 0

    while queue:
        cur_x, cur_y, cur_meet = queue.popleft()
        sum_meet += int(cur_meet)

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, board[nx][ny]))

    return sum_meet


def solution(maps):
    answer = []
    n = len(maps) # 행
    m = len(maps[0]) # 열
    board = [['' for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()

    # 자연수도 문자로 저장된 상태
    for i in range(n):
        for j in range(m):
            board[i][j] = maps[i][j]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] != 'X':
                queue.append((i, j, board[i][j]))
                visited[i][j] = True
                sum_meet = search(queue, visited, board, n, m)
                answer.append(sum_meet)

    if len(answer) == 0:
        return [-1]

    answer.sort()

    return answer