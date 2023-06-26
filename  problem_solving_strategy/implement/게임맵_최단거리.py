from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    answer = 0
    row, column = len(maps), len(maps[0])
    visited = [[False] * column for _ in range(row)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        x, y, count = queue.popleft()

        if x == row - 1 and y == column - 1:
            return count

        for i in range(4):
            next_x = dx[i] + x
            next_y = dy[i] + y

            if next_x >= 0 and next_y >= 0 and next_x < row and next_y < column:
                if not visited[next_x][next_y] and maps[next_x][next_y] == 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, count + 1))

    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))