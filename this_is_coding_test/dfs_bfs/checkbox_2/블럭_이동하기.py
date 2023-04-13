# BFS 꿀팁 중요!
# 무조건 visited 이후에 queue 에 좌표를 넣는 건 아니다.
# 움직일 수 있는 좌표를 찾고, 더 이상 고려할 경우가 없을 때 그때 방문 처리를 하는 것 !!
# 이 문제처럼 상하좌우 이동 뿐 아니라, 회전까지 고려해야하는 상황일 때 좌표를 찾는 즉시 방문 처리를 하게된다면 상하좌우 및 회전 시에
# 이미 방문 체크가 되있어서, 해당 좌표로 이동할 수 있는 상황에도 불구하고 Queue 에 좌표를 삽입할 수 없는 경우가 발생한다.

# 또한, 좌표 값이 이 문제처럼 2개 이상이라면, 집합 자료형을 사용하자.
# 마지막으로, queue 와 visited 변수는 항상 비슷하게 하자. queue 가 리스트라면, visited 도 리스트 이런 식으로 !

from collections import deque

def get_next_position(position, board):
    next_position_list = []
    (x1, y1), (x2, y2) = position

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상, 하, 좌, 우 좌표 확인 후 다음에 갈 수 있는 좌표 리스트에 등록
    # 실제로 해당 위치로 가는게 아니라 visited 처리는 나중에.
    for i in range(4):
        if board[x1 + dx[i]][y1 + dy[i]] == 0 and board[x2 + dx[i]][y2 + dy[i]] == 0:
            next_position = {(x1 + dx[i], y1 + dy[i]), (x2 + dx[i], y2 + dy[i])}
            next_position_list.append(next_position)

    # 회전 가능한 좌표 확인
    if x1 == x2: # 로봇이 가로로 놓여져 있을 때, 위 2개, 아래 2개 블록이 0 이여야 회전할 수 있다.
        for i in [-1, 1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_position_a = {(x1, y1), (x1 + i, y1)}
                next_position_b = {(x2, y2), (x2 + i, y2)}
                next_position_list.append(next_position_a)
                next_position_list.append(next_position_b)

    elif y1 == y2: # 로봇이 세로로 놓여져 있을 때, 좌 2개, 우 2개 블록이 0 이여만 회전할 수 있다.
        for i in [-1, 1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_position_a = {(x1, y1), (x1, y1 + i)}
                next_position_b = {(x2, y2), (x2, y2 + i)}
                next_position_list.append(next_position_a)
                next_position_list.append(next_position_b)

    return next_position_list

def solution(board):
    # 회전이 있기 때문에 외벽을 세워서 분기문을 하나 지워준다.
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    board = new_board

    position = {(1, 1), (1, 2)}
    queue = deque()
    visited = []
    queue.append((position, 0))
    visited.append(position)

    while queue:
        position, time = queue.popleft()

        # 로봇의 양 끝 중 하나라도 도착 지점에 도달한다면 종료
        if (n, n) in position:
            return time

        for next_position in get_next_position(position, board):
            if next_position not in visited:
                visited.append(next_position)
                queue.append((next_position, time + 1))

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))