from collections import deque

def solution(n, edge):
  visited = [False] * (n + 1)
  dis = [0] * (n + 1)
  graph = [[] for _ in range(n + 1)]

  for a, b in edge:
    graph[a].append(b)
    graph[b].append(a)

  # 기본 셋팅
  queue = deque()
  queue.append(1)
  visited[1] = True
  dis[1] = 1

  while queue:
    cur_node = queue.popleft()

    for next_node in graph[cur_node]:
      if not visited[next_node]:
        dis[next_node] += dis[cur_node] + 1
        visited[next_node] = True
        queue.append(next_node)

  return dis.count(max(dis))

print(solution(n = 6, edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(n = 2, edge=[[1, 2], [2, 1]]))