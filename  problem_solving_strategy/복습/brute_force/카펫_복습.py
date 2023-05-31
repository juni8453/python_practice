# 생 구현 풀이
def solution(brown, yellow):
    answer = []
    cases = []
    sum_tile = brown + yellow
    for x in range(1, sum_tile + 1):
        if sum_tile % x == 0:
            cases.append((x, sum_tile // x))

    # sorted() 시 결과 Type 은 list 이므로 set 중복제거를 위해선 tuple 로 다시 바꿔줘야한다.
    cases = list(set(tuple(sorted(sublist)) for sublist in cases))

    # 가로 길이 >= 세로 길이
    # (x, y) -> x 는 세로 길이, y 는 가로 길이
    # 2차원 배열을 만든다.
    for case in cases:
        # 4군데의 모퉁이에서 곂치므로 -4로 초기화한다.
        b_count = -4
        high, width = case

        # 중앙 타일이 있으려면 최소 가로, 세로 길이가 2보다는 커야한다.
        if high > 2 and width > 2:
            grid = [['Y' for i in range(width)] for j in range(high)]

            # (위) 가로 방향으로 B 채우기
            for i in range(width):
                grid[0][i] = 'B'
                b_count += 1

            # (아래) 가로 방향으로 B 채우기
            for i in range(width):
                grid[high - 1][i] = 'B'
                b_count += 1

            # (왼쪽) 세로 방향으로 B 채우기
            for i in range(high):
                grid[i][0] = 'B'
                b_count += 1

            # (오른쪽) 세로 방향으로 B 채우기
            for i in range(high):
                grid[i][width - 1] = 'B'
                b_count += 1

            if sum_tile - b_count == yellow:
                answer.append(width)
                answer.append(high)
                break

    return answer

# 개선한 풀이
def solution(brown, yellow):
    answer = []
    cases = []

    sum_tile = brown + yellow

    # 전체 타일에서 가로, 세로가 3 이상인 모든 경우의 수를 뽑아온다.
    for x in range(1, sum_tile + 1):
        if sum_tile % x == 0:
            y = sum_tile // x
            if x > 2 and y > 2:
                cases.append((x, y))

    # cases 중복 제거
    cases = list(set(tuple(sorted(sublist)) for sublist in cases))

    for case in cases:
        # 가로 >= 세로
        high, width = case
        if (high - 2) * (width - 2) == yellow:
            answer.append(width)
            answer.append(high)

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))