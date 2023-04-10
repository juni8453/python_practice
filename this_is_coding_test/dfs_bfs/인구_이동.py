from collections import deque

n, l, r = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  graph.append(list(map(int, input().split()))) # 숫자를 입력받아야하기 때문에 int 사용

def bfs(x, y, visited):
  visited[x][y] = True
  queue = deque()
  queue.append((x, y))
  union_list = [(x, y)]
  union_sum = graph[x][y]

  while queue:
    cur_x, cur_y = queue.popleft()

    for i in range(4):
      next_x = cur_x + dx[i]
      next_y = cur_y + dy[i]

      if 0 <= next_x < n and 0 <= next_y < n:
        if not visited[next_x][next_y]:
          if l <= abs(graph[cur_x][cur_y] - graph[next_x][next_y]) <= r:
            visited[next_x][next_y] = True
            queue.append((next_x, next_y))
            union_sum += graph[next_x][next_y]
            union_list.append((next_x, next_y))

  # 더 이상의 연합 결성이 없다면 인구 이동 중지
  if len(union_list) == 1:
    return False

  # 연합 결성이 완료되었다면 분배 시작
  for i, j in union_list:
    graph[i][j] = union_sum // len(union_list)
  return True

moved_count = 0

while True:
  visited = [[False] * n for _ in range(n)]
  flag = False

  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        if bfs(i, j, visited):
          flag = True

  # 인구 이동이 더 이상 필요없다.
  if not flag:
    break

  moved_count += 1

print(moved_count)