from collections import deque

def solution(grid):
  shortest_path_len = -1
  n = len(grid)
  visited = [[False] * n for _ in range(n)]

  # 시작점과 출발점이 벽이라면 길이 없는 것이므로 BFS 이전에 -1 이 반환되도록 한다.
  if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
    return shortest_path_len

  # x, y 위치 정보와 추적을 위해 길이 정보 1을 함께 넣어준다.
  queue = deque()
  queue.append((0, 0, 1))
  visited[0][0] = True
  delta = [
    (1,0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
  ]

  while queue:
    cur_x, cur_y, cur_len = queue.popleft()

    # 목적지에 도착했을 때 cur_len 를 sortest_path_len 에 저장하면 된다.
    # BFS 특성 상 가장 빨리 도달했을 때 최소 길이가 구해지므로 더이상 while 문을 반복하지 않아도 무방
    if cur_x == n - 1 and cur_y == n - 1:
      shortest_path_len = cur_len
      break

    for dx, dy in delta:
      next_x = cur_x + dx
      next_y = cur_y + dy

      if 0 <= next_x < n and 0 <= next_y < n:
        if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
          visited[next_x][next_y] = True
          queue.append((next_x, next_y, cur_len + 1))

  return shortest_path_len

print(solution(grid=[
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]))

print(solution(grid=[
  [0, 1],
  [1, 0]
]))

print(solution(grid=[
  [0, 1, 0],
  [1, 1, 0],
  [1, 1, 0]
]))

print(solution(grid=[
  [1, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]))

print(solution(grid=[
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 1]
]))