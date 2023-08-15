import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 인덱스와 input 범위를 맞추기 위해 n + 1 만큼 지정
# A = [[0, 0, 0, 0, 0]]
# D = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

# 기본 배열 초기화
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 2차원 합 배열 초기화
# D[2][2] = D[2][1] + D[1][2] - D[1][1] + A[2][2]
# D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

# 구간 좌표를 입력 받고 구간 합 추출
# D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 -1] + D[x1 -1][y1 - 1]
    print(result)


