from collections import deque

def number_of_islands(grid):
  count = 0
  m = len(grid)
  n = len(grid[0])
  visited = [[False] * n for _ in range(m)]

  def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
      cur_x, cur_y = queue.popleft()

      for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if 0 <= next_x < m and 0 <= next_y < n:
          if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            queue.append((next_x, next_y))

  for i in range(m):
    for j in range(n):
      # 1이면서 아직 방문하지 않았다면 bfs 실행
      if grid[i][j] == 1 and not visited[i][j]:
        bfs(i, j)
        count += 1

  return count

print(number_of_islands(grid=[
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]))

print(number_of_islands(grid=[
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]))