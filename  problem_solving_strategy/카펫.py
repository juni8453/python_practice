def solution(brown, yellow):
    answer = []
    sum_tile_count = brown + yellow

    for h_len in range(3, sum_tile_count):
        w_len = sum_tile_count // h_len
        b_count = 0
        y_count = 0

        # h_len = 3, w_len = 4
        grid = [[''] * w_len for _ in range(h_len)]

        # 맨 위 B
        for i in range(w_len):
            grid[0][i] = 'B'

        # 맨 아래 B
        for i in range(w_len):
            grid[h_len - 1][i] = 'B'

        # 맨 왼쪽 B
        for i in range(h_len):
            grid[i][0] = 'B'

        # 맨 오른쪽 B
        for i in range(h_len):
            grid[i][w_len - 1] = 'B'

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'B':
                    b_count += 1
                else:
                    y_count += 1

        if b_count == brown and y_count == yellow:
            answer.append(w_len)
            answer.append(h_len)
            break

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))