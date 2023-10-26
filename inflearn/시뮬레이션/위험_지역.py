def search(x, y, n, trap_check, board):
    count = 0
    # 상, 하, 좌, 후, 상우, 상좌, 하우, 하좌
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                if not trap_check[nx][ny]:
                    trap_check[nx][ny] = True
                    count += 1
    return count

def solution(board):
    answer = 0
    n = len(board)
    visit_check = [[False for _ in range(n)] for _ in range(n)]
    trap_check = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visit_check[i][j]:
                visit_check[i][j] = True # 방문 표시
                if board[i][j] == 1: # 지뢰 매설 지역
                    count = search(i, j, n, trap_check, board)
                    answer += count

    return answer


print(solution([
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

print(solution([
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]))

print(solution([
    [0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0]
]))

print(solution([
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0]
]))