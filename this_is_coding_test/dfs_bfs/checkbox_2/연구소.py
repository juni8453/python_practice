import copy
from collections import deque

n, m = list(map(int, input().split()))
grid = []
answer = -1e9
# queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  grid.append(list(map(int, input().split())))

# 벽이 3개 세워졌으면 virus 를 퍼뜨린다.
def spread_virus():
  queue = deque()
  for r in range(n):
    for c in range(m):
      if grid[r][c] == 2:
        queue.append((r, c))

  # 바이러스를 퍼뜨려볼 테스트용 grid 생성
  test_grid = copy.deepcopy(grid)

  while queue:
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      next_x = cur_x + dx[i]
      next_y = cur_y + dy[i]

      if 0 <= next_x < n and 0 <= next_y < m:
        if test_grid[next_x][next_y] == 0:
          test_grid[next_x][next_y] = 2
          queue.append((next_x, next_y))

  cur_safe_zone = 0
  for r in range(n):
    for c in range(m):
      if test_grid[r][c] == 0:
        cur_safe_zone += 1

  global answer
  answer = max(answer, cur_safe_zone)

# 벽을 3개 세운다
def make_wall(wall_count):
  if wall_count == 3:
    spread_virus()
    return # Base Case 이기 때문에 BFS 로 작업을 넘기고 return

  else:
    for r in range(n):
      for c in range(m):
        if grid[r][c] == 0:
          grid[r][c] = 1
          make_wall(wall_count + 1)
          grid[r][c] = 0

make_wall(0)
print(answer)
