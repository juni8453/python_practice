from collections import deque

n, k = map(int, input().split())
graph = []
virus_data = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 큐에 virus 좌표를 삽입할 때 미리 낮은 순서로 삽입해야한다.
# 그래야 알아서 작은 순서대로 큐가 돌기 때문
for i in range(n):
  graph.append(list(map(int, input().split())))

  for j in range(n):
    if graph[i][j] != 0:
      virus_data.append((graph[i][j], 0, i, j))

# 작은 virus 부터 오름차순으로 정렬한 뒤 queue 로 옮긴다.
virus_data.sort()
queue = deque(virus_data)

s, x, y = map(int, input().split())

while queue:
  cur_virus_type, cur_time, cur_x, cur_y = queue.popleft()

  if cur_time == s:
    break

  for i in range(4):
    next_x = cur_x + dx[i]
    next_y = cur_y + dy[i]

    if 0 <= next_x < n and 0 <= next_y < n:
      if graph[next_x][next_y] == 0:
        graph[next_x][next_y] = cur_virus_type
        queue.append((cur_virus_type, cur_time + 1, next_x, next_y))

print(graph[x - 1][y - 1])