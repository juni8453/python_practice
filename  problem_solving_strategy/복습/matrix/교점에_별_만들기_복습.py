def solution(line):
    answer = []
    position = []
    max_x = -2100000000
    max_y = -2100000000
    min_x = 2100000000
    min_y = 2100000000

    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]

            # 두 직선이 같거나 평행한 경우는 건너뜀
            if (a * d) - (b * c) == 0:
                continue

            # 교점 구하는 공식 사용
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            # 정수형 교점만 취급하도록 설정
            if x == int(x) and y == int(y):
                position.append([int(x), int(y)])

                # 교점을 구하는 즉시 2차원 배열을 위한 max_x, min_x, max_y, min_y 를 구해준다.
                if max_x < x:
                    max_x = int(x)
                if max_y < y:
                    max_y = int(y)
                if min_x > x:
                    min_x = int(x)
                if min_y > y:
                    min_y = int(y)

    # 별을 찍을 2차원 배열 생성
    grid = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    # 이제 position 교점 좌표를 기준으로 이차원 배열에 별을 삽입한다.
    for pos in position:
        x, y = pos

        # 이차원 배열의 행은 좌표평면 상 y, 열은 좌표평면 상 x 이다.
        grid[y - min_y][x - min_x] = '*'

        answer = [''.join(grid_line) for grid_line in grid]

    # 역순으로 뒤집고 반환
    return answer[::-1]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))