from collections import deque

n = int(input())
data = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data.append(list(input().split()))

def search_student():
    queue = deque()
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'T':
                queue.append((i, j)) # 선생님 좌표 위치 Queue 에 삽입

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            # 한 방향을 잡고 나가야하기 때문에 while 사용
            while 0 <= next_x < n and 0 <= next_y < n:
                if data[next_x][next_y] == 'S': # 감시 위치에 학생이 있다면 실패
                    return False
                elif data[next_x][next_y] == 'O': # 벽을 만나면 해당 방향 탐색 종료
                    break
                else:
                    next_x += dx[i]
                    next_y += dy[i]

    # 전부 확인했음에도 학생을 감지하지 못했다면 성공
    return True

def make_wall(wall_count):
    if wall_count == 3:
        if search_student():
            return True
        else:
            return False

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                if make_wall(wall_count + 1):
                     return True
                data[i][j] = 'X'

answer = make_wall(0)

if answer:
    print('YES')
else:
    print('NO')
