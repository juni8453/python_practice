def solution(line):
    # x = bf - ed / ad - bc
    # y = ec - af / ad - bc

    n = len(line)
    answer = []
    cross = []
    max_x = -1e15
    min_x = 1e15
    max_y = -1e15
    min_y = 1e15

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]

            # 예외 처리
            if (a * d) - (b * c) == 0:
                continue

            # # 공식 사용 후 정수 교점 구하기
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if int(x) == x and int(y) == y:
                cross.append((int(x), int(y)))

                # 최소, 최대 x, y 값 구하기
                if max_x < x: max_x = int(x)
                if max_y < y: max_y = int(y)
                if min_x > x: min_x = int(x)
                if min_y > y: min_y = int(y)

    # 최소로 필요한 배열 길이 설정 후 2차원 배열 초기화
    # x, y 는 좌표 평면 기준 x, y 를 뜻하므로 x 는 열, y 는 행 으로 생각해야한다.
    grid_x = max_x - min_x + 1
    grid_y = max_y - min_y + 1
    grid = [['.'] * grid_x for _ in range(grid_y)]

    # 2차원 배열에 별 찍기
    for star_x, star_y in cross:
        if min_x < 0: # 좌표 값 x 의 최소값이 음수라면, 2차원 배열은 0 부터 시작하므로 그 만큼 밀어줘야 함.
            nx = star_x + abs(min_x)
        else: # 최소 값이 0 이 아니라면 그냥 최소 값을 빼주면 된다.
            nx = star_x - min_x
        if star_y < 0: # 똑같이 y 최소값이 음수일 때, 밀어주기
            ny = star_y + abs(min_y)
        else:
            ny = star_y - min_y

        # x 는 열, y 는 행이기 때문에 거꾸로 넣기
        grid[ny][nx] = '*'

    for line in grid:
        answer.append(''.join(line))

    # 뒤집어서 반환
    # 처음부터 끝까지 -1 간격으로 슬라이싱 (즉, 거꾸로 뒤집기)
    return answer[::-1]

print(solution(line=[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution(line=[[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
