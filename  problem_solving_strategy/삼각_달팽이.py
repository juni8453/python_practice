def solution(n):
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    board = [[0] * n for _ in range(n)]

    x = 0
    y = 0
    angle = 0 # 3개의 방향 각도, 0 으로 설정해서 아래 방향부터 채운다.
    count = 1
    board_size_by_filled = n * (n + 1) // 2

    while count <= board_size_by_filled:
        board[x][y] = count

        # 현재 방향에 더 채울 칸이 있다면 각도는 그대로 냅두고 x, y 를 방향에 맞춰 갱신한다.
        nx = dx[angle] + x
        ny = dy[angle] + y
        count += 1

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                x = nx
                y = ny

        # 현재 방향을 다 채웠다면 각을 변경한다.
        else:
            angle = (angle + 1) % 3 # 0을 나눌 수 없으니 1 더하기
            x += dx[angle] # n = 4 대각이라면 (3,3) -> (2,2) 로 이동
            y += dy[angle]

    answer = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            answer.append(board[i][j])

    return answer

print(solution(4))