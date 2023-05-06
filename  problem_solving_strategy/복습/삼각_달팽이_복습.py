def solution(n):
    answer = []
    board = [[0] * n for _ in range(n)]
    x, y = -1, 0 # 아래부터 채워지므로 x = -1 로 초기
    count = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1

            elif i % 3 == 1:
                y += 1

            elif i % 3 == 2:
                x -= 1
                y -= 1

            board[x][y] = count
            count += 1

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                answer.append(board[i][j])

    return answer

print(solution(4))
print(solution(5))
print(solution(6))
