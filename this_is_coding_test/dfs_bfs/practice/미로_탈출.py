from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽 = 0, 길 = 1
# 탈출을 위해 움직여야 하는 최소 칸의 개수는 ?
# 칸은 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
def solution(n, m, map):
  answer = 0
  visited = [[False] * m for _ in range(n)]
  dis = [[0] * m for _ in range(n)]

  # 출발 시점은 1로 초기화 (시작 칸을 세야하므로)
  dis[0][0] = 1
  visited[0][0] = True

  def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
      # 최단 거리가 구해졌을 경우 바로 return 할 수 있도록
      if dis[n - 1][m - 1] != 0:
        break

      cur_shell_x, cur_shell_y = queue.popleft()

      for i in range(4):
        next_x = cur_shell_x + dx[i]
        next_y = cur_shell_y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < m:
          if map[next_x][next_y] == 1:
            if not visited[next_x][next_y]:
              visited[next_x][next_y] = True
              queue.append((next_x, next_y))
              dis[next_x][next_y] = dis[cur_shell_x][cur_shell_y] + 1

  bfs()

  return dis[n - 1][m - 1]



print(solution(5, 6, [
  [1,0,1,0,1,0],
  [1,1,1,1,1,1],
  [0,0,0,0,0,1],
  [1,1,1,1,1,1],
  [1,1,1,1,1,1]
]))