from collections import deque

def path(grid):
  n = len(grid)
  visited = [[False] * n for _ in range(n)]
  dis = [[0] * n for _ in range(n)]

  def bfs(x, y):
    visited[x][y] = True

    # 대각
    dx = [-1, 0, 1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]

    queue = deque()
    queue.append((x, y))

    while queue:
      cur_x, cur_y = queue.popleft()

      for i in range(8):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < n:
          if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
            dis[next_x][next_y] = dis[cur_x][cur_y] + 1
            visited[next_x][next_y] = True
            queue.append((next_x, next_y))

  for i in range(n):
    for j in range(n):

      # BFS 를 한 번만 실행해야만 경로가 끊기고 나서 끊긴 뒤 '0' 을 찾아 헤메지 않는다.
      if grid[i][j] == 0 and not visited[i][j] and i == 0 and j == 0:
        bfs(i, j)

  # 만약 크기가 1*1 이면서 (출발지 == 도착지) '0' 인 경우
  if n == 1 and grid[n - 1][n - 1] == 0:
    return 1

  # 경로가 아예 존재하지 않는 경우
  if dis[n - 1][n - 1] == 0:
    return -1

  # 경로가 존재하는 경우 도착지에는 최단 거리가 표기되어있다.
  return dis[n - 1][n - 1] + 1

print(path(grid=[[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))

print(path(grid=[
  [1]
]))

print(path(grid=[
  [0]
]))

print(path(grid=[
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]))

print(path(grid=[
  [0, 1],
  [1, 0]
]))

print(path(grid=[
  [0, 1, 0],
  [1, 1, 0],
  [1, 1, 0]
]))

print(path(grid=[
  [1, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]))

print(path(grid=[
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 1]
]))