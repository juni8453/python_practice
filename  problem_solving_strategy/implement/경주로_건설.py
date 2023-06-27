from collections import deque

# 북, 남, 서, 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_corner(dir, next_dir):
    if (dir == 'RIGHT' or dir == 'LEFT') and (next_dir == 'UP' or next_dir == 'DOWN'):
        return True

    if (dir == 'UP' or dir == 'DOWN') and (next_dir == 'RIGHT' or next_dir == 'LEFT'):
        return True

    return False

def bfs(n, board):
    answer = 1e15
    visited_and_cost = [[False] * n for _ in range(n)]
    visited_and_cost[0][0] = True

    queue = deque()
    queue.append((0, 0, 0, ''))  # (x, y, fee, dir)에서 dir을 문자로 저장하여 방향을 표현

    while queue:
        x, y, fee, dir = queue.popleft()

        # 도착을 했다면 최소 비용 셋팅
        if x == n - 1 and y == n - 1:
            answer = min(answer, fee)

        for i in range(4):
            next_x = dx[i] + x
            next_y = dy[i] + y
            next_dir = ''

            if i == 0:
                next_dir = 'UP'
            elif i == 1:
                next_dir = 'DOWN'
            elif i == 2:
                next_dir = 'LEFT'
            elif i == 3:
                next_dir = 'RIGHT'

            if 0 <= next_x and next_x < n and 0 <= next_y and next_y < n:
                # 여기서 방문까지 확인하지는 않는다.
                # 현재 판단중인 비용이 이전에 지금 좌표의 산정된 비용보다 더 작은 경우가 있을 수 있기 때문에
                # 일단 이전 비용과 산정한 현재 비용을 비교해야하기 때문
                if board[next_x][next_y] == 0:
                    next_fee = fee + 100

                    if is_corner(dir, next_dir):
                        next_fee += 500

                    # 처음 방문이라면 현재 산정된 비용 넣어주고, 이미 값이 있는 상태라면 이전에 산정된 값과 현재 산정된 값을 비교해서
                    # 현재 산정된 값이 더 작을 때 값을 갱신한다.
                    if not visited_and_cost[next_x][next_y] or next_fee <= visited_and_cost[next_x][next_y]:
                        visited_and_cost[next_x][next_y] = next_fee
                        queue.append((next_x, next_y, next_fee, next_dir))

    return answer

def solution(board):
    n = len(board)
    return bfs(n, board)

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))

board =  [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))

board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(board))

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))

