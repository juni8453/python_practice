from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, place):
    queue = deque()
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[x][y] = True
    queue.append((x, y, 0))

    while queue:
        x, y, level = queue.popleft()

        # level이 2 이상이라면 맨해튼 거리를 더 따질 필요가 없다.
        if level > 2:
            continue

        # 자기 자신이 아니면서 다른 시작 위치가 0 이 아닌 상태에서 다른 응시자를 만난다면
        # if level > 2 를 거쳤기 때문에 맨해튼 거리가 2 이하라서 바로 False 반환
        if level != 0 and place[x][y] == 'P':
            return False

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny]:
                    if place[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, level + 1))

    return True


def check_room(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                # 거리두기를 지키지 못하는 응시자가 발견되는지 확인
                if not bfs(i, j, place):
                    return False
    return True

def solution(places):
    answer = []

    for place in places:
        if check_room(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))



