import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point = deque()
dx = [-1, 0, 1, 0] # 상, 우, 하, 좌
dy = [0, 1, 0, -1]
count = 0

# (r = 7, c = 4 시작)
point.append((r, c, d, count))
while point:
    cur_x, cur_y, cur_d, count = point.popleft()
    if board[cur_x][cur_y] == 0:
        board[cur_x][cur_y] = 2 # 2 로 바꾸면 청소된 것
        count += 1

    # 현재 칸의 상, 하, 좌, 우 4칸 중 청소 안된 칸이 없는 경우 후진 가능하면 후진, 후진 불가능하면 멈춤
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0: # 청소 안된 경우가 하나라도 있다면, 90도 좌회전하고 board[nx][ny] 가 청소되지 않았으면 이동 -> 1번으로 이동
                cur_d = (cur_d + 3) % 4
                nx = cur_x + dx[cur_d]
                ny = cur_y + dy[cur_d]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0:
                        point.append((nx, ny, cur_d, count))
                        break # 1번으로 이동 (새 좌표부터 다시 시작)
            else:
                continue

        # 청소 안된 구역이 없다면,
        # 현재 d 방향을 유지한채로 후진 가능한지 확인
        reverse_d = (cur_d + 2) % 4
        nx = cur_x + dx[reverse_d]
        ny = cur_y + dy[reverse_d]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] != 1: # 후진하는 칸이 벽이 아니라면 후진 가능
                point.append((nx, ny, cur_d, count))
                break

        elif board[nx][ny] == 1: # 후진하는 칸이 벽이라면 후진 불가
            break

print(count)


