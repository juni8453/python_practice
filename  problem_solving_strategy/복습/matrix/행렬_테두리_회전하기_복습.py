def solution(rows, columns, queries):
    answer = []
    count = 1
    grid = [[0 for i in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = count
            count += 1

    for x1, y1, x2, y2 in queries:
        x1 -= 1 # 1 빼줘야 인덱스 값과 일치
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # [x1][y1] 값 저장
        save = grid[x1][y1]
        min_value = save

        # 왼쪽 회전 (아래에서 위로)
        for i in range(x1, x2):
            # [1][1] = [2][1]
            # [2][1] = [1][1] ...
            grid[i][y1] = grid[i + 1][y1]
            min_value = min(min_value, grid[i][y1])

        # 아래 회전 (오른쪽에서 왼쪽으로)
        for i in range(y1, y2):
            # [4][1] = [4][2]
            grid[x2][i] = grid[x2][i + 1]
            min_value = min(min_value, grid[x2][i])

        # 오른쪽 회전 (위에서 아래로)
        for i in range(x2, x1, -1):
            # [4][3] = [3][3]
            # [3][3] = [2][3]
            grid[i][y2] = grid[i - 1][y2]
            min_value = min(min_value, grid[i][y2])

        # 위 회전 (왼쪽에서 오른쪽으로)
        for i in range(y2, y1, -1):
            # [1][3] = [1][2]
            grid[x1][i] = grid[x1][i - 1]
            min_value = min(min_value, grid[x1][i])

        grid[x1][y1 + 1] = save
        answer.append(min_value)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
