# 기준이 (0,0) 이 아닌 (1,1) 이기 때문에 n + 1 로 배열 설정

n, m = map(int, input().split())
grid = [[0] * (n + 1)]
sum_grid = [[0] * (n + 1) for _ in range(n + 1)]

# 인덱스를 1부터 사용하기 위해
for i in range(n):
    grid_row = [0] + list(map(int, input().split()))
    grid.append(grid_row)

# 이차원 합 배열 공식 사용
# sum_grid[i][j] = sum_grid[i][j - 1] + sum_grid[i - 1][j] + grid[i][j] - sum_grid[i - 1][j - 1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_grid[i][j] = sum_grid[i][j - 1] + sum_grid[i - 1][j] + grid[i][j] - sum_grid[i - 1][j - 1]

# 합 배열 참고, 해당 구간 합 구하기 공식 사용
# sum_grid[x2][y2] - sum_grid[x1 - 1][y2] - sum_grid[x2][y1 - 1] + sum_grid[x1 - 1][y1 - 1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sum_grid[x2][y2] - sum_grid[x1 - 1][y2] - sum_grid[x2][y1 - 1] + sum_grid[x1 - 1][y1 - 1]
    print(answer)

