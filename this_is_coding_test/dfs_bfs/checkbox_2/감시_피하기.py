# 어느 한 경우라도 선생님이 학생을 찾을 수 없다면, 성공하는 것으로 반환후 끝내기 (백트래킹)

from collections import deque

n = int(input())
grid = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    grid.append(list(input().split()))

def search_student():  # 장애물 3개 설치 후 탐색
    queue = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'T':
                queue.append((i, j))

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            while 0 <= next_x < n and 0 <= next_y < n:
                if grid[next_x][next_y] == 'S':
                    return False
                elif grid[next_x][next_y] == 'O':
                    break
                else:
                    next_x += dx[i]
                    next_y += dy[i]

    return True # 성공적인 장애물 설치

def make_wall(wall_count):  # 장애물을 하나 씩 설치
    if wall_count == 3:
        if search_student(): # 백트래킹 (하나라도 선생님이 학생을 찾지 못하는 경우의 수가 있다면 바로 True 반환하고 끝내기)
            return True
        else:
            return False # 아래 if make_wall(wall_count+1) 에서 None 을 받지 않기 위해 False 를 명시적으로 반환해야 한다.

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'X':
                grid[i][j] = 'O'
                if make_wall(wall_count + 1): # 선생님이 학생을 찾지 못하는 경우의 수를 찾았다면 True 반환 (다시 O -> X 로 못돌리게)
                    return True
                grid[i][j] = 'X'

answer = make_wall(0)

if answer: # 잘 숨었는가 ?
    print('YES')
else: # 들켰는가 ?
    print('NO')
