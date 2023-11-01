dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
my_board = []
visited = []


def DFS(x, y):
    global visited
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < 5 and 0 <= ny < 5: # 격자를 침범하지 않으면서,
            if my_board[nx][ny] == 1 and not visited[nx][ny]: # 1번이면서 아직 방문하지 않은 경우,
                visited[nx][ny] = True
                DFS(nx, ny) # 계속해서 탐색


def solution(board):
    global my_board
    global visited
    my_board = board
    visited = [[False for _ in range(5)] for _ in range(5)]
    count = 0

    for i in range(5):
        for j in range(5):
            if my_board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                DFS(i, j) # 탐색 시작
                count += 1

    return count


print(solution([
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0]
]))

print(solution([
    [1,1,1,0,1],
    [1,1,1,0,1],
    [0,0,1,0,0],
    [1,1,0,1,0],
    [1,0,1,0,0]
]))
