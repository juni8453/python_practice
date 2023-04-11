from collections import deque

answer = 0
n, m, k, x = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

dis = [0] * (n + 1)

visited = [False] * (n + 1)
visited[x] = True

queue = deque()
queue.append(x)


while queue:
  cur_city = queue.popleft()

  for next_city in graph[cur_city]:
    if not visited[next_city]:
      visited[next_city] = True
      queue.append(next_city)
      dis[next_city] = dis[cur_city] + 1

flag = False

for i in range(1, len(dis)):
  if dis[i] == k:
    print(i)
    flag = True

if not flag:
  print(-1)
