from collections import deque

# n : 도시의 개수
# m : 도로의 개수
# k : 거리 정보
# x : 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] * m for _ in range(n + 1)]
visited = [False] * (n + 1)
dis = [0] * (n + 1)

# 도로 개수 만큼 각 도시 연결
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b) # 양방향 리스트가 아니기 때문에 단방향으로 연결

# graph = [
#     [],
#     [2, 3], 1번 도시는 2, 3번 도시와 연결 되어있음.
#     [3, 4], 2번 도시는 3, 4번 도시와 연결 되어있음.
#     [],
#     []
# ]

# 출발 도시 방문 표시
visited[x] = True
queue = deque()
queue.append(x)

while queue:
  cur_city = queue.popleft()

  for next_city in graph[cur_city]:
    if not visited[next_city]:
      visited[next_city] = True
      dis[next_city] = dis[cur_city] + 1
      queue.append(next_city)

check = False
for i in range(1, len(dis)):
  if dis[i] == k:
    print(i)
    check = True

if not check:
  print(-1)