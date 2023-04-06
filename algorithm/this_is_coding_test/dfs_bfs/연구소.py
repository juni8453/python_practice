import copy
from collections import deque

n, m = map(int, input().split())
data = []
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  data.append(list(map(int, input().split())))

# 벽을 세울 위치를 정하고 바이러스를 퍼트린 뒤 안전 구역을 카운트하는 완전 탐색 기법 필요

# 벽 3개를 세우고 BFS 실행
def make_wall(wall_count):
  if wall_count == 3:
    make_virus()
    return

  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        make_wall(wall_count + 1)
        # BFS 후 다른 곳에 벽을 세우기 위해 벽 허물기
        data[i][j] = 0

# 벽 3개를 세웠다면 바이러스를 퍼뜨린다.
def make_virus():
  queue = deque()
  # 바이러스의 좌표부터 퍼져나가야하기 때문에 바이러스 좌표 값을 큐에 삽입
  for i in range(n):
    for j in range(m):
      if data[i][j] == 2:
        queue.append((i, j))

  # 바이러스를 퍼뜨릴 test_data 값을 위해 data 깊은 복사
  test_data = copy.deepcopy(data)

  while queue:
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      next_x = dx[i] + cur_x
      next_y = dy[i] + cur_y

      if 0 <= next_x < n and 0 <= next_y < m:
        if test_data[next_x][next_y] == 0:
          test_data[next_x][next_y] = 2
          queue.append((next_x, next_y))

  count = 0
  for i in range(n):
    for j in range(m):
      if test_data[i][j] == 0:
        count += 1

  global result
  result = max(result, count)


make_wall(0)
print(result)

