def solution(n):
    answer = []

    # 알아낸 사실
    # 총 꺾는 횟수는 n 과 동일하다.
    # 꺾일 때 마다 원소를 채우는 횟수가 1 씩 감소한다.

    # 먼저 2차원 배열을 만든다.
    grid = [[0 for _ in range(n)] for _ in range(n)]

    count = 1
    x = -1 # grid[0][0] 로 만들기 위해선 최초 x 는 0 이 아니라 -1 이여야 한다.
    y = 0

    # 총 꺾는 횟수는 n 과 동일하고 꺾일 때 마다 원소를 채우는 횟수가 1 씩 감소하므로,
    # 아래와 같이 2중 반복문을 짤 수 있다.
    for i in range(n):
        for j in range(i, n):
            angle = i % 3 # 나머지를 사용한다.
            # 아래
            if angle == 0: # angle 이 0, 3, 6 ..이라는 것은, 한번도 꺾지 않은 상태라는 것
                x += 1
            # 우측
            if angle == 1: # angle 이 1, 4, 7 ..이라는 것은, 한번 꺾은 상태라는 것
                y += 1
            # 좌측 대각선 위
            if angle == 2: # angle 이 2, 5, 8 ..라는 것은, 2번 꺾은 상태라는 것
                x -= 1
                y -= 1

            grid[x][y] = count
            count += 1

    # 1. for grid_line in gird
    # 2. for i in grid_line
    # 3. i 추출 완료
    answer = [i for grid_line in grid for i in grid_line if i != 0]

    return answer

print(solution(4))