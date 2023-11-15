dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 2차원 배열을 탐색
# 방문하지 않았고
# 1 인 격자를 발견하면 탐색 시작

# 위와 같은 내용으로 탐색
# 탐색 종료 후 빠져나오면서 영역 카운팅
count = 0


def search(x, y, visited, n, board):
    global count
    visited[x][y] = True  # 탐색이 시작되는 순간 방문 체크, 카운팅
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == 1:
                search(nx, ny, visited, n, board)

    return count


def solution(board):
    answer = []
    global count
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 1:
                count = 0
                count = search(i, j, visited, n, board)
                answer.append(count)

    return answer


print(solution([
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0]
]))

print(solution([
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0]
]))

print(solution([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0]
]))

print(solution([
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0]
]))
