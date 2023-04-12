from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
grid = []
move = 0

for i in range(n):
    grid.append(list(map(int, input().split())))

# 시작 좌표 동적으로 삽입
def search_city(x, y, visited):
    queue = deque()
    queue.append((x, y))
    union_list = [(x, y)]
    union_sum = grid[x][y]
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x = dx[i] + cur_x
            next_y = dy[i] + cur_y

            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y]:
                    if l <= abs(grid[cur_x][cur_y] - grid[next_x][next_y]) <= r:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
                        union_list.append((next_x, next_y))
                        union_sum += grid[next_x][next_y]

    if len(union_list) == 1:
        return False

    for i, j in union_list:
        grid[i][j] = int(union_sum / len(union_list))
    return True

# 인구이동이 없을 때 까지 반복
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if search_city(i, j, visited):
                    flag = True

    # 인구 이동이 없다면 while 탈출
    if not flag:
        break

    move += 1

print(move)
