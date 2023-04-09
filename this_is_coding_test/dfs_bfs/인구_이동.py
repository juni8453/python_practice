from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
graph = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
  graph.append(list(map(int, input().split()))) # 숫자가 사용되니 map() 사용

def bfs(x, y, visited):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  sum_list = [graph[x][y]]
  union_count = 1

  while queue:
    cur_x, cur_y = queue.popleft()

    for i in range(4):
      next_x = cur_x + dx[i]
      next_y = cur_y + dy[i]

      if 0 <= next_x < n and 0 <= next_y < n: # 그래프 범위를 넘지 않고,
        if not visited[next_x][next_y]: # 방문하지 않았고,
          if l <= abs(graph[cur_x][cur_y] - graph[next_x][next_y]) <= r: # 국가 수의 차이가 l <= x <= r 이라면,
            sum_list.append(graph[next_x][next_y])
            visited[next_x][next_y] = True
            queue.append((next_x, next_y))
            union_count += 1

  if union_count == 1: # 이번 라운드에서 인구 이동이 일어나지 않았을 경우
    return False

  divided_people = sum(sum_list) // len(sum_list)

  for i in range(n):
    for j in range(n):
      if visited[i][j]:
        graph[i][j] = divided_people

  return True

count = 0

while True:
  visited = [[False] * n for _ in range(n)]
  moved = False

  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        if bfs(i, j, visited):
          moved = True

  if not moved: # 인구 이동이 일어나지 않은 경우
    break

  count += 1

print(count)
