def solution(rows, columns, queries):
    answer = []
    grid = [[0] * columns for _ in range(rows)]

    # 1씩 증가하는 2차원 배열을 만든다.
    count = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = count
            count += 1

    # 각 테두리 회전 후 최소값을 하나씩 answer 배열에 담아 반환한다.
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, grid))

    return answer

def rotate(x1, y1, x2, y2, grid):
    first = grid[x1][y1]
    min_value = grid[x1][y1]

    # 회전
    # 1. 왼쪽  -> 아래에서 위로
    for k in range(x1, x2):
        grid[k][y1] = grid[k + 1][y1]
        min_value = min(min_value, grid[k + 1][y1])

    # 2. 아래쪽 -> 오른쪽에서 왼쪽으로
    for k in range(y1, y2):
        grid[x2][k] = grid[x2][k + 1]
        min_value = min(min_value, grid[x2][k + 1])

    # 3. 오른쪽 -> 위에서 아래로
    for k in range(x2, x1, -1):
        grid[k][y2] = grid[k - 1][y2]
        min_value = min(min_value, grid[k - 1][y2])

    # 4. 위쪽 -> 왼쪽에서 오른쪽으로
    for k in range(y2, y1 + 1, -1):
        grid[x1][k] = grid[x1][k - 1]
        min_value = min(min_value, grid[x1][k - 1])

    # first 를 대입
    grid[x1][y1 + 1] = first

    # 최소값 반환
    return min_value

print(solution(rows=6, columns=6, queries=[[2,2,5,4], [3,3,6,6], [5,1,6,3]]))
