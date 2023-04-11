# Tip) 한 칸 이상의 최단 거리 BFS 문제일 경우 집합 자료형과 튜플을 섞어서 처리
# Tip) 회전을 할 수 있는 경우 맵 외곽을 벽으로 둘러 쌓는 것이 범위 판정 코드 작성에서 유리
#   왜냐면 외부 벽이 없다면 index 가 넘어가는지 체크해줘야 하는데, 벽이 있다면 통로인 경우 (이 문제에서는 0) 만 처리해주면 되기 떄문

from collections import deque

def get_next_pos(pos, board):
  # 다음 로봇의 위치를 반환할 배열 선언
  next_pos = []
  (x1, y1), (x2, y2) = pos

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # 상, 하, 좌, 우 이동 처리
  for i in range(4):
    if board[x1 + dx[i]][y1 + dy[i]] == 0 and board[x2 + dx[i]][y2 + dy[i]] == 0:
      next_pos.append({(x1 + dx[i], y1 + dy[i]), (x2 + dx[i], y2 + dy[i])})

  # 회전 처리
  # 1. 가로 -> 세로로 회전하는 경우
  if x1 == x2:
    for i in [-1, 1]:
      if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
        # ({(기준 축), (기준 축에서 회전할 수 있는 좌표)})
        next_pos.append({(x1, y1), (x1 + i, y1)})
        next_pos.append({(x2, y2), (x2 + i, y2)})

  # 2. 세로 -> 가로로 회전하는 경우
  if y1 == y2:
    for i in [-1, 1]:
      if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
        next_pos.append({(x1, y1), (x1, y1 + i)})
        next_pos.append({(x2, y2), (x2, y2 + i)})

  return next_pos

def solution(board):
  # 회전이 있는 문제이기 때문에 외벽을 설치해서 분기문을 간단하게 한다.
  n = len(board)
  new_board = [[1] * (n + 2) for _ in range(n + 2)]

  for r in range(n):
    for c in range(n):
      new_board[r + 1][c + 1] = board[r][c]

  board = new_board

  # 로봇이 좌표 하나 이상으로 표현되니까 집합 자료형, 튜플 사용
  queue = deque()
  pos = {(1, 1), (1, 2)}
  vistied = []
  queue.append((pos, 0))
  vistied.append(pos)

  while queue:
    pos, time = queue.popleft()

    # 도착 지점에 도달했다면 return
    if (n, n) in pos:
      return time

    # get_next_pos 함수를 활용해 BFS 수행
    for next_pos in get_next_pos(pos, board):
      if next_pos not in vistied:
        vistied.append(next_pos)
        queue.append((next_pos, time + 1))

print(solution(
  [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1],
   [0, 0, 0, 0, 0]]))