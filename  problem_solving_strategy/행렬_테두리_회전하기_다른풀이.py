def solution(rows, columns, queries):
    answer = []
    grid = [[0] * columns for _ in range(rows)]

    grid_count = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = grid_count
            grid_count += 1

    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        row1 = grid[x1][y1:y2]
        row2 = grid[x2][y1 + 1:y2 + 1]
        _min = min(row1 + row2) # 배열 합친 후 최소 값 구하기

        for i in range(x2, x1, -1):
            grid[i][y2] = grid[i - 1][y2]
            _min = min(_min, grid[i - 1][y2])

        for i in range(x1, x2):
            grid[i][y1] = grid[i + 1][y1]
            _min = min(_min, grid[i + 1][y1])

        # 빼뒀던 row1, row2 를 덧붙여준다.
        grid[x1][y1 + 1:y2 + 1] = row1
        grid[x2][y1:y2] = row2

        answer.append(_min)

    return answer

print(solution(rows=6, columns=6, queries=[[2,2,5,4], [3,3,6,6], [5,1,6,3]]))
print(solution(rows=3, columns=3, queries=[[1,1,2,2], [1,2,2,3], [2,1,3,2], [2,2,3,3]]))