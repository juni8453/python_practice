def solution(rooms):
  # visited2 = [[False] * len(rooms)] 2차원으로 생성할 때 주로 사용
  # visited3 = [False] * len(rooms) 1차원으로 생성할 때 주로 사용
  visited = [False] * len(rooms)

  def dfs(cur_v):
    visited[cur_v] = True
    for next_v in rooms[cur_v]:
      if not visited[next_v]:
        dfs(next_v)

  dfs(0)

  return all(visited)

print(solution(rooms=[
  [1, 3],
  [3, 0, 1],
  [2],
  [0]
]))
