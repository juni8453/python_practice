dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

def solution(n, m, map):
  # 구멍은 0, 칸막이는 1
  # 완전 탐색 풀이 (DFS)
  count = 0
  visited = [[False] * m for _ in range(n)]

  def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
      next_x = x + dx[i]
      next_y = y + dy[i]

      if 0 <= next_x < n and 0 <= next_y < m:
        if map[next_x][next_y] == 0:
          if not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            dfs(next_x, next_y)


  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] != 1 and not visited[i][j]:
        dfs(i, j)
        count += 1

  return count

print(solution(15, 14, [
  [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
  [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
  [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
  [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
  [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
  [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
  [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
  [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
  [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
  [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
  [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
  [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
]))

print(solution(4, 5, [
  [0, 0, 1, 1, 0],
  [0, 0, 0, 1, 1],
  [1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0]
]))
